E-commerce Growth Intelligence
Data Dictionary

Version: 1.1
Last Updated: October 21, 2026
Status: Initial documentation — source validation pending

1. Dataset Information
Attribute	Description
Dataset name	Online Retail II
Publisher	UCI Machine Learning Repository
Source URL	https://archive.ics.uci.edu/dataset/502/online+retail+ii
Original format	Excel workbook
Expected filename	online_retail_II.xlsx
Data domain	Historical retail transactions
Primary analytical use	Sales, product, geographic, and customer purchasing analysis
License	CC BY 4.0, according to the UCI dataset record

The dataset contains historical transaction records from a UK-based online retailer.

The published dataset covers the period from December 1, 2009, through December 9, 2011, and contains approximately 1.07 million transaction-line records.

These figures describe the published dataset. The actual file, worksheets, row counts, and date range must be inspected before they are recorded as validated project results.

2. Source Structure

The original workbook is expected to contain two worksheets covering different historical periods.

The expected source fields are:

Invoice
StockCode
Description
Quantity
InvoiceDate
Price
Customer ID
Country

The actual worksheet names, column types, null counts, and schema consistency remain to be verified.

The source must be inspected before defining primary keys, relationships, or final analytical tables.

3. Source Field Definitions
Source field	Expected type	Business meaning	Validation requirements
Invoice	String	Invoice identifier	Investigate missing identifiers and cancellation-related prefixes
StockCode	String	Product or stock identifier	Preserve identifier formatting and investigate inconsistent values
Description	String	Product description	Inspect missing values and inconsistent descriptions
Quantity	Integer	Quantity recorded on a transaction line	Investigate negative, zero, and unusually large values
InvoiceDate	Datetime	Invoice-associated date and time	Validate parsing, date range, and missing values
Price	Decimal	Unit price recorded for a transaction line	Investigate negative, zero, and missing values
Customer ID	Nullable identifier	Customer identifier, when available	Measure missingness and preserve identifier semantics
Country	String	Country associated with the transaction	Investigate missing values and naming inconsistencies

The types above are expected types, not the results of an executed schema inspection.

Identifiers should be handled as identifiers rather than numerical measures. In particular, Invoice, StockCode, and Customer ID should not be used for arithmetic calculations.

4. Proposed Normalized Column Names

The following naming conventions may be used in staging and analytical tables.

Source field	Proposed normalized name
Invoice	invoice_id
StockCode	stock_code
Description	description
Quantity	quantity
InvoiceDate	invoice_date
Price	unit_price
Customer ID	customer_id
Country	country

Normalization must preserve the original meaning and identifier values.

The mapping between the original source columns and the normalized columns must remain documented and reproducible.

5. Transaction Grain and Relationships

The source is expected to represent individual transaction lines rather than one row per invoice.

An invoice may contain multiple products and therefore multiple source records.

Consequently:

A source row must not automatically be interpreted as an invoice.
An invoice identifier must not automatically be assumed to be unique across source rows.
A stock code may appear across multiple invoices.
A customer may be associated with multiple invoices.
Customer-level analysis is limited when the customer identifier is missing.

The final grain and candidate keys of each analytical table must be established after source inspection.

No primary key or foreign key should be declared solely on the basis of the field names.

6. Data Quality Assessment

The following checks must be performed during data exploration.

6.1. Schema and Data Types
Confirm the actual worksheet names.
Compare the columns across worksheets.
Validate source data types.
Confirm that invoice dates can be parsed.
Verify that identifiers retain their original formatting.
Record row counts for each worksheet and for the combined dataset.
6.2. Missing Values
Calculate missing-value counts by column.
Calculate the percentage of records without customer identifiers.
Investigate missing invoice identifiers.
Investigate missing invoice dates.
Investigate missing product descriptions and prices.
Define field-specific handling rules.

Missing values must not trigger automatic deletion of entire records without evaluating the effect on the relevant analysis.

6.3. Duplicate Records
Identify exact duplicate rows.
Investigate repeated invoice and stock-code combinations.
Determine whether repeated records represent legitimate transaction lines.
Document the criteria for removing confirmed duplicates, if applicable.

Repeated values in selected columns do not, by themselves, establish that a record is a duplicate.

6.4. Quantities and Prices
Count records with negative quantities.
Count records with zero quantities.
Count records with negative prices.
Count records with zero prices.
Investigate unusually large quantities or prices.
Examine cancellation-related invoice identifiers.
Determine how returns and adjustments should be represented in analytical metrics.

Negative quantities and prices must not be discarded automatically. Their meaning must be investigated first.

6.5. Temporal Consistency
Determine the minimum and maximum invoice dates.
Check for invalid dates.
Verify coverage across both worksheets.
Identify unexpected gaps or inconsistencies in the date distribution.
6.6. Product and Customer Consistency
Investigate stock codes associated with different descriptions.
Inspect customer identifier consistency.
Measure the number of identifiable customers.
Identify invoices containing both positive and negative quantities, where relevant.

All checklist items remain pending until the corresponding checks have been executed and their results documented.

7. Initial Transformation Rules

These rules are candidates for implementation and must be finalized using the source data and business requirements.

Source Preservation

The original dataset must remain unchanged.

All normalization, cleaning, and aggregation should be performed in derived tables or files.

Identifier Handling

Identifiers should be stored using appropriate string types.

Missing customer identifiers must not be replaced with a shared artificial customer identifier, because doing so would combine unrelated transactions into a fictitious customer.

Missing Values

Missing values should be handled according to the purpose of each field and metric.

A transaction may remain useful for sales analysis even if it cannot be attributed to an identifiable customer.

Cancellation and Return Handling

Cancellation-related invoice identifiers and negative quantities must be investigated together.

The project must distinguish between:

Identifying a potentially cancelled or returned transaction.
Determining how that transaction affects a particular business metric.

The final inclusion and exclusion rules must be documented in BUSINESS_METRICS.md.

Monetary Values

A preliminary transaction-line value can be calculated as:

line_value = quantity * unit_price

This calculation represents a derived transaction-line amount, not automatically recognized accounting revenue, net revenue, or profit.

The project must document how cancellation-related records, returns, and other adjustments affect each reported metric.

Deduplication

Deduplication must use validated source semantics and explicit rules.

Records must not be removed solely because several fields share the same values.

8. Analytical Use Cases

The dataset can support the following analyses, subject to validation of the source data and the adopted business definitions.

Analysis	Required fields	Important limitation
Sales trends	InvoiceDate, Quantity, Price, Invoice	Transaction eligibility must be defined
Invoice volume	Invoice	Count distinct eligible invoices, not rows
Product performance	StockCode, Description, Quantity, Price	Investigate inconsistent descriptions and returns
Geographic sales	Country, transaction fields	Interpret country according to the source definition
Average invoice value	Invoice, Quantity, Price	Aggregate at invoice level before calculating the average
Customer purchasing behavior	Customer ID, InvoiceDate, transaction fields	Limited to records with identifiable customers
RFM segmentation	Customer ID, InvoiceDate, transaction fields	Requires a reference date, observation window, and documented thresholds
Cancellation analysis	Invoice, Quantity, Price	Cancellation and return identification requires validation

These use cases describe analytical possibilities, not findings already established by the project.

9. Customer RFM Requirements

RFM segmentation will be calculated for identifiable customers using eligible transactions.

Recency

The elapsed time between a documented reference date and the customer's most recent eligible purchase.

Frequency

The number of distinct eligible purchase invoices associated with a customer during the observation period.

Monetary

The total eligible transaction value associated with a customer under the adopted monetary definition.

Before implementation, the project must specify:

The analysis reference date.
The observation window.
The treatment of cancellations and returns.
The definition of an eligible purchase.
The scoring method and thresholds.
The rules used to assign segment names.

RFM is a descriptive segmentation method in this project. It must not be presented as a validated predictive model.

Records without customer identifiers cannot support reliable customer-level RFM assignments.

10. Data Limitations

The dataset does not directly establish all the information needed for broader marketing analytics.

The following metrics require additional data or a separately documented methodology:

Customer acquisition cost (CAC).
Return on advertising spend (ROAS).
Advertising spend by channel.
Advertising-attributed conversions and revenue.
Website traffic and conversion rates.
Product cost and profit margins.
A validated predictive customer lifetime value (LTV).

These metrics must not be presented as measured results when the necessary source data is unavailable.

The dataset reflects a particular retailer and historical period. Its results must not automatically be generalized to current e-commerce businesses.

11. Data Governance and Attribution

The original source and applicable license must be documented in the project README.

The dataset is published by the UCI Machine Learning Repository. Attribution and license requirements must be respected when redistributing or publishing derived materials.

Raw datasets and generated files should not be committed to version control without a specific justification.

12. Current Status

Status: Initial source documentation prepared; data validation pending.

Completed in this document:

Initial source identification.
Expected field definitions.
Proposed normalized column names.
Initial data quality checklist.
Candidate analytical use cases.
Preliminary transformation considerations.

Not yet verified:

Downloaded file structure.
Actual worksheet names and row counts.
Actual source data types.
Missing-value statistics.
Duplicate statistics.
Cancellation and return patterns.
Final transformation rules.
Final analytical schema.
13. Next Steps
Obtain the original dataset from the official source.
Inspect both worksheets and compare their schemas.
Record actual row counts, column types, and date ranges.
Calculate missing-value and duplicate statistics.
Investigate cancellation-related records and negative quantities.
Establish the source grain and appropriate analytical keys.
Finalize transformation rules.
Update this document with measured results and confirmed definitions.

The data dictionary should evolve from an initial schema reference into a verified record of the dataset actually used by the project.


## Initial Data Profiling Results

**Status:** Initial exploration completed; data quality investigation ongoing.

**Source:** UCI Machine Learning Repository — Online Retail II  
**Official URL:** https://archive.ics.uci.edu/dataset/502/online+retail+ii  
**Local file:** `data/raw_data/online_retail_II.xlsx`

### Dataset Structure

The original workbook contains two worksheets:

| Worksheet | Data rows | Columns |
|---|---:|---:|
| Year 2009-2010 | 525,461 | 8 |
| Year 2010-2011 | 541,910 | 8 |
| Combined | 1,067,371 | 8 |

The combined dataset contains the following columns:

- `Invoice`: Invoice identifier.
- `StockCode`: Product identifier.
- `Description`: Product description.
- `Quantity`: Quantity recorded on the transaction line.
- `InvoiceDate`: Transaction date and time.
- `Price`: Recorded unit price.
- `Customer ID`: Customer identifier, when available.
- `Country`: Country associated with the transaction.

Both worksheets have the expected column names.

### Observed Date Range

- Minimum timestamp: `2009-12-01 07:45:00`
- Maximum timestamp: `2011-12-09 12:50:00`
- Invalid dates after conversion with pandas: 0

### Missing Values

| Column | Missing rows |
|---|---:|
| Customer ID | 243,007 |
| Description | 4,382 |
| StockCode | 0 |
| Invoice | 0 |
| Quantity | 0 |
| InvoiceDate | 0 |
| Price | 0 |
| Country | 0 |

Missing values must be handled according to the analytical use case. Records without customer identifiers must not be treated as identifiable customers.

### Initial Data Quality Findings

| Finding | Observed count |
|---|---:|
| Rows with negative quantities | 22,950 |
| Rows with zero quantities | 0 |
| Rows with negative prices | 5 |
| Rows with zero prices | 6,202 |
| Rows with invoice identifiers beginning with `C` | 19,494 |
| Distinct `C`-prefixed invoice identifiers | 8,292 |
| Rows belonging to exact duplicate groups | 67,242 |
| Repeated occurrences beyond the first | 34,335 |
| Distinct exact duplicate groups | 32,907 |

The duplicate statistics use the eight original columns. They describe exact row repetition, not confirmed erroneous records.

### Cancellation Investigation

Of the 19,494 rows with invoice identifiers beginning with `C`, 19,493 have negative quantities and one has a positive quantity.

A further 3,457 rows have negative quantities without a `C` prefix.

These findings show that negative quantities and cancellation identifiers are related but are not interchangeable classifications.

### Negative Quantities Without a C Prefix

The investigated records have invoice identifiers beginning with `4` or `5`:

- Prefix `4`: 729 rows.
- Prefix `5`: 2,728 rows.

Many descriptions are missing or refer to operational conditions such as damaged, missing, lost, or checked items. All 3,457 records have a unit price of zero in the inspected sample.

Their exact commercial meaning and treatment remain under investigation.

### Zero-Price Records

A total of 6,202 rows have a unit price of zero. Their descriptions include missing values, operational notes, and identifiable product descriptions.

Zero price must not automatically be interpreted as an invalid record. These rows require classification before inclusion in monetary metrics.

### Negative-Price Records

Five rows have negative unit prices. Their descriptions are `Adjust bad debt`, their invoice identifiers begin with `A`, and their customer identifiers are missing.

They are preliminary candidates for classification as financial adjustments rather than ordinary merchandise sales.

### Extreme Values

Observed extreme quantities include positive and negative values of 80,995 and 74,215 units.

Some large positive quantities have corresponding negative records with matching products and quantities. These are candidates for cancellation or reversal analysis, not proof of a complete cancellation relationship.

### Important Limitations

- The profiling scripts do not establish final sales eligibility rules.
- Exact duplicates have not been removed.
- Cancellation and adjustment classifications remain preliminary.
- The original workbook remains the source of truth.
- No cleaned analytical dataset has yet been validated.
- No final PostgreSQL model has been implemented or confirmed.

### Reproducibility

Initial profiling was performed with:

- Python
- pandas 3.0.6
- openpyxl 3.1.5

Scripts used:

- `scripts/explore_dataset.py`
- `scripts/investigate_data_quality.py`
- `scripts/investigate_sales_rules.py`

The scripts read the source workbook and report exploratory statistics. They do not establish that a production ingestion pipeline or automated validation suite exists.
