# 🛡️ AWS Threat Hunting and Visualization Pipeline

This project implements a comprehensive, real-time threat detection and visualization pipeline using AWS Security Hub, CloudTrail, VPC Flow Logs, and related services. Findings and logs from GuardDuty, Macie, Inspector, CloudTrail, and VPC Flow Logs are ingested, stored, cataloged, and visualized using a fully automated and serverless architecture.

---

## 📊 Architecture Overview

![Architecture Diagram](https://github.com/user-attachments/assets/756dde00-3f75-40b0-8efb-c4ff0dd6df0e)

---

## ⚙️ Workflow

1. **Log and Findings Sources**  
   - AWS GuardDuty findings via Security Hub  
   - AWS Macie findings via Security Hub  
   - AWS Inspector findings via Security Hub  
   - **AWS CloudTrail logs** stored in S3  
   - **VPC Flow Logs** stored in S3  

2. **Ingestion & Triggering**  
   - Findings sent to **AWS Security Hub** trigger EventBridge rules.  
   - CloudTrail and VPC Flow Logs are delivered continuously to designated S3 buckets.  
   - EventBridge triggers a **Lambda** function on Security Hub findings.
   - EventBridge triggers a **Lambda** function to automate Glue Crawler execution, enabling near real-time updates of data cataloging for timely   visualization in Grafana.


3. **Data Processing**  
   - Lambda function receives Security Hub findings and stores them as **raw JSON** in S3.  
   - CloudTrail and VPC Flow Logs go straight to S3 as raw files.

4. **Data Cataloging (creating a structured, searchable metadata repository)**  
   - **AWS Glue Crawlers** detect and catalog schemas for all S3 data sources, including Security Hub findings, CloudTrail logs, and VPC Flow Logs.  
   - Glue Crawler Trigger Lambda automatically starts crawlers upon new data arrival.

5. **Query Layer**  
   - **Amazon Athena** queries structured findings and logs using SQL.

6. **Visualization**  
   - **Grafana** dashboards visualize Athena query results, providing real-time findings unified insights across findings and network logs.

<img width="1475" alt="Screenshot 2025-06-23 at 19 35 28" src="https://github.com/user-attachments/assets/6ae104ac-2f6a-474f-be66-d7f35102a983" />
<img width="1485" alt="Screenshot 2025-06-23 at 19 37 18" src="https://github.com/user-attachments/assets/212f7a7f-1534-488d-96c5-837d6e25d035" />

---

## 📦 Services Used

| Service                 | Purpose                                                            |
|-------------------------|--------------------------------------------------------------------|
| AWS Security Hub        | Centralizes and aggregates GuardDuty, Macie, Inspector findings   |
| AWS CloudTrail          | Captures API activity logs stored in S3                           |
| VPC Flow Logs           | Captures network traffic logs stored in S3                        |
| Amazon EventBridge      | Triggers Lambda on new Security Hub findings                      |
| AWS Lambda              | Stores Security Hub findings as raw JSON in S3 (can be extended to parse/structure) |
| Amazon S3               | Stores findings and logs in JSON format                            |
| AWS Glue                | Crawls and catalogs S3 data for Athena                            |
| Glue Crawler Trigger Lambda | Automatically starts Glue crawlers on new data                  |
| Amazon Athena           | Executes SQL queries on findings and logs                         |
| Grafana                 | Visualizes Athena query results                                   |
| IAM Roles/Policies      | Secure access and permissions                                     |

---

## 🚀 How to Deploy

1. Enable Security Hub and integrate GuardDuty, Macie, Inspector.  
2. Configure CloudTrail to send logs to S3.  
3. Enable VPC Flow Logs to send logs to S3.  
4. Create EventBridge rule to catch new Security Hub findings.  
5. Deploy Lambda function to store Security Hub findings as raw JSON in S3.  
   *(Optionally, update Lambda to parse and structure findings for improved querying.)*  
6. Set up Glue Crawlers to discover schemas for:  
   - Security Hub findings  
   - CloudTrail logs  
   - VPC Flow Logs  
7. Configure Athena to read from the Glue Data Catalog.  
8. Connect Athena as a data source in Grafana.  
9. Import provided Grafana dashboards for unified visualization.

---

