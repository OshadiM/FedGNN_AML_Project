import torch
import torch.optim as optim
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from gnn_model import SimpleGCN

print("\n=== FedGNN Project: Phase 6 Training the GNN Model with Visualization ===")

# 1. Load the dataset and build the graph
df = pd.read_csv('data/aml_transactions.csv')
G = nx.from_pandas_edgelist(
    df, 'sender_account', 'receiver_account', 
    ['amount', 'location_risk_score', 'is_fraud'], 
    create_using=nx.DiGraph()
)

nodes = list(G.nodes())
node_mapping = {node: i for i, node in enumerate(nodes)}

# 2. Feature Engineering for Nodes
features = np.zeros((len(nodes), 4))
labels = np.zeros(len(nodes), dtype=int)

for i, node in enumerate(nodes):
    in_edges = G.in_edges(node, data=True)
    out_edges = G.out_edges(node, data=True)
    
    in_deg = len(in_edges)
    out_deg = len(out_edges)
    total_edges = in_deg + out_deg
    
    if total_edges > 0:
        avg_amt = (sum([d['amount'] for u, v, d in in_edges]) + sum([d['amount'] for u, v, d in out_edges])) / total_edges
        avg_risk = (sum([d['location_risk_score'] for u, v, d in in_edges]) + sum([d['location_risk_score'] for u, v, d in out_edges])) / total_edges
    else:
        avg_amt, avg_risk = 0, 0
        
    features[i] = [in_deg, out_deg, avg_amt, avg_risk]
    is_fraud = 1 if any([d['is_fraud'] == 1 for u, v, d in out_edges]) else 0
    labels[i] = is_fraud

features = (features - features.mean(axis=0)) / (features.std(axis=0) + 1e-8)
x = torch.tensor(features, dtype=torch.float32)
y = torch.tensor(labels, dtype=torch.long)

edge_list = [[node_mapping[u], node_mapping[v]] for u, v in G.edges()]
edge_index = torch.tensor(edge_list, dtype=torch.long).t().contiguous()

# 3. Initialize Model
model = SimpleGCN(in_features=4, hidden_dim=16, out_classes=2)
optimizer = optim.Adam(model.parameters(), lr=0.01)
criterion = torch.nn.NLLLoss()

# Arrays to store metrics for the plot
history_loss = []
history_acc = []

print(f"[INFO] Starting Training Loop for {len(nodes)} Accounts...")

# 4. Training Loop
epochs = 50
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    
    out = model(x, edge_index)
    loss = criterion(out, y)
    
    loss.backward()
    optimizer.step()
    
    # Calculate accuracy
    _, pred = out.max(dim=1)
    correct = int(pred.eq(y).sum().item())
    acc = (correct / len(y)) * 100
    
    # Save metrics for plotting
    history_loss.append(loss.item())
    history_acc.append(acc)
    
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1:02d}/{epochs} | Loss: {loss.item():.4f} | Accuracy: {acc:.2f}%")

print("[SUCCESS] Model Training Completed!")

# 5. Plotting the Learning Curves
print("[INFO] Generating visual performance graphs...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot Loss
ax1.plot(range(1, epochs + 1), history_loss, color='red', linewidth=2, marker='o', markersize=4)
ax1.set_title('Model Loss over Time (Lower is Better)')
ax1.set_xlabel('Epochs (Training Steps)')
ax1.set_ylabel('Loss (Error)')
ax1.grid(True, linestyle='--', alpha=0.6)

# Plot Accuracy
ax2.plot(range(1, epochs + 1), history_acc, color='green', linewidth=2, marker='s', markersize=4)
ax2.set_title('Model Accuracy over Time (Higher is Better)')
ax2.set_xlabel('Epochs (Training Steps)')
ax2.set_ylabel('Accuracy (%)')
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()