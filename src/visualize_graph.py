import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

print("\n=== FedGNN Project: Phase 5 Visualizing the Transaction Network ===")

# Using the same dummy transaction data from Phase 1
data = {
    'transaction_id': ['T1', 'T2', 'T3', 'T4', 'T5'],
    'sender_account': ['ACC_001', 'ACC_002', 'ACC_001', 'ACC_003', 'ACC_004'],
    'receiver_account': ['ACC_002', 'ACC_005', 'ACC_004', 'ACC_005', 'ACC_001'],
    'amount': [50000, 1500000, 20000, 2000000, 75000],
    'is_fraud': [0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Create the Directed Graph representing the money flow
G = nx.from_pandas_edgelist(
    df, 'sender_account', 'receiver_account', 
    ['amount', 'is_fraud'], create_using=nx.DiGraph()
)

# Set edge colors: Red for fraudulent transactions (is_fraud = 1), Blue for normal transactions
edge_colors = ['red' if G[u][v]['is_fraud'] == 1 else 'blue' for u, v in G.edges()]

# Plot the graph structure
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42) # Keeps the node positions stable on the screen

nx.draw(
    G, pos, with_labels=True, node_color='lightblue', 
    node_size=3000, edge_color=edge_colors, width=2.0, 
    font_size=10, font_weight='bold', arrows=True, arrowsize=20
)

plt.title("AML Transaction Network (Red edges = Fraudulent Flow)", fontsize=14)
print("[INFO] Displaying graph window... (Close the window to continue)")
plt.show()