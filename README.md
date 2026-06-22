# Telecom Fraud Analytics – Cloud Data Warehouse

End-to-end cloud-based fraud analytics and customer intelligence platform for telecom operators, built on Microsoft Azure using Medallion Architecture, Azure Databricks, Azure Data Lake Storage Gen2, Azure SQL/Synapse, and Power BI.

---

## Architecture

<img width="943" height="241" alt="image" src="https://github.com/user-attachments/assets/0955d066-92ee-4305-873e-c62126fe6c80" />


### Data Flow

1. Raw telecom data is ingested from CSV files.
2. Data is stored in Azure Data Lake Storage Gen2 (Bronze Layer).
3. Azure Databricks performs data cleansing, validation, and transformation.
4. Curated datasets are stored in Silver and Gold layers.
5. Azure Synapse serves as the analytical data warehouse.
6. Power BI provides executive, fraud, customer behavior, and complaint analytics dashboards.

---
## Project Overview

Telecommunication providers generate massive volumes of call records, customer interactions, transactions, and complaints every day. Detecting fraudulent activities such as voice phishing (Vishing), spam campaigns, and abusive calling behavior requires scalable data platforms capable of processing large datasets efficiently.

This project delivers a cloud-native Data Engineering and Analytics solution that integrates customer data into a centralized Customer 360 platform while providing a transparent fraud scoring engine for risk detection and operational decision-making.

### Business Objectives

* Build a scalable cloud data warehouse for telecom analytics.
* Create a unified Customer 360 view.
* Detect suspicious customer behavior using explainable fraud rules.
* Enable data-driven decision making through interactive dashboards.
* Improve data quality, governance, and reporting efficiency.

---

## Architecture

### Medallion Architecture

### Bronze Layer

* Raw telecom data ingestion.
* Call Detail Records (CDR).
* Customer profiles.
* Transactions.
* Complaints.

### Silver Layer

Data cleansing and standardization using Azure Databricks (PySpark).

Implemented:

* 13 Data Quality Rules.
* Missing value handling.
* Data type validation.
* Duplicate removal.
* Business rule validation.

### Gold Layer

Business-ready analytical datasets optimized for reporting and fraud analysis.

---

## Technology Stack

| Category       | Technology                                   |
| -------------- | -------------------------------------------- |
| Cloud Platform | Microsoft Azure                              |
| Storage        | Azure Data Lake Storage Gen2                 |
| Processing     | Azure Databricks (PySpark)                   |
| Data Warehouse | Azure SQL Database / Azure Synapse Analytics |
| Modeling       | Star Schema                                  |
| Visualization  | Power BI                                     |
| Programming    | Python, SQL                                  |
| Architecture   | Medallion Architecture                       |

---

## Data Warehouse Design

### Star Schema

#### Fact Table

* Fact_CustomerActivity

#### Dimension Tables

* DimCustomer
* DimDate
* DimRegion
* DimPlan
* DimFraudRisk
* DimComplaint
* DimCallType
* DimUsageCategory

Total:

* 1 Fact Table
* 8 Dimension Tables

---

## Fraud Scoring Engine

The fraud detection framework uses a transparent rule-based scoring model designed for explainability and operational trust.

### Fraud Indicators

Negative Indicators:

* Excessive outgoing calls
* High unique recipient count
* Short-duration call patterns
* Repeated complaint history
* Suspicious calling frequency
* High-risk behavioral activity

Positive Indicators:

* Long customer tenure
* Consistent usage behavior
* Stable payment history

### Risk Classification

| Score    | Risk Level |
| -------- | ---------- |
| 0 – 29   | Low        |
| 30 – 59  | Medium     |
| 60 – 79  | High       |
| 80 – 100 | Critical   |

---

## Project Statistics

| Metric                       | Value       |
| ---------------------------- | ----------- |
| Customers                    | 5,000+      |
| Call Records                 | 1.4 Million |
| Analysis Period              | 3 Months    |
| Data Quality Score           | 98.8%       |
| Critical/High Risk Customers | 115         |
| Pipeline Runtime             | ~15 Minutes |

---

## Power BI Dashboard

The reporting layer consists of four interactive dashboard pages:

### Executive Overview

* Total customers
* Revenue metrics
* Fraud distribution
* Business KPIs

### Fraud Analytics

* Risk segmentation
* Fraud score distribution
* High-risk customer monitoring

### Customer Behavior

* Usage trends
* Calling patterns
* Customer segmentation

### Complaints Analysis

* Complaint categories
* Regional trends
* Customer satisfaction insights

---

## Key Achievements

* Processed over 1.4 million telecom events.
* Built a scalable Azure-based data platform.
* Achieved 98.8% data quality after cleansing.
* Developed an explainable fraud scoring framework.
* Delivered actionable business insights through Power BI.
* Enabled Customer 360 analytics for telecom operations.

---

## Future Enhancements

* Machine Learning-based fraud prediction.
* Real-time streaming analytics using Azure Event Hub.
* Automated fraud alerting workflows.
* Customer churn prediction models.
* Advanced anomaly detection.

