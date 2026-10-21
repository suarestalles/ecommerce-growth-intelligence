E-commerce Growth Intelligence
Project Roadmap and Timeline

Version: 2.0
Last Updated: October 21, 2026
Status: Phase 0 — Planning

1. Project Overview

E-commerce Growth Intelligence is a data analytics platform designed to transform historical retail transaction data into actionable business insights.

The project combines data engineering, SQL, business intelligence, backend development, and frontend visualization to demonstrate an end-to-end analytical workflow.

Primary dataset: Online Retail II — UCI Machine Learning Repository

Official source: https://archive.ics.uci.edu/dataset/502/online+retail+ii

The dataset contains historical retail transactions that support sales analysis, product performance, customer purchasing behavior, geographic analysis, and transaction quality investigations.

The MVP will use a locally downloaded dataset, without requiring Google Cloud authentication or external query services.

2. Phase 0 — Planning and Project Setup

Status: IN PROGRESS

Tasks
Define the professional objectives and target audience.
Define the project concept and product vision.
Select the primary dataset.
Define the initial technology stack.
Establish the preliminary MVP scope.
Create the master project documentation.
Verify the development environment.
Create the GitHub repository.
Review the existing repository structure.
Align all documentation with the selected dataset.
Review .gitignore and .env.example.
Completion Criteria

The project objectives, dataset, technology stack, and MVP scope are documented. The development environment and repository structure are verified, and the project is ready for data exploration.

3. Phase 1 — Data Exploration

Estimated duration: Days 1–2

Tasks
Download the Online Retail II dataset from the official UCI repository.
Document the dataset source and licensing information.
Inspect the original file, worksheets, columns, and data types.
Confirm the number of records and historical coverage.
Identify missing values and duplicate records.
Investigate negative quantities and invoice cancellation patterns.
Validate product descriptions, unit prices, and invoice dates.
Identify relevant business identifiers and data relationships.
Determine the appropriate transaction and invoice granularity.
Define initial data cleaning and validation rules.
Update DATA_DICTIONARY.md.
Document the main data quality issues and analytical limitations.
Deliverables
Original dataset stored locally.
Initial data exploration results.
Updated data dictionary.
Documented data quality findings.
Initial business rules and assumptions.
Completion Criteria

The dataset structure is understood, its main data quality issues are documented, and the initial transformation rules are defined.

The final analytical model must not be established before the original data has been inspected.


### Phase 1 — Data Exploration

**Status:** In progress  
**Last reviewed:** 2026-10-21

#### Confirmed Completed Tasks

- Downloaded the original Online Retail II workbook.
- Confirmed both worksheet names and the expected eight columns.
- Verified the combined row count reported by pandas: 1,067,371.
- Inspected missing values, data types, date ranges, negative quantities, zero prices, negative prices, cancellation identifiers, and exact duplicate rows.
- Investigated negative quantities without a `C` invoice prefix.
- Identified negative-price records associated with bad-debt adjustment descriptions.
- Confirmed that the raw data path is ignored by Git.

#### Remaining Tasks

- Complete investigation of cancellation and reversal relationships.
- Determine the appropriate classification of operational adjustments.
- Investigate zero-price records.
- Decide whether any duplicate handling is justified.
- Define and document sales eligibility rules.
- Complete the data dictionary and business metrics documentation.
- Define initial data validation checks.
- Confirm the data model and ingestion approach.

#### Completion Criteria

Phase 1 is complete only when:

1. The original schema and data characteristics are documented.
2. Major quality issues have been investigated sufficiently to support explicit handling rules.
3. The initial business metrics and eligibility rules are documented.
4. Data limitations and unresolved assumptions are clearly recorded.
5. The proposed rules are ready to be implemented and tested in the next phase.

Do not mark the phase complete merely because exploratory scripts have executed successfully.


4. Phase 2 — Database and Data Pipeline

Estimated duration: Days 3–4

Tasks
Configure the PostgreSQL development environment.
Define the initial database schema.
Implement the dataset ingestion process.
Preserve the original data without modifications.
Create staging tables for imported records.
Normalize column names and data types.
Handle missing values and duplicates according to documented rules.
Investigate and classify cancellations and negative quantities.
Implement data quality validations.
Define the analytical data model and table granularity.
Create the initial analytical tables.
Implement tests for critical transformation rules.
Document the pipeline execution process.
Verify that the pipeline can be executed repeatedly.
Deliverables
Configured PostgreSQL database.
Reproducible data ingestion pipeline.
Staging tables and initial analytical tables.
Data quality validation rules.
Documented transformation logic.
Completion Criteria

The dataset can be loaded and transformed reproducibly, and the prepared data is available for analytical SQL queries.

5. Phase 3 — SQL Analytics and Business Metrics

Estimated duration: Days 5–6

Tasks
Define the business metrics in BUSINESS_METRICS.md.
Calculate the number of eligible invoices.
Calculate sales value using documented inclusion and exclusion rules.
Calculate units sold and average invoice value.
Analyze sales trends over time.
Analyze sales performance by product.
Analyze sales distribution by country.
Investigate cancelled invoices and transaction adjustments.
Analyze customer purchasing frequency.
Implement RFM customer segmentation for identifiable customers.
Validate the results against independent calculations.
Identify at least three business insights supported by the data.
Document the methodology, assumptions, and limitations of each analysis.
Deliverables
SQL queries organized in the repository.
Documented business metric definitions.
Validated analytical results.
Initial RFM customer segmentation.
At least three reproducible business insights.
Completion Criteria

The principal metrics are reproducible, their definitions are documented, and the analytical results have been validated.

Sales value must not automatically be interpreted as net revenue, profit, or accounting revenue.

6. Phase 4 — Backend Development

Estimated duration: Days 7–8

Tasks
Review the existing FastAPI application structure.
Implement or validate the health endpoint.
Define Pydantic response schemas.
Implement the executive overview endpoint.
Implement sales trend and product performance endpoints.
Implement country-level analysis endpoints.
Implement customer segmentation endpoints.
Implement cancellation analysis endpoints.
Add relevant query parameters and filters.
Integrate the API with PostgreSQL.
Implement consistent error handling.
Add unit and integration tests.
Validate the generated OpenAPI documentation.
Document local execution instructions.
Initial Endpoint Candidates
GET /health
GET /api/v1/overview
GET /api/v1/sales/trends
GET /api/v1/sales/products
GET /api/v1/sales/countries
GET /api/v1/customers/segments
GET /api/v1/invoices/cancellations
GET /api/v1/insights

The final endpoints may be adjusted according to the analytical model and actual implementation requirements.

Deliverables
Functional FastAPI application.
Documented REST endpoints.
Database integration.
Automated tests.
API documentation.
Completion Criteria

The endpoints return validated analytical results, relevant tests pass, and the API contracts are documented.

7. Phase 5 — Frontend and Dashboard

Estimated duration: Days 9–11

Tasks
Review the existing Next.js application structure.
Implement the dashboard layout.
Create KPI cards for the main business metrics.
Visualize sales trends over time.
Display product performance rankings.
Visualize sales distribution by country.
Display customer segmentation results.
Present cancellation and adjustment metrics.
Integrate the frontend with the FastAPI backend.
Implement date and other relevant filters.
Handle loading, empty, and error states.
Display business insights with supporting metrics.
Validate responsive behavior across different screen sizes.
Compare dashboard results with the corresponding API responses.
Deliverables
Functional executive dashboard.
Sales and product analysis views.
Customer intelligence view.
Cancellation analysis.
Business insights section.
Responsive frontend integrated with the backend.
Completion Criteria

The dashboard displays real results from the prepared dataset, and its metrics are consistent with the validated backend calculations.

8. Phase 6 — Quality Assurance and Deployment

Estimated duration: Days 12–14

Tasks
Review and execute the automated test suite.
Validate critical data transformation rules.
Test API and database integration.
Compare dashboard metrics against SQL results.
Configure Docker and Docker Compose.
Review environment variables and secrets management.
Verify that raw datasets and sensitive files are excluded from Git.
Update the root README.md in English.
Document installation and execution instructions.
Document the dataset source, attribution, and license.
Review the project documentation for consistency.
Capture dashboard screenshots.
Deploy the frontend and backend, where feasible.
Record a short project demonstration.
Prepare a project description for the résumé and LinkedIn profile.
Deliverables
Validated test suite.
Reproducible local development environment.
Complete English documentation.
Public GitHub repository with appropriate data exclusions.
Deployed application, if feasible.
Screenshots and project demonstration.
Completion Criteria

Another developer can understand the project, follow the documentation, run the application locally, and verify the main analytical results.

9. Phase 7 — Strategic Enhancements

Status: DEFERRED UNTIL THE MVP IS COMPLETE

Potential Enhancements
Develop cohort analysis and customer retention metrics.
Improve RFM segmentation and evaluate alternative thresholds.
Evaluate dbt for SQL transformations and data quality testing.
Explore sales forecasting with appropriate validation.
Integrate complementary marketing data when justified.
Demonstrate CAC and ROAS using suitable additional data.
Add an optional BI tool or reporting layer.
Implement AI-generated executive summaries.
Improve CI/CD automation and deployment infrastructure.
Completion Criteria

Each enhancement must address a clearly defined business or technical need and include appropriate validation and documentation.

Optional features must not delay the initial MVP.

CAC, ROAS, and conversion metrics must not be calculated as if they were directly available in the primary dataset. Any supplementary synthetic data must be explicitly labeled and kept separate from observed historical transactions.

10. Timeline and Project Management

The proposed timeline is an estimate based on approximately two weeks of focused work.

Actual durations may change depending on data quality issues, implementation complexity, testing requirements, and deployment constraints.

The project prioritizes data quality, reproducibility, and reliable business metrics over meeting arbitrary deadlines.

If a phase requires additional time, update its status and estimated duration rather than compromising implementation quality.

Tasks should only be marked as complete when implementation and relevant validation have been performed.

11. Definition of Done

A task is considered complete only when:

The implementation is finished.
Relevant tests have been executed.
Results have been validated.
Required documentation has been updated.
Known limitations have been documented.

Suggested code or proposed changes do not constitute completed work until they have been implemented and verified in the project environment.

12. Progress Tracking

At the end of each development session, record:

Date.
Phase and objective.
Files created or modified.
Technical decisions made.
Commands executed.
Tests performed and results.
Problems encountered.
Remaining tasks.
Recommended next action.

Update this roadmap when the scope, architecture, implementation status, or timeline changes.

Only confirmed progress should be recorded as completed.

13. Next Action

Immediate priority: Complete Phase 0 and begin Phase 1.

The next concrete steps are to verify the repository structure, obtain the Online Retail II dataset, inspect its actual schema and data quality, and update the data dictionary before defining the final analytical model.