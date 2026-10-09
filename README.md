markdown
# Business Performance Analysis & Reporting

This repository contains the database querying frameworks and data validation logic used to benchmark cross-regional business units. The primary emphasis of this deployment is removing transactional record redundancies, validating reporting systems, and isolating operational variance.

## Pipeline Architecture
1. **`business_performance_analysis.sql`**: Features window functions (`ROW_NUMBER() OVER...`) and Common Table Expressions (CTEs) to isolate duplicate database rows, aggregate customer metrics, and compute Average Order Values (AOV).
2. **`data_reconciliation.py`**: Conducts data reconciliation audits across decoupled datasets, calculates reporting variances, and exports structured, verified summaries ready for management compliance reviews.

## Analytical Skillsets Applied
- **Database Deduplication:** Eliminating transaction tracking replication to protect upstream reporting systems.
- **Cross-System Verification:** Performing automated audits between system database states and independent enterprise planning logs.
- **Performance Benchmarking:** Segmenting organizational performance metrics across specific temporal milestones (Fiscal Quarters) and geographic bounds.
