E-commerce Growth Intelligence
Project Master Document — Context, Architecture, and Roadmap

Version: 2.0
Last Updated: October 21, 2026
Status: Initial planning — dataset selected; implementation to be confirmed.

Objective: Build a professional portfolio project demonstrating skills in software development, data engineering, data analytics, business intelligence, e-commerce, and analytics engineering.

1. PROJECT CONTEXT
Professional Background

The developer responsible for this project has:

A bachelor's-level degree in Systems Analysis and Development from Brazil.
A postgraduate qualification in Artificial Intelligence.
Approximately five years of professional software development experience.
Primary experience with Python and FastAPI.
Experience with Flutter.
Additional experience with Next.js and Node.js.
Current residence in Spain.
Plans to begin a Master's program in Marketing and E-commerce in Madrid in early 2027.
Career Objectives

Secure a professional opportunity in Spain or another European market, leveraging existing software development experience while expanding into fields such as:

Data Analytics.
Analytics Engineering.
Business Intelligence.
Data Engineering.
Marketing Analytics.
E-commerce Analytics.
Marketing Technology (MarTech).
Data and AI solution development.

The project should demonstrate the ability to solve practical data problems, build reproducible solutions, and communicate findings to both technical and business audiences.

The goal is not to position the developer as a beginner in technology, but to demonstrate a deliberate expansion of existing professional expertise into the data domain.

Strategy

Build a functional application integrating software development, data processing, SQL, analytical modeling, dashboards, and business analysis.

The priority is to deliver a simple, well-documented, publicly accessible, and technically sound MVP while avoiding unnecessary features.

The project should demonstrate a complete workflow:

Raw Data → Ingestion → Validation and Transformation → Analytical Modeling → Metrics → API → Dashboard → Business Insights.

2. PRODUCT VISION
Product Name

E-commerce Growth Intelligence

Description

An e-commerce analytics platform that transforms transactional data into metrics, analyses, and recommendations to improve commercial performance and understand customer purchasing behavior.

The application simulates a decision-support tool used by e-commerce, BI, and commercial management teams.

Business Problem

E-commerce businesses accumulate large volumes of transaction data but need to transform them into actionable information to answer questions such as:

How are sales evolving over time?
Which products and categories generate the highest sales value?
What is the average invoice value?
Which geographic markets account for the largest share of sales?
Which customers demonstrate higher purchase frequency and monetary value?
Which customers have not purchased recently?
What proportion of transactions involve cancellations?
Are there observable patterns in seasonality, revenue concentration, or purchasing behavior?
What commercial opportunities can be identified from historical data?

The project must answer questions supported by the available data and explicitly identify situations where the data is insufficient to support a conclusion.

Target Audience
Technology and data recruiters.
E-commerce companies.
Retailers and distributors.
Marketplaces.
SaaS companies.
Data consultancies.
BI, CRM, and commercial management teams.
Differentiation

The project will not be merely a collection of charts. It must demonstrate a complete analytical workflow with documented business rules, reproducible transformations, automated tests, and verifiable results.

Recommendations must be derived from actual analyses rather than invented findings or correlations presented as proof of causation.

3. MVP SCOPE
3.1. Executive Dashboard

Display metrics such as:

Gross merchandise sales value, according to the adopted definition.
Number of eligible invoices and orders.
Number of units sold.
Average invoice value.
Monthly sales trends.
Sales value by product.
Sales distribution by country.
Cancellation metrics.
Number of identifiable customers.
Customer distribution by purchase frequency and monetary value.

Metrics must use consistent filters and eligibility criteria. The interface must distinguish indicators calculated from complete data from those affected by missing records or dataset limitations.

3.2. Product and Sales Analytics

Enable users to identify:

Products generating the highest sales value.
Products with the highest quantities sold.
Products appearing most frequently in invoices.
Monthly sales trends.
Transaction value distributions.
Country-level sales contributions.
Revenue concentration across products and customers.
Observable seasonal patterns within the historical period.

Definitions for sales value, invoices, units, and average invoice value must be documented.

The dataset contains retail transactions, including wholesale activity. Results must not assume that every invoice represents a typical individual consumer purchase.

3.3. Customer Intelligence

Implement customer segmentation using RFM analysis when sufficient customer identifiers are available.

Recency: Time since the customer's most recent purchase.
Frequency: Number of eligible purchase invoices within the defined period.
Monetary: Monetary value of the customer's eligible purchases.

Create interpretable segments such as recent customers, repeat customers, high-value customers, and potentially inactive customers.

Calculation rules, segment thresholds, and the reference date must be documented.

Customer identifiers may be missing from some records. These records must be handled explicitly rather than grouped together as if they belonged to the same customer.

RFM segmentation will be treated as a descriptive, heuristic method rather than a validated predictive model.

3.4. Cancellations and Commercial Data Quality

Investigate cancelled invoices and other inconsistencies identified in the available fields.

The analysis must consider:

Identification of invoices associated with cancellations.
Negative quantities and potential returns.
Missing, null, or invalid unit prices.
Invoices without customer identifiers.
Duplicate and inconsistent records.
Differences between gross values, adjustments, and eligible sales metrics.

Rules for excluding, retaining, or classifying records must be documented and tested.

Negative quantities must not automatically be treated as complete cancellations without validating the meaning of the corresponding records.

3.5. Business Insights

Create an analytical section explaining:

What was observed.
Which metric supports the finding.
Which period was analyzed.
Which rules and filters were applied.
What limitations affect the conclusion.
Which business action could be tested.

Recommendations must be reproducible and consistent with the available data.

Optional Features

Implement only after the MVP is functional:

Cohort and retention analysis.
Sales forecasting.
Revenue concentration analysis.
Additional customer segmentation.
An optional BI layer using external tools.
An AI assistant for executive summaries.
Additional datasets for marketing analytics.
Business hypothesis testing or experimentation.

CAC, ROAS, and visitor-to-buyer conversion are outside the initial scope because they require acquisition, advertising spend, traffic, or attribution data that the primary dataset does not directly provide.

These features may only be implemented using suitable additional data sources or clearly labeled synthetic data.

4. DATA SOURCE
Primary Dataset

Online Retail II — UCI Machine Learning Repository

Official page:

https://archive.ics.uci.edu/dataset/502/online+retail+ii

Original file provided by the repository: online_retail_II.xlsx.

General Characteristics

The dataset contains approximately 1.07 million transaction records from a UK-based retailer, covering the period from December 1, 2009, to December 9, 2011.

The main fields include:

Invoice: Invoice identifier.
StockCode: Product identifier.
Description: Product description.
Quantity: Number of units.
InvoiceDate: Transaction date and time.
Price: Unit price.
Customer ID: Customer identifier.
Country: Country associated with the transaction.

The file contains records requiring data preparation, including missing values, negative quantities, and invoice identifiers that may indicate cancellations.

The actual schema and data characteristics must be verified during the data exploration phase.

Rationale for Selection

The dataset supports analysis of:

Sales and sales value.
Products and quantities.
Transaction history.
Customers and repeat purchasing.
Geographic distribution.
Temporal patterns.
Cancellations and commercial data inconsistencies.
Analytical modeling and RFM segmentation.

It provides opportunities to demonstrate Python, pandas, SQL, PostgreSQL, dimensional modeling, data quality practices, and analytical visualization.

The selection also differentiates this project from another project that uses the Brazilian E-Commerce Public Dataset by Olist.

License and Attribution

The UCI repository identifies the dataset under the CC BY 4.0 license.

Project documentation must preserve attribution to the original source and include the official dataset URL.

Before redistributing the data, the applicable terms must be reviewed in the context of the intended distribution method.

Data Handling Principles
Preserve the original file without modifications.
Document the source, period, and license.
Do not assume that every record represents an independent order.
Do not assume that every invoice represents a consumer purchase.
Identify cancelled invoices using documented rules.
Handle negative quantities and other adjustments carefully.
Document missing values, duplicates, and inconsistencies.
Do not confuse gross merchandise sales value with net revenue or profit.
Do not assume that the dataset contains costs, margins, operating expenses, or marketing spend.
Do not present historical findings as current market benchmarks.
Do not publish raw data on GitHub without an explicit and justified decision.
Local Data Storage

The dataset must be downloaded and processed locally.

The application must not depend on Google Cloud authentication, external query services, or cloud credentials to run the MVP.

The ingestion process must be reproducible from the original file using instructions documented in the repository.

5. TECHNOLOGY STACK
Backend
Python.
FastAPI.
Pydantic.
SQLAlchemy, if appropriate for the implementation.
pytest.

Responsibilities:

Expose metrics through REST endpoints.
Validate parameters and filters.
Centralize business logic that needs to be shared.
Query the analytical layer.
Document the API using OpenAPI.
Provide consistent responses and error messages.
Database

PostgreSQL.

Responsibilities:

Store prepared data.
Provide analytical tables.
Execute SQL queries.
Support dashboard metrics.
Enable validation of result consistency.
Data Processing
Python.
pandas.
SQL.

Responsibilities:

Read the original file.
Validate the schema and field types.
Handle dates, missing values, and duplicates.
Classify cancellations and adjustments using documented rules.
Produce staging tables.
Build reproducible analytical tables.
Record relevant execution results and errors.
Frontend
Next.js.
TypeScript.
A charting library such as Recharts.
A consistent styling solution such as Tailwind CSS.

Responsibilities:

Present the dashboard.
Implement filters.
Consume the FastAPI.
Display metrics, charts, and insights.
Provide a responsive interface.
Handle loading states, empty results, and errors.
Infrastructure and Quality
Git and GitHub.
Docker and Docker Compose.
pytest.
Integration tests.
Environment variables.
CI with GitHub Actions, where feasible.
Public deployment of the frontend and backend.
Scope Decisions
Do not use Flutter in the first version.
Do not introduce an additional Node.js backend.
Do not implement microservices.
Do not add authentication without a concrete need.
Do not introduce Airflow, Kafka, or distributed infrastructure in the MVP.
Do not add AI before validating the metrics and data quality.
Do not introduce additional transformation tools without a demonstrated need.
Do not create architectural layers without clear responsibilities.

The goal is to demonstrate technical competence and sound engineering judgment, not to accumulate technologies for a résumé.

6. PROPOSED ARCHITECTURE
Main Workflow
The original file is obtained from the UCI Machine Learning Repository.
A Python pipeline reads and validates the data.
Prepared data is loaded into PostgreSQL.
The analytical layer provides tables and queries for metrics.
The FastAPI backend exposes metrics through REST endpoints.
The Next.js frontend queries the API.
Users apply filters and explore the results.
The insights section presents data-driven interpretations.

The first version will use a simple architecture consisting of one backend, one frontend, and one PostgreSQL database.

Implementation must respect the existing repository structure. New modules should only be created when there is a concrete responsibility to implement.

Data Modeling

The final data model must be defined after inspecting the original file and formalizing the business rules.

A candidate structure includes:

stg_online_retail: Imported data normalized for preparation.
fact_sales: Eligible sales records, preserving the documented grain.
fact_invoices: Invoice-level aggregated metrics, if needed.
dim_products: Product information.
dim_customers: Information about identifiable customers.
dim_country: Available geographic information.
dim_date: Analytical calendar.
customer_rfm: Customer metrics and segments calculated for a reference date.

These tables are proposals, not implemented structures.

The data model must explicitly define the grain of each table and prevent joins from multiplying quantities or monetary values.

Records without customer identifiers may contribute to certain sales analyses but must not be treated as identifiable customers in repeat-purchase analyses.

Raw and Processed Data

The data structure must clearly separate original files from derived artifacts:

data/raw/: Original source file.
data/processed/: Prepared data, where necessary.

Final directory names must be aligned with the actual repository structure before existing files are moved.

Large raw datasets and processed artifacts must not be committed to Git without explicit justification.

7. REPOSITORY STRUCTURE

The repository already has an initial monorepo structure containing the backend, frontend, data, documentation, scripts, and SQL directories.

Organization must evolve from the existing directories:

docs/: Project documentation.
data/: Raw and processed data.
scripts/: Ingestion and execution scripts.
sql/: Staging queries, analytical models, and analyses.
backend/: FastAPI application and tests.
frontend/: Next.js application.
.env.example: Example configuration.
.gitignore: Exclusion of data, secrets, and generated files.
README.md: Project overview and setup instructions.

The detailed structure must be confirmed against the actual repository files.

Do not create empty directories, duplicate data structures, or reorganize modules without a technical need.

8. PROPOSED API ENDPOINTS

The API may initially include the following endpoints:

GET /health

Checks whether the service is operational.

GET /api/v1/overview

Returns the main KPIs.

GET /api/v1/sales/trends

Returns sales trends over time.

GET /api/v1/sales/products

Returns product-level metrics.

GET /api/v1/sales/countries

Returns country-level metrics.

GET /api/v1/customers/segments

Returns the distribution of customers across RFM segments.

GET /api/v1/invoices/cancellations

Returns cancellation and adjustment metrics according to the defined rules.

GET /api/v1/insights

Returns insights derived from the analyses.

Filters may include dates, products, countries, and other relevant fields.

These endpoints are initial candidates and may be adjusted during development.

Responses must have documented contracts, defined types, and automated tests.

9. BUSINESS METRICS AND DEFINITIONS

The BUSINESS_METRICS.md document must record the exact definition of each metric.

Sales and Sales Value

Gross merchandise sales value: The sum of values calculated from quantity multiplied by unit price for eligible records, according to the documented rules.

Number of invoices: The distinct count of eligible invoices, with cancellations handled explicitly.

Units sold: The sum of quantities for eligible sales records, according to the adopted policy for adjustments and returns.

Average invoice value: Eligible gross merchandise sales value divided by the number of eligible invoices, using the same record population.

Sales by period: Aggregation of sales by transaction date, using consistent calendar rules and filters.

The project must not automatically label these metrics as net revenue, accounting revenue, or profit, because the dataset does not contain all the components needed to calculate those measures.

Customer Metrics

Recency: The difference between the reference date and the customer's most recent eligible purchase date.

Frequency: The number of eligible purchase invoices for a customer within the defined period.

Monetary: The cumulative monetary value of a customer's eligible purchases, according to the adopted definition.

Repeat-purchase rate: The proportion of identifiable customers with at least two eligible purchases, using an explicitly defined population and observation window.

Customer segmentation must include only identifiable customers and document the reference date.

Cancellations and Adjustments

Cancellation identification must use fields and patterns found in the original file, including invoice identifiers.

Negative quantities and cancellation-related records must be investigated before any automatic exclusion or classification.

Adopted rules must be documented, reproducible, and tested.

Metrics Not Directly Available

CAC: Requires acquisition spend and consistent identification of customers attributed to that spend.

ROAS: Requires advertising spend and revenue attributed to advertising according to a defined attribution rule.

Visitor-to-buyer conversion: Requires visitor or session data and purchases linked consistently.

Predictive LTV: Requires a validated forecasting methodology and suitable data. Historical customer spend must not be presented as a predictive LTV estimate.

These metrics must not be invented or inferred from fields that do not support their definitions.

10. ROADMAP AND TIMELINE

The following estimates must be updated according to actual progress.

Phase 0 — Planning

Status: Initial planning; completion to be confirmed.

Define the career objective.
Define the product concept.
Select the dataset.
Define the technology stack.
Establish the preliminary scope.
Create the initial documentation.
Confirm the development environment.
Prepare the GitHub repository.

Completion criteria: Initial scope and decisions documented, with the environment and repository verified.

Phase 1 — Data Exploration

Estimated duration: Days 1–2.

Download the original file.
Inspect the schema, fields, and data types.
Confirm the historical period and record count.
Identify missing values and duplicates.
Investigate cancelled invoices and negative quantities.
Define initial business rules.
Update the data dictionary.
Document limitations.

Completion criteria: Data structure understood, major data quality issues identified, and initial rules documented.

Phase 2 — Database and Pipeline

Estimated duration: Days 3–4.

Configure PostgreSQL.
Implement data loading.
Create the required transformations.
Define the analytical model.
Implement validations.
Add tests for critical business rules.
Document metrics.

Completion criteria: Reproducible pipeline and prepared data available for SQL queries.

Phase 3 — SQL Analytics

Estimated duration: Days 5–6.

Sales and invoice queries.
Time-series analysis.
Product performance.
Geographic analysis.
RFM segmentation.
Cancellation and adjustment analysis.
Identify at least three data-supported business insights.

Completion criteria: Reproducible metrics, validated results, and documented analyses.

Phase 4 — Backend

Estimated duration: Days 7–8.

Implement the FastAPI application.
Create endpoints.
Define response schemas.
Implement filters.
Add tests.
Document the API.

Completion criteria: Functional, documented, and tested endpoints.

Phase 5 — Frontend and Dashboard

Estimated duration: Days 9–11.

Build the dashboard layout.
Implement KPI cards.
Create charts.
Connect the frontend to the API.
Implement filters.
Handle loading states and errors.
Validate the experience across different devices.

Completion criteria: Functional dashboard using prepared dataset records.

Phase 6 — Quality and Deployment

Estimated duration: Days 12–14.

Review tests.
Configure Docker Compose.
Review environment variables.
Review the documentation in English.
Create screenshots.
Deploy the frontend and backend.
Record a short demonstration.
Add the project to the résumé and LinkedIn profile.

Completion criteria: Another person can understand the project, run its components by following the instructions, and try the deployed application.

Phase 7 — Strategic Enhancements

Execute after the MVP.

Add cohort and retention analysis.
Evaluate dbt for transformation and SQL testing.
Explore forecasting models when sufficient data and validation are available.
Integrate complementary marketing data if there is a concrete need.
Add AI-generated summaries.
Improve infrastructure according to actual requirements.
Timeline Notes

The goal is to deliver an MVP in approximately two focused weeks of work without compromising metric quality or clarity of business rules.

If a phase requires more time, update its status and estimated duration instead of marking incomplete tasks as finished.

11. DEVELOPMENT STANDARDS
Implement one stage at a time.
Prioritize small, functional deliverables.
Explain relevant architectural decisions.
Do not create features before validating their need.
Write tests for important business rules.
Do not invent data, results, or benchmarks.
Never publish credentials or secrets.
Keep the README up to date.
Use clear names for variables, functions, tables, and endpoints.
Write the final project documentation in English to target international recruiters.
Keep planning and development explanations in Portuguese unless requested otherwise.
Update this document when the scope, architecture, or status changes significantly.
Do not mark a task as complete without evidence of implementation and validation.
Definition of Done

A task is complete only when:

The implementation is finished.
Relevant tests pass.
Results have been validated.
Required documentation has been updated.

If a step has not been executed in the actual environment, it must remain pending, even if code has been suggested or written in a conversation.

12. PROGRESS TRACKING ACROSS CONVERSATIONS

This document is the primary source of project context.

When starting a new conversation, the developer should provide this document and, where possible, the current repository state, relevant files, and the latest test results.

The assistant must:

Read this document before suggesting changes.
Identify the latest completed phase.
Review pending tasks.
Consider only tasks with evidence of completion.
Propose the next concrete task.
Avoid repeating completed steps.
Respect existing technologies and decisions.
Suggest updates to the master document when necessary.
Update the timeline only with confirmed information.
Never claim that commands were executed or tests passed without evidence.
Prefer small, verifiable changes.

At the end of each development session, record:

Date.
Session objective.
Files created or modified.
Technical decisions made.
Commands executed.
Tests performed and results.
Issues encountered.
Recommended next task.
13. CURRENT PROJECT STATUS

Last documentation update: October 21, 2026.

Current phase: Planning and documentation alignment.

Selected dataset: Online Retail II — UCI Machine Learning Repository.

Dataset download and inspection: Not yet confirmed.

GitHub repository: An initial structure has been described; the current state of files must be verified.

Development environment: Initial structure described; complete configuration to be confirmed.

Database: Not configured or not yet confirmed.

Ingestion pipeline: Not implemented or not yet confirmed.

Backend: Initial FastAPI structure described; functionality to be confirmed.

Frontend: Initial Next.js structure described; functionality to be confirmed.

Deployment: Not started or not yet confirmed.

Recommended next action: Complete documentation alignment with Online Retail II, download and inspect the original file, and define data quality rules before implementing the pipeline.


### Current Status — 2026-10-21

**Current phase:** Phase 1 — Data Exploration.

**Dataset:** Online Retail II, UCI Machine Learning Repository.

**Confirmed progress:**

- Original workbook downloaded and read successfully.
- Both worksheets and the expected schema verified.
- Initial profiling and data quality investigation scripts executed.
- Missing customer identifiers, duplicate groups, negative quantities, cancellation identifiers, zero prices, and financial adjustment candidates identified.
- Raw dataset exclusion from Git verified.

**Not yet confirmed as complete:**

- Final business rules for sales eligibility.
- Final cancellation and adjustment classification.
- Deduplication policy.
- Production ingestion pipeline.
- PostgreSQL schema and analytical model.
- Automated validation suite.
- Backend, frontend, and deployment.

**Immediate next action:** Finish investigating cancellation relationships and operational adjustments, then formalize the initial business metrics and data quality rules before implementing the ingestion pipeline.


14. INSTRUCTIONS FOR CONTINUING THE PROJECT IN A NEW CHAT

We are developing E-commerce Growth Intelligence, a professional portfolio project demonstrating skills in Python, FastAPI, SQL, PostgreSQL, Next.js, data analytics, BI, e-commerce, and analytics engineering.

The selected primary dataset is Online Retail II, provided by the UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/502/online+retail+ii

Read this document in full and use it as the primary source of project context.

Before proposing any implementation:

Identify the current phase in Section 13.
Review the roadmap in Section 10.
Consider only tasks confirmed as completed.
Propose the next task incrementally.
Explain the objective, affected files, and validation criteria.
When providing code, include executable instructions and explain how to verify the results.
At the end of the session, summarize progress and identify any required changes to this document.

Do not restart the project from scratch. Do not assume that files, databases, environments, or services have been created unless documented.

The dataset must be processed locally, without requiring Google Cloud authentication for the MVP.

Immediate objective: Complete documentation alignment and begin data exploration, validating the actual file structure before finalizing the ingestion pipeline and analytical model.