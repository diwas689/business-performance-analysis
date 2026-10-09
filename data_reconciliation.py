python
import pandas as pd

def run_performance_reconciliation():
    # 1. Simulate data extraction from multiple business systems (SQL vs. ERP system)
    database_records = pd.DataFrame({
        'region_id': ['North', 'South', 'East', 'West'],
        'sql_tracked_revenue': [152000.50, 98400.75, 210500.00, 115000.20]
    })
    
    erp_system_records = pd.DataFrame({
        'region_id': ['North', 'South', 'East', 'West'],
        'erp_reported_revenue': [152000.50, 98100.00, 210500.00, 115250.00]
    })
    
    # 2. Merge data frames to cross-verify structural alignment
    merged_audit = pd.merge(database_records, erp_system_records, on='region_id')
    
    # 3. Calculate financial discrepancies between reporting networks
    merged_audit['variance'] = merged_audit['sql_tracked_revenue'] - merged_audit['erp_reported_revenue']
    merged_audit['requires_investigation'] = merged_audit['variance'] != 0
    
    # Calculate global business health indicators
    total_reconciled_revenue = merged_audit['sql_tracked_revenue'].sum()
    total_discrepancy_variance = merged_audit['variance'].abs().sum()
    
    print("============= EXECUTIVE RECONCILIATION SUMMARY =============")
    print(f"Total Audited System Revenue: ${total_reconciled_revenue:,.2f}")
    print(f"Total Discrepancy Variance Identified: ${total_discrepancy_variance:,.2f}")
    print("\nRegional Data Breakdown:")
    print(merged_audit[['region_id', 'sql_tracked_revenue', 'variance', 'requires_investigation']])
    print("=============================================================")
    
    # Export clean audit log ready for management review
    merged_audit.to_csv('reconciled_business_performance.csv', index=False)

if __name__ == "__main__":
    run_performance_reconciliation()
