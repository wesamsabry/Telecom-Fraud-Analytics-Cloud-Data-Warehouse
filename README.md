Telecom-Fraud-Analytics-Cloud-Data-Warehouse

> An end-to-end cloud data warehouse and fraud analytics platform for telecom customer 360 insights, built on Microsoft Azure using Medallion Architecture (Bronze-Silver-Gold), Star Schema, and Power BI.

The platform processes **1.4 million call records** for **5,000 telecom customers** and generates a **Fraud Score (0–100)** to classify customers into risk levels, detecting harmful calling behavior such as Vishing (Voice Phishing) and Telephone Harassment.

---

##  Project Objective

Build a scalable cloud data platform that:

- ✅ Processes telecom customer data at scale
- ✅ Detects suspicious calling behavior
- ✅ Generates explainable fraud scores
- ✅ Provides actionable business insights through dashboards
- ✅ Implements a complete Medallion Architecture pipeline

---

##  Risk Classification

| Risk Level | Score Range | Action |
|------------|-------------|--------|
| 🔴 Critical | 80 – 100 | Immediate investigation required |
| 🟠 High | 60 – 79 | High probability – investigate |
| 🟡 Medium | 30 – 59 | Needs monitoring |
| 🟢 Low | 0 – 29 | Normal behavior |

> Every fraud score is fully explainable and can be traced back to the exact rule that triggered it.

---

##  Architecture
┌─────────────────────────────────────────────────────────────────────────────┐
│ RAW CSV FILES │
│ (Calls, Customers, Recharges, Complaints) │
└─────────────────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ BRONZE LAYER (Raw Data) │
│ Azure Data Lake Storage Gen2 │
│ Immutable raw data storage │
└─────────────────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ SILVER LAYER (Cleaned Data) │
│ Azure Databricks (PySpark) │
│ 13 Data Quality Rules Applied │
│ Output: Cleaned Parquet Files │
└─────────────────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ GOLD LAYER (Star Schema) │
│ Feature Engineering + Fraud Engine │
│ Azure SQL Database / Synapse │
│ 1 Fact Table + 8 Dimension Tables │
└─────────────────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ REPORTING LAYER │
│ Power BI Dashboard │
│ 4 Interactive Pages │
│ 12+ KPIs │
└─────────────────────────────────────────────────────────────────────────────┘

text

---

##  Medallion Architecture

| Layer | Purpose | Technology |
|-------|---------|------------|
| **Bronze** | Raw data ingestion from CSV files | Azure Data Lake Storage Gen2 |
| **Silver** | Data cleaning, validation & 13 quality rules | Azure Databricks (PySpark) → Parquet |
| **Gold** | Feature engineering & fraud scoring | Azure SQL Database / Synapse (Star Schema) |

---

##  Technology Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Storage** | Azure Data Lake Storage Gen2 | Raw & cleaned data |
| **Processing** | Azure Databricks (PySpark) | Data transformation |
| **Data Warehouse** | Azure SQL Database / Synapse | Star Schema |
| **Fraud Engine** | SQL Rule-Based Engine | Fraud detection |
| **Visualization** | Power BI | Dashboards |
| **Data Generation** | Python (Pandas, NumPy) | Simulated dataset |

---

##  Fraud Rules Engine

### 🔴 Negative Indicators

| Rule | Description | Weight |
|------|-------------|--------|
| High Call Frequency | > 60 calls/day | +20 |
| Very Short Calls | Avg duration < 10 sec | +15 |
| Repeated Calls | > 10 calls/hour to same number | +15 |
| Random Number Pattern | > 20 new numbers/day + answer rate < 20% | +20 |
| Complaints | Fraud/Harassment complaints | +30 |
| High Off-net Usage | Off-net > 60% + complaints | +15 |

### 🟢 Positive Indicators

| Rule | Description | Weight |
|------|-------------|--------|
| Number Correction | 1–2 digit difference | -5 |
| Normal Call Duration | 60–300 sec | -10 |
| Regular Recharge Pattern | Consistent weekly behavior | -10 |

### Fraud Score Formula
Fraud Score = (Sum of Negative Rules) - (Sum of Positive Rules)
Fraud Score = max(0, min(100, Fraud Score))

text

---

## Project Results

| Metric | Value |
|--------|-------|
| Calls Processed | 1.4 Million |
| Customers | 5,000 |
| Fraud Rules | 9 |
| High/Critical Risk Customers | 115 |
| Data Quality | 98.8% |
| Runtime | ~15 Minutes |
| Idempotency | Verified |

### Risk Distribution
🟢 Low 65% ████████████████████████████████████████████████████████
🟡 Medium 25% █████████████████████████
🟠 High 8% ████████
🔴 Critical 2% ██

Total Customers: 5,000

text

---

## Data Warehouse Design

### Star Schema

**Fact Table**
- `fact_events_dedup`

**Dimension Tables**
- `dim_customer`
- `dim_date`
- `dim_location`
- `dim_plan`
- `dim_subscription`
- `dim_recharge`
- `dim_complaint`
- `dim_risk`

---

##  Power BI Dashboard

### Executive Dashboard
- Total Calls
- Revenue
- Fraud Rate
- Active Customers
- Revenue Trend

### Fraud Analysis
- Top 5 High-Risk Customers
- Risk Distribution
- Behavioral Patterns

### Customer Behaviour
- Age Distribution
- Subscription Type
- Average Call Duration
- Recharge Channels

### Complaints Analytics
- Total Complaints
- Resolution Days
- Complaint Categories
- Monthly Trend

---

##  Repository Structure
Telecom-Fraud-Analytics-Cloud-Data-Warehouse/
│
├── bronze/ # Raw data layer
├── silver/ # Cleaned data layer
├── gold/ # Curated data layer
│
├── scripts/ # ETL and transformation scripts
├── notebooks/ # Databricks notebooks
├── reports/ # Power BI reports
├── docs/ # Project documentation
│
└── README.md # Project overview

text

---

##  How to Run

### 1. Set up Azure resources
- Create Resource Group
- Create Storage Account (ADLS Gen2)
- Create Databricks Workspace
- Create Synapse Workspace / SQL Database

### 2. Upload raw data to Bronze layer
- Upload CSV files to `bronze/` container

### 3. Run Databricks notebooks
- `01_bronze_to_silver.ipynb` – applies data quality rules
- `02_silver_to_gold.ipynb` – builds Star Schema

### 4. Connect Power BI
- Open `Telecom_Dashboard.pbix`
- Update connection string
- Refresh and explore

---

## Future Improvements

- Machine Learning fraud detection
- Real-time streaming using Azure Event Hub
- Automated alerts for Critical Risk customers
- CI/CD deployment pipeline
