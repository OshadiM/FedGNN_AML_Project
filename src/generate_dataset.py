import pandas as pd
import numpy as np
import random
import os

print("\n=== FedGNN Project: Generating Realistic AML Dataset ===")

# Create 'data' directory if it doesn't exist
os.makedirs('data', exist_ok=True)

np.random.seed(42)
random.seed(42)
num_transactions = 1000

# Generate 100 unique bank accounts
accounts = [f"ACC_{i:04d}" for i in range(1, 101)]

# Create realistic transaction properties
data = {
    'transaction_id': [f"TRX_{i:05d}" for i in range(1, num_transactions + 1)],
    'sender_account': [random.choice(accounts) for _ in range(num_transactions)],
    'receiver_account': [random.choice(accounts) for _ in range(num_transactions)],
    'amount': np.round(np.random.uniform(100, 500000, num_transactions), 2), # Amounts between 100 and 500,000
    'location_risk_score': np.round(np.random.uniform(0, 1, num_transactions), 2),
    'is_fraud': np.random.choice([0, 1], size=num_transactions, p=[0.95, 0.05]) # 5% of transactions are marked as fraud
}

df = pd.DataFrame(data)

# Remove transactions where sender and receiver are the same (self-loops)
df = df[df['sender_account'] != df['receiver_account']]

# Save the dataset to a CSV file
csv_path = 'data/aml_transactions.csv'
df.to_csv(csv_path, index=False)

print(f"[SUCCESS] Dataset successfully saved to '{csv_path}'!")
print(f"Total Transactions: {len(df)}")
print("\nPreview of the first 5 rows:")
print(df.head())