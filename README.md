<h1 align="center">FedGNN: Privacy-Preserving Anti-Money Laundering (AML) System</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-ee4c2c.svg" alt="PyTorch">
  <img src="https://img.shields.io/badge/Federated%20Learning-FedAvg-brightgreen.svg" alt="FedAvg">
  <img src="https://img.shields.io/badge/Status-Active-success.svg" alt="Status">
</p>

## Executive Summary
The **Federated Graph Neural Network (FedGNN)** is an enterprise-grade machine learning framework designed to detect complex money laundering networks across multiple financial institutions. 

Traditional AML systems fail to capture multi-hop transactional relationships, and privacy regulations (like GDPR) prevent banks from sharing raw customer data. **FedGNN solves this by combining Graph Convolutional Networks (GCN) with Federated Learning (FedAvg).** It allows banks to collaboratively train a global fraud detection model while keeping 100% of their sensitive transactional data strictly localized.

---

## Key Capabilities & Features

- **Graph-Based Fraud Detection:** Utilizes PyTorch-based GCNs to analyze the topological structure of transactions, identifying circular money flows and hidden mule accounts.
- **Privacy-Preserving Federated Learning:** Implements the `FedAvg` algorithm to aggregate model weights from isolated "Local Bank" nodes without exposing Personally Identifiable Information (PII).
- **Explainable AI (XAI):** Identifies and highlights the exact transactional subgraphs and features that trigger fraud alerts, ensuring regulatory transparency.
- **Real-Time FinTech Dashboard:** A standalone, responsive HTML/JS dashboard styled with a professional dark theme and Chart.js, providing instant visual analytics of network risk distributions.

---

## Technology Stack

| Category | Technologies Used |
| :--- | :--- |
| **Deep Learning** | PyTorch, PyTorch Geometric |
| **Federated Learning** | Custom FedAvg Implementation |
| **Graph Analytics** | NetworkX, PyVis |
| **Data Engineering** | Pandas, NumPy |
| **Frontend Analytics** | HTML5, CSS3, Chart.js, JSON |

---

## Project Architecture

```text
FedGNN_AML_Project/
├── data/                           # Datasets and generated HTML visualizations
│   ├── aml_transactions.csv        # Simulated transactional dataset
│   ├── bank_a_network.html         # Local graph visualization for Bank A
│   ├── bank_b_network.html         # Local graph visualization for Bank B
│   ├── dashboard.html              # Generated FinTech Analytics Dashboard
│   └── interactive_network.html    # Global interactive network visualization
├── lib/                            # PyVis frontend dependencies for local rendering
│   ├── bindings/
│   ├── tom-select/
│   └── vis-9.1.2/
├── src/                            # Source Code
│   ├── data_preprocessing.py       # Data cleaning and feature engineering
│   ├── explainability.py           # XAI logic for fraud prediction
│   ├── federated_learning.py       # FedAvg orchestration across simulated banks
│   ├── generate_dataset.py         # Script to simulate realistic banking data
│   ├── gnn_model.py                # Core PyTorch GCN architecture
│   ├── graph_from_csv.py           # Graph construction from tabular data
│   ├── html_dashboard.py           # Generates the static HTML dashboard
│   ├── interactive_graph.py        # PyVis interactive network generation
│   ├── train_model.py              # Main training loop
│   ├── visualize_graph.py          # Base graph visualization utilities
│   ├── visualize_local_banks.py    # Script for federated node visualizations
│   └── visualize_real_graph.py     # Real-world network rendering
├── .gitignore                      # Git ignore rules (excludes venv, __pycache__)
└── README.md                       # Project documentation