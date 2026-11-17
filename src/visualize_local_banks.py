import pandas as pd
import networkx as nx
from pyvis.network import Network

print("\n=== FedGNN Project: Visualizing Local Bank Networks ===")

# 1. Load the dataset
df = pd.read_csv('data/aml_transactions.csv')

# 2. Simulate Data Privacy (Splitting data for Bank A and Bank B)
# In real life, these two banks would have entirely separate databases
mid_point = len(df) // 2
df_bank_a = df.iloc[:mid_point]
df_bank_b = df.iloc[mid_point:]

def create_bank_html(dataframe, bank_name, output_filename, node_color):
    # Build NetworkX Graph for the local bank
    G = nx.from_pandas_edgelist(
        dataframe, 'sender_account', 'receiver_account', 
        ['amount', 'is_fraud'], create_using=nx.DiGraph()
    )
    
    # Initialize PyVis
    net = Network(height='600px', width='100%', bgcolor='#222222', font_color='white', directed=True)
    
    for node in G.nodes():
        net.add_node(node, label=node, title=f"{bank_name} Account: {node}", color=node_color)
        
    for u, v, d in G.edges(data=True):
        if d['is_fraud'] == 1:
            edge_color = 'red'
            hover_text = f"🚨 FRAUD!\nAmount: LKR {d['amount']:,.2f}"
            edge_width = 3
        else:
            edge_color = '#555555'
            hover_text = f"Normal\nAmount: LKR {d['amount']:,.2f}"
            edge_width = 1
            
        net.add_edge(u, v, color=edge_color, title=hover_text, value=edge_width)
        
    net.force_atlas_2based()
    net.write_html(output_filename)
    print(f"[SUCCESS] {bank_name} local network saved to '{output_filename}' (Nodes: {G.number_of_nodes()})")

# 3. Generate HTML for Bank A (Green Nodes)
create_bank_html(df_bank_a, "Bank A", "data/bank_a_network.html", "#97f2aa")

# 4. Generate HTML for Bank B (Orange Nodes)
create_bank_html(df_bank_b, "Bank B", "data/bank_b_network.html", "#ffcc99")

print("\n[INFO] Please open 'bank_a_network.html' and 'bank_b_network.html' in your browser!")