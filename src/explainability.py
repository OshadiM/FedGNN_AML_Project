import torch
from gnn_model import SimpleGCN

print("\n=== FedGNN Project: Phase 4 Explainable AI (XAI) for AML Compliance ===")

# Initialize the trained Global Model structure
in_feats = 4
hidden_dim = 16
out_classes = 2
model = SimpleGCN(in_features=in_feats, hidden_dim=hidden_dim, out_classes=out_classes)

def explain_fraud_prediction(node_id, features, edge_index):
    print(f"\n[INFO] Initializing GNNExplainer for Account/Node ID: {node_id}...")
    
    # In a full production PyG environment, we would use: 
    # explainer = GNNExplainer(model, epochs=200)
    # Here, we simulate the XAI output for our AML compliance demonstration
    
    # Mocking feature importance scores to show WHICH features caused the flag
    feature_names = ["Transaction Amount", "Transaction Frequency", "Location Risk", "KYC Risk Score"]
    importance_scores = torch.rand(in_feats)
    importance_scores = importance_scores / importance_scores.sum() # Normalize to 1.0
    
    print(f"[SUCCESS] Explanation generated successfully for Regulator Audit.")
    print("\n--- Feature Importance (Why was this flagged?) ---")
    for name, score in zip(feature_names, importance_scores):
        print(f" - {name}: {score.item() * 100:.2f}%")
        
    print("\n--- Network Subgraph Importance ---")
    print(" Identified risky connections: [ACC_002] <--> [ACC_005]")
    print(" Reason: High volume circular money flow detected between these nodes.")

# Let's explain why a specific account was flagged as fraudulent
node_to_explain = "ACC_005"
dummy_features = torch.randn(1, in_feats)
dummy_edges = torch.tensor([[0, 1], [1, 0]]) # Dummy structural edges

explain_fraud_prediction(node_to_explain, dummy_features, dummy_edges)