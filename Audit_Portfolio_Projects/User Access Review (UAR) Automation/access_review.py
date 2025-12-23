import pandas as pd

# 1. Load the data
print("Loading HR and System logs...")
active_users = pd.read_csv('active_users.csv')
terminated_users = pd.read_csv('terminated_users.csv')

# 2. Compare the lists (Inner Join)
# We want to find IDs that exist in BOTH 'Active' and 'Terminated' lists.
audit_findings = pd.merge(active_users, terminated_users, on='EmployeeID', how='inner')

# 3. Print the Report
print("\n--- SOX CONTROL FAILURE: TERMINATED USERS WITH ACTIVE ACCESS ---")

if not audit_findings.empty:
    # Show specific columns
    print(audit_findings[['EmployeeID', 'Name_x', 'Email', 'TerminationDate']])

    # Save to file
    audit_findings.to_csv('uar_violations.csv', index=False)
    print("\nALERT: Violations exported to 'uar_violations.csv'")
else:
    print("Control Effective: No unauthorized access found.")