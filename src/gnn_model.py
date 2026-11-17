import torch
import torch.nn as nn
import torch.nn.functional as F

print("=== FedGNN Project: Phase 2 GNN Model Architecture ===")

# Simple Graph Convolutional Network (GCN) layer structure for Fraud Detection
# This model will analyze node features and neighboring transaction topologies to classify fraud.

class SimpleGCN(nn.Module):
    def __init__(self, in_features, hidden_dim, out_classes):
        super(SimpleGCN, self).__init__()
        # Simulating GCN feature transformations for transaction graph nodes
        self.linear1 = nn.Linear(in_features, hidden_dim)
        self.linear2 = nn.Linear(hidden_dim, out_classes)

    def forward(self, x, edge_index):
        # Forward pass through the network layers
        h = self.linear1(x)
        h = F.relu(h)
        h = F.dropout(h, training=self.training)
        out = self.linear2(h)
        return F.log_softmax(out, dim=1)

# Initialize the GNN model structure
# in_features: node attribute size, hidden_dim: hidden layer size, out_classes: Benign (0) vs Fraud (1)
in_feats = 4
hidden_dim = 16
out_classes = 2

model = SimpleGCN(in_features=in_feats, hidden_dim=hidden_dim, out_classes=out_classes)
print("\n[SUCCESS] GCN Model Initialized Successfully:")
print(model)