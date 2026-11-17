import torch
import copy
from gnn_model import SimpleGCN

print("\n=== FedGNN Project: Phase 3 Federated Learning Aggregation ===")

# 1. Initialize the Global Model (Central Server)
in_feats = 4
hidden_dim = 16
out_classes = 2
global_model = SimpleGCN(in_features=in_feats, hidden_dim=hidden_dim, out_classes=out_classes)

# 2. Simulate Local Models for different institutions (e.g., Bank A and Bank B)
print("[INFO] Simulating local training at Bank A and Bank B...")
bank_a_model = SimpleGCN(in_features=in_feats, hidden_dim=hidden_dim, out_classes=out_classes)
bank_b_model = SimpleGCN(in_features=in_feats, hidden_dim=hidden_dim, out_classes=out_classes)

# Simulating local weight updates (mocking the training process)
with torch.no_grad():
    for param in bank_a_model.parameters():
        param.add_(torch.randn(param.size()) * 0.05)
    for param in bank_b_model.parameters():
        param.add_(torch.randn(param.size()) * 0.05)

# 3. Federated Averaging (FedAvg) Algorithm
def federated_averaging(global_model, local_models):
    global_dict = global_model.state_dict()
    for k in global_dict.keys():
        # Average the weights of all local models for each layer
        global_dict[k] = torch.stack([local_models[i].state_dict()[k].float() for i in range(len(local_models))], 0).mean(0)
    global_model.load_state_dict(global_dict)
    return global_model

# 4. Execute Aggregation
print("[INFO] Aggregating local model weights into the Global Model securely...")
local_models_list = [bank_a_model, bank_b_model]
global_model = federated_averaging(global_model, local_models_list)

print("[SUCCESS] Federated Averaging (FedAvg) completed!")
print("[SUCCESS] Global model successfully updated with cross-bank knowledge without sharing raw transaction data.")