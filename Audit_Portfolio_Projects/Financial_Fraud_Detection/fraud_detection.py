import pandas as pd
from scipy import stats

# 1. Load the data
print("Loading transaction data...")
df = pd.read_csv('transactions.csv')

# 2. Calculate Z-Scores
# The Z-score tells us how unusual a number is.
# A score > 1.5 (for this small dataset) means it is an outlier.
df['z_score'] = stats.zscore(df['Amount'])

# 3. Set the "Risk Threshold"
threshold = 1.5

# 4. Filter for anomalies
anomalies = df[df['z_score'].abs() > threshold]

# 5. Output Results
print("\n--- AUDIT FINDINGS: HIGH RISK TRANSACTIONS DETECTED ---")
if not anomalies.empty:
    print(anomalies[['TransactionID', 'Amount', 'Vendor', 'z_score']])

    # Save to a new file for the auditor to review
    anomalies.to_csv('audit_report_findings.csv', index=False)
    print("\nSUCCESS: Findings saved to 'audit_report_findings.csv'")
else:
    print("No anomalies detected.")