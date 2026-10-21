E-commerce Growth Intelligence
System Architecture

Version: 1.1
Last Updated: October 21, 2026
Status: Proposed — implementation pending verification

1. Architecture Overview

The application follows a modular monolithic architecture organized into four main technical components:

Data processing pipeline.
PostgreSQL analytical database.
FastAPI backend.
Next.js frontend.

Each component has a clearly defined responsibility. The frontend communicates with the backend through HTTP, while the backend retrieves analytical results from PostgreSQL.

The initial implementation does not require microservices, distributed infrastructure, or cloud-specific authentication.

2. High-Level Data Flow
Online Retail II Dataset
          |
          v
Python Ingestion Pipeline
          |
          v
Data Validation and Transformation
          |
          v
PostgreSQL Staging Layer
          |
          v
SQL Analytical Models
          |
          v
FastAPI REST API
          |
          v
Next.js Dashboard


The pipeline will be designed to process a locally downloaded copy of the dataset.

The original source data should remain unchanged. Cleaning, normalization, and analytical transformations must produce derived data that can be regenerated from the source.

The final pipeline structure and analytical models will be defined after inspecting the source file.

3. Technology Stack
Component	Technology	Responsibility
Data processing	Python, pandas	Ingestion, validation, cleaning, and transformation
Analytical queries	SQL	Aggregation, business rules, and analytical models
Database	PostgreSQL	Persistent storage and analytical queries
Backend	FastAPI, Pydantic	API endpoints, input validation, and response schemas
Database access	SQLAlchemy, if appropriate	Database connectivity and query execution
Frontend	Next.js, TypeScript	Dashboard interface and user interaction
Visualization	Recharts or equivalent	Charts and data visualization
Testing	pytest	Automated tests for Python logic and API behavior
Environment	Docker, Docker Compose	Reproducible local execution, if implemented

The table describes the intended stack, not proof that each component has already been configured.

4. Component Responsibilities
4.1. Data Processing Pipeline

The Python pipeline is responsible for:

Reading the original dataset.
Validating the source schema.
Normalizing column names and data types.
Identifying missing values and duplicate records.
Investigating cancellation-related transactions and negative quantities.
Applying documented transformation rules.
Loading validated records into PostgreSQL.
Running data quality checks.

The pipeline must preserve valid transactions and avoid silently discarding records whose business meaning has not been established.

4.2. PostgreSQL Database

PostgreSQL is the persistent storage and analytical query layer.

The proposed organization separates:

Staging: imported and normalized source records.
Analytical models: tables or views prepared for business analysis.

The final schema and table grain must be established after source inspection.

Database credentials must remain on the server side and must never be exposed to frontend code.

4.3. FastAPI Backend

The backend provides a REST interface between the database and the frontend.

Its responsibilities include:

Exposing analytical results through versioned endpoints.
Validating query parameters.
Defining response schemas with Pydantic.
Executing database queries through an appropriate data access layer.
Applying consistent error handling.
Providing API documentation through OpenAPI.
Testing business logic and endpoint behavior.

Business metric definitions must remain consistent across endpoints. Calculations should use shared analytical queries or reusable business logic rather than duplicated formulas.

4.4. Next.js Frontend

The frontend provides the dashboard interface.

Its responsibilities include:

Displaying KPIs and charts.
Providing supported date, product, and geographic filters.
Consuming the FastAPI endpoints.
Showing loading, empty, and error states.
Displaying metric definitions and reporting periods where relevant.
Adapting the interface to different screen sizes.

The frontend should present values returned by the API rather than independently reimplementing core business calculations.

5. Proposed Data Model

The following structures are candidates, not confirmed database tables.

Table or View	Intended Grain	Purpose
stg_online_retail	Source transaction line	Store imported and normalized records
fact_sales	Validated transaction line	Support sales and quantity analysis
fact_invoices	Invoice	Support invoice-level metrics and aggregates
dim_products	Product identifier	Support product-level analysis
dim_customers	Identifiable customer	Support customer-level analysis
dim_country	Country	Support geographic analysis
dim_date	Calendar date	Support time-based analysis
customer_rfm	Identifiable customer and analysis reference date	Support RFM metrics and segment assignments

Not every proposed table needs to be implemented.

The final model must be based on the source data, actual analytical requirements, and documented business definitions.

Data Grain and Aggregation

The source dataset is expected to contain multiple transaction lines for some invoices.

Therefore:

Invoice counts must use distinct eligible invoice identifiers.
Quantity metrics must aggregate the appropriate transaction lines.
Invoice-level values must be calculated after grouping records at invoice level.
Joins must not multiply transaction values.
Customer metrics must use a documented population and observation period.

The treatment of cancellations, returns, and negative quantities must be defined in BUSINESS_METRICS.md before the corresponding metrics are finalized.

6. Proposed API Interface

The following endpoints are initial candidates.

Endpoint	Purpose
GET /health	Check application availability
GET /api/v1/overview	Return executive KPIs
GET /api/v1/sales/trends	Return sales trends over time
GET /api/v1/sales/products	Return product performance
GET /api/v1/sales/countries	Return geographic sales metrics
GET /api/v1/customers/segments	Return RFM segment results
GET /api/v1/invoices/cancellations	Return cancellation-related metrics
GET /api/v1/insights	Return data-supported business insights

The final endpoint list, response schemas, and available filters will depend on the implemented analytical models.

These endpoints must not be considered implemented until their existence and behavior have been verified.

7. Configuration and Environment

Application configuration should be managed through environment variables.

The .env.example file should document required variable names and safe example values.

The actual .env file must not be committed to version control.

The local development environment should support:

PostgreSQL connectivity.
Backend database configuration.
Frontend API configuration.
Repeatable application startup.

Docker Compose may be used to coordinate the database, backend, and frontend.

The initial data workflow must not depend on Google Cloud authentication.

8. Testing and Quality Controls

Testing should cover the following technical areas.

Data Pipeline
Source schema validation.
Data type conversions.
Missing-value handling.
Cancellation and adjustment rules.
Transformation repeatability.
Aggregation correctness.
Analytical Models
Invoice-level calculations.
Quantity and monetary-value calculations.
Duplicate handling.
Join cardinality.
Consistency of business definitions.
RFM calculation rules.
Backend
Response schemas.
Query parameter validation.
Filtering behavior.
Database integration.
Error handling.
Metric correctness.
Frontend
API integration.
Loading and error states.
Filter behavior.
Displayed values against API responses.
Responsive behavior.

Only tests that have actually been executed should be reported as passing.

9. Security and Data Management
Keep database credentials and secrets out of version control.
Do not expose database connections to the browser.
Validate API inputs.
Avoid returning unnecessary source-level records through public endpoints.
Exclude large datasets and generated artifacts from Git when appropriate.
Document the dataset source and comply with its applicable license.
Preserve the original dataset and make transformation rules reproducible.
10. Related Documentation
Document	Responsibility
PROJECT_BRIEF.md	Product vision, scope, and technology choices
ROADMAP.md	Development phases and completion criteria
DATA_DICTIONARY.md	Source fields, data types, and data quality
BUSINESS_METRICS.md	KPI definitions and calculation rules
SESSION_LOG.md	Development history
DECISIONS.md	Significant technical decisions, when needed

This document describes component responsibilities and proposed technical interfaces. It does not replace the detailed business definitions or the development roadmap.

11. Implementation Status

The architecture described here is a proposal based on the current project plan.

The following items require verification:

Dataset download and inspection.
PostgreSQL configuration.
Ingestion pipeline implementation.
Final analytical schema.
SQL model implementation.
FastAPI endpoint implementation.
Frontend integration.
Automated test execution.
Deployment configuration.

Architecture changes should be documented when they materially affect component responsibilities, data models, interfaces, or security.


### Data Processing Boundaries

The proposed data workflow separates three responsibilities:

1. **Raw source:** Preserve the original workbook without modifications.
2. **Staging:** Load and normalize source records while retaining traceability to the original data and source worksheet.
3. **Analytical layer:** Apply documented classifications and eligibility rules to support business metrics.

Cancellation candidates, returns, operational adjustments, and exact duplicate rows must not be silently discarded during ingestion.

The analytical model must define the grain of each table and ensure that joins do not multiply quantities or monetary values.

The final table design and transformation rules remain pending until the data quality investigation and business metric definitions are sufficiently complete.
