import pandas as pd
import networkx as nx
import numpy as np

print("=== FedGNN Project: Phase 1 Data Ingestion & Graph Construction ===")

# 1. Mocking Node Profiles (KYC / Income Data) and Transactions
data = {
    'transaction_id': ['T1', 'T2', 'T3', 'T4', 'T5'],
    'sender_account': ['ACC_001', 'ACC_002', 'ACC_001', 'ACC_003', 'ACC_004'],
    'receiver_account': ['ACC_002', 'ACC_005', 'ACC_004', 'ACC_005', 'ACC_001'],
    'amount': [50000, 1500000, 20000, 2000000, 75000],
    'is_fraud': [0, 1, 0, 1, 0]
}

df_transactions = pd.DataFrame(data)
print("\n[INFO] Sample Transaction Data Loaded Successfully:")
print(df_transactions)

# 2. Building the Local Graph Network using NetworkX
G = nx.from_pandas_edgelist(
    df_transactions, 
    source='sender_account', 
    target='receiver_account', 
    edge_attr=['amount', 'is_fraud'], 
    create_using=nx.DiGraph()
)

print(f"\n[SUCCESS] Graph successfully created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
print("Nodes in the graph:", list(G.nodes()))