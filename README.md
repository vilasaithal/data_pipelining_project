# data_pipelining_project

# Scalable ETL Data Pipeline on AWS

## Overview

- **Description**: An end-to-end ETL data pipeline using AWS services to process, transform, and store data in a structured, queryable format.
- **Goal**: Efficiently process multiple datasets, enable querying for analytics, and store data in a cost-effective format.

## Architecture

1. **Data Sources**: Three raw datasets stored on Amazon S3.
2. **ETL Process**:
   - AWS Glue and Apache Spark for data transformation (cleaning, joining, filtering).
   - Transformation logic and scripts are managed in Spark, orchestrated via AWS Glue jobs.
3. **Data Storage**: Final dataset saved in Amazon S3 in Parquet format to optimize storage and performance.
4. **Querying**: AWS Athena configured for on-demand SQL queries on the Parquet data.

## Setup and Prerequisites

- **AWS Services Needed**: S3, Glue, Athena.
- **Data Format**: Ensure data in S3 is accessible and properly formatted for Glue ETL processing.
- **IAM Permissions**: Ensure proper permissions for Glue, S3, and Athena.

## Project Steps

1. **Upload Data**: Upload initial datasets to a designated S3 bucket.
2. **Configure Glue Jobs**:
   - Define Glue crawlers to catalog data.
   - Set up Glue jobs to perform Spark-based transformations.
3. **Store Output**: Store ETL results in a dedicated S3 bucket in Parquet format.
4. **Query with Athena**: Set up Athena for querying; configure queries for analytics.

## Usage

- **Running the ETL**: Trigger the Glue jobs through the AWS Console or by using the AWS CLI.
  ```bash
  aws glue start-job-run --job-name your-glue-job-name
  ```
- **Running Queries**: Use Athena to run SQL queries. Here’s an example query:
  ```sql
  SELECT * FROM your_table_name LIMIT 10;
  ```

## Technologies Used

- **AWS Glue** for ETL orchestration and Spark jobs.
- **Apache Spark** for data processing.
- **Amazon S3** for data storage.
- **AWS Athena** for querying and analytics.

## Future Improvements

- Integration with AWS QuickSight for data visualization.
