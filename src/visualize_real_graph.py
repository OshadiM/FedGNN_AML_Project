import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

print("\n=== FedGNN Project: Visualizing the Real AML Network ===")

# 1. Load the real synthetic dataset
df = pd.read_csv('data/aml_transactions.csv')

# 2. Build the Graph
G = nx.from_pandas_edgelist(
    df, 'sender_account', 'receiver_account', 
    ['amount', 'is_fraud'], create_using=nx.DiGraph()
)

print(f"[INFO] Rendering Network with {G.number_of_nodes()} Nodes and {G.number_of_edges()} Edges...")

# 3. Set Colors (Red for Fraud, Light Gray for Normal transactions so the fraud pops out)
edge_colors = ['red' if d['is_fraud'] == 1 else 'lightgray' for u, v, d in G.edges(data=True)]

# 4. Plot the large graph
plt.figure(figsize=(12, 8)) # Larger figure size for the big network
pos = nx.spring_layout(G, seed=42, k=0.15) # 'k' adjusts the spacing between nodes

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=100, alpha=0.9)

# Draw edges
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=1.2, alpha=0.7, arrows=True, arrowsize=10)

# (We are not drawing node labels here because 100 labels will make it too crowded)

plt.title("Real AML Transaction Network (Red Edges = Fraudulent Flow)", fontsize=14, fontweight='bold')
plt.axis('off') # Hide axes for a cleaner look
print("[INFO] Displaying graph window... (Zoom in to see the fraudulent connections clearly)")
plt.tight_layout()
plt.show()