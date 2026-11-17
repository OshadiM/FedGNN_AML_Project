import pandas as pd
import networkx as nx

print("\n=== FedGNN Project: Loading Real AML Dataset ===")

# 1. Load the dataset from the CSV file
csv_path = 'data/aml_transactions.csv'
df_transactions = pd.read_csv(csv_path)
print(f"[INFO] Data loaded successfully from {csv_path}")
print(f"[INFO] Total transaction records: {len(df_transactions)}")

# 2. Build the Large Graph Network using NetworkX
print("\n[INFO] Constructing the Graph Network from CSV...")
G = nx.from_pandas_edgelist(
    df_transactions,
    source='sender_account',
    target='receiver_account',
    edge_attr=['amount', 'location_risk_score', 'is_fraud'],
    create_using=nx.DiGraph()
)

# 3. Display Graph Details
print(f"\n[SUCCESS] Large Graph successfully created!")
print(f" - Total Accounts (Nodes): {G.number_of_nodes()}")
print(f" - Total Transactions (Edges): {G.number_of_edges()}")

# Let's check how many fraud transactions are in the network
fraud_edges = [(u, v) for u, v, d in G.edges(data=True) if d['is_fraud'] == 1]
print(f" - Total Fraudulent Connections detected: {len(fraud_edges)}")