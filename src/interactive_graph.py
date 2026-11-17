import pandas as pd
import networkx as nx
from pyvis.network import Network

print("\n=== FedGNN Project: Creating Interactive HTML Graph ===")

# 1. Load the real synthetic dataset
df = pd.read_csv('data/aml_transactions.csv')

# 2. Build the NetworkX Graph
G = nx.from_pandas_edgelist(
    df, 'sender_account', 'receiver_account', 
    ['amount', 'is_fraud'], create_using=nx.DiGraph()
)

# 3. Initialize PyVis Network (Dark mode looks more professional for Cyber/AML)
net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white', directed=True)

# 4. Add nodes to the PyVis network
for node in G.nodes():
    net.add_node(node, label=node, title=f"Account ID: {node}", color='#97c2fc')

# 5. Add edges (connections) with hover data
for u, v, d in G.edges(data=True):
    if d['is_fraud'] == 1:
        edge_color = 'red'
        hover_text = f"🚨 FRAUDULENT FLOW!\nAmount: LKR {d['amount']:,.2f}"
        edge_width = 3 # Make fraud edges thicker
    else:
        edge_color = '#555555'
        hover_text = f"Normal Transaction\nAmount: LKR {d['amount']:,.2f}"
        edge_width = 1
        
    net.add_edge(u, v, color=edge_color, title=hover_text, value=edge_width)

# 6. Apply physics layout for a beautiful organic structure
net.force_atlas_2based()

# 7. Save the graph as an HTML file
output_path = 'data/interactive_network.html'
net.write_html(output_path)

print(f"[SUCCESS] Interactive graph saved to '{output_path}'")
print("[INFO] Please open this HTML file in your web browser (Chrome/Edge) to view it!")