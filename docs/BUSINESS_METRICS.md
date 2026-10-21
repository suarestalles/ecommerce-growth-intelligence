
# Business Metrics and Rules

**Project:** E-commerce Growth Intelligence  
**Status:** Draft — definitions and eligibility rules require validation  
**Dataset:** UCI Online Retail II  
**Last reviewed:** 2026-10-21

## 1. General Principles

- Preserve the original source data.
- Keep raw records separate from classified analytical records.
- Document the grain of every analytical table.
- Apply consistent eligibility rules to related metrics.
- Do not equate gross merchandise sales value with accounting revenue or profit.
- Do not infer customer identity when `Customer ID` is missing.
- Do not remove duplicate rows without evidence that they are erroneous.
- Keep cancellations, returns, and financial adjustments distinguishable where the source supports it.

## 2. Sales Metrics

### Gross Merchandise Sales Value

**Proposed definition:** Sum of `Quantity * Price` over records explicitly classified as eligible merchandise sales.

The eligibility rules are not yet finalized.

Negative quantities, zero prices, cancellation records, and operational adjustments require explicit classification.

### Units Sold

**Proposed definition:** Sum of quantities for eligible merchandise sales.

The treatment of returns and reversals must be documented. Gross positive quantities and net quantities after adjustments may be reported separately if useful.

### Eligible Invoices

**Proposed definition:** Distinct invoice identifiers associated with eligible merchandise sales.

Cancellation-only invoices must not automatically count as sales invoices. Mixed invoices require a documented policy.

### Average Invoice Value

**Proposed definition:**

Eligible merchandise sales value / number of eligible sales invoices.

The numerator and denominator must use compatible eligibility rules and the same filters.

### Sales Trends

Aggregate eligible sales by transaction date using a documented calendar convention.

Invalid dates, excluded adjustments, and the selected observation window must be handled consistently.

## 3. Customer Metrics

### Identifiable Customers

Distinct non-null customer identifiers in the eligible analytical population.

The total number of identifiable customers must not be calculated by adding distinct counts from separate worksheets, because the same customer may appear in both.

### Recency

Difference between a documented reference date and the most recent eligible purchase date for an identifiable customer.

### Frequency

Number of distinct eligible purchase invoices for an identifiable customer within the selected observation window.

### Monetary

Sum of eligible merchandise sales value for an identifiable customer within the selected observation window.

### Repeat-Purchase Rate

Proportion of identifiable customers with at least two eligible purchase invoices within the defined observation window.

The population, observation window, and denominator must be explicitly documented.

### RFM Segmentation

RFM is a descriptive heuristic, not a validated predictive model.

The reference date, scoring approach, thresholds, and treatment of incomplete customer histories must be documented before implementation.

## 4. Cancellations and Adjustments

### C-Prefixed Invoices

Invoice identifiers beginning with `C` are candidates for cancellation classification.

Initial profiling identified 8,292 distinct identifiers and 19,494 associated rows.

The relationship between these records and original sales must be investigated before defining net or cancellation-adjusted metrics.

### Negative Quantities Without a C Prefix

Initial profiling identified 3,457 such rows. Their descriptions often contain operational notes, and their observed unit prices are zero.

These rows must not automatically be included in merchandise sales or treated as ordinary customer returns.

### Negative Unit Prices

Five records have negative unit prices and descriptions indicating bad-debt adjustments.

These are preliminary candidates for financial-adjustment classification and must be separated from ordinary merchandise sales unless further evidence supports another interpretation.

### Zero Unit Prices

Zero-price records must be preserved during staging and classified before monetary metrics are calculated.

A zero price does not, by itself, establish that the row is erroneous.

## 5. Duplicate Handling

Exact duplicate rows have been identified, but their business meaning has not been fully validated.

No blanket deduplication rule is approved at this stage.

The pipeline must preserve sufficient information to reproduce and audit the source data.

## 6. Metrics Not Supported by the Primary Dataset Alone

The dataset does not directly provide all the information needed to calculate:

- Customer acquisition cost (CAC).
- Return on advertising spend (ROAS).
- Visitor-to-buyer conversion.
- Profit or contribution margin.
- Predictive customer lifetime value.

These metrics require additional suitable data or a separately documented methodology.

## 7. Pending Decisions

- Final merchandise sales eligibility rules.
- Treatment of cancellation and reversal records.
- Treatment of negative quantities without a cancellation prefix.
- Treatment of zero-price records.
- Classification of financial adjustments.
- Deduplication policy, if any.
- Reference date and thresholds for RFM.
- Final definitions of gross and adjustment-aware sales metrics.

These decisions must be documented and tested before the production analytical model is finalized.
