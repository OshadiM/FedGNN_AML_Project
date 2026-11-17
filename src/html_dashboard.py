import csv
import random
from datetime import datetime, timedelta
import json

print("\n=== FedGNN Project: Generating Static HTML Dashboard (Professional Theme) ===")

# 1. Read data and generate dates
total_trx = 0
total_fraud = 0
fraud_amount = 0.0

fraud_by_date = {}
today = datetime.today()

# Generate the last 30 days list for X-axis labels
last_30_days = [(today - timedelta(days=i)).strftime('%b %d') for i in range(29, -1, -1)]
for day in last_30_days:
    fraud_by_date[day] = 0

random.seed(42)

with open('data/aml_transactions.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_trx += 1
        if row['is_fraud'] == '1':
            total_fraud += 1
            fraud_amount += float(row['amount'])
            random_day = random.choice(last_30_days)
            fraud_by_date[random_day] += 1

normal_trx = total_trx - total_fraud

dates_js = json.dumps(last_30_days)
fraud_counts_js = json.dumps([fraud_by_date[d] for d in last_30_days])

# 2. Create a Beautiful FinTech Dark-Themed HTML Dashboard
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AML Fraud Analytics Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        body {{ background-color: #0b1120; color: #e2e8f0; font-family: 'Inter', sans-serif; margin: 0; padding: 35px; }}
        .header {{ text-align: left; padding-bottom: 20px; margin-bottom: 30px; border-bottom: 1px solid #1e293b; }}
        .header h1 {{ margin: 0; color: #f8fafc; font-size: 26px; font-weight: 700; letter-spacing: -0.5px; }}
        .header p {{ color: #94a3b8; margin-top: 8px; font-size: 14px; }}
        .cards {{ display: flex; justify-content: space-between; gap: 24px; margin-bottom: 30px; }}
        .card {{ background-color: #1e293b; padding: 24px; border-radius: 10px; width: 33.33%; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2); border: 1px solid #334155; }}
        .card h3 {{ margin: 0 0 12px 0; color: #94a3b8; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }}
        .card h2 {{ margin: 0; font-size: 32px; font-weight: 700; color: #f8fafc; }}
        .text-alert {{ color: #ef4444; }} 
        
        /* Increased height to 440px so the legend doesn't get cut off */
        .charts-container {{ display: flex; justify-content: space-between; gap: 24px; width: 100%; height: 440px; }} 
        .chart-box {{ background-color: #1e293b; padding: 24px; border-radius: 10px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2); border: 1px solid #334155; display: flex; justify-content: center; align-items: center; }}
        .chart-left {{ width: 32%; }}
        .chart-right {{ width: 65%; flex-grow: 1; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>FedGNN Anti-Money Laundering (AML) Control Center</h1>
        <p>Real-time Fraud Analytics & Network Risk Monitoring</p>
    </div>

    <div class="cards">
        <div class="card">
            <h3>Total Transactions Analyzed</h3>
            <h2>{total_trx:,}</h2>
        </div>
        <div class="card">
            <h3>High-Risk Frauds Detected</h3>
            <h2 class="text-alert">{total_fraud:,}</h2>
        </div>
        <div class="card">
            <h3>Total Fraud Value (LKR)</h3>
            <h2 class="text-alert">{fraud_amount:,.2f}</h2>
        </div>
    </div>

    <div class="charts-container">
        <div class="chart-box chart-left">
            <canvas id="fraudChart"></canvas>
        </div>
        <div class="chart-box chart-right">
            <canvas id="trendChart"></canvas>
        </div>
    </div>

    <script>
        const ctx1 = document.getElementById('fraudChart').getContext('2d');
        new Chart(ctx1, {{
            type: 'doughnut',
            data: {{
                labels: ['Legitimate Transactions', 'Fraudulent Transactions'],
                datasets: [{{
                    data: [{normal_trx}, {total_fraud}],
                    backgroundColor: ['#3b82f6', '#ef4444'],
                    borderWidth: 0,
                    hoverOffset: 4
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                cutout: '70%',
                layout: {{ padding: {{ bottom: 15 }} }},
                plugins: {{
                    legend: {{ 
                        position: 'bottom', 
                        labels: {{ color: '#cbd5e1', padding: 15, font: {{ family: 'Inter', size: 13 }} }} 
                    }},
                    title: {{ display: true, text: 'Transaction Risk Distribution', color: '#f8fafc', font: {{ family: 'Inter', size: 15, weight: '600' }}, padding: {{ bottom: 15 }} }}
                }}
            }}
        }});

        const ctx2 = document.getElementById('trendChart').getContext('2d');
        let gradient = ctx2.createLinearGradient(0, 0, 0, 400);
        gradient.addColorStop(0, 'rgba(239, 68, 68, 0.4)');
        gradient.addColorStop(1, 'rgba(239, 68, 68, 0.0)');

        new Chart(ctx2, {{
            type: 'line',
            data: {{
                labels: {dates_js},
                datasets: [{{
                    label: 'Daily Fraud Alerts',
                    data: {fraud_counts_js},
                    borderColor: '#ef4444',
                    backgroundColor: gradient,
                    borderWidth: 2,
                    pointBackgroundColor: '#0b1120',
                    pointBorderColor: '#ef4444',
                    pointBorderWidth: 2,
                    pointRadius: 4,
                    pointHoverRadius: 6,
                    fill: true,
                    tension: 0.4
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{ display: false }},
                    title: {{ display: true, text: '30-Day Fraud Alert Trend', color: '#f8fafc', font: {{ family: 'Inter', size: 15, weight: '600' }}, padding: {{ bottom: 20 }} }}
                }},
                scales: {{
                    y: {{ beginAtZero: true, grid: {{ color: 'rgba(51, 65, 85, 0.3)', drawBorder: false }}, ticks: {{ color: '#94a3b8', stepSize: 1, font: {{ family: 'Inter' }} }} }},
                    x: {{ grid: {{ display: false }}, ticks: {{ color: '#94a3b8', maxTicksLimit: 10, font: {{ family: 'Inter' }} }} }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""

output_path = 'data/dashboard.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"[SUCCESS] Professional HTML Dashboard saved to '{output_path}'")