
from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/raw_data/online_retail_II.xlsx")
SHEETS = ["Year 2009-2010", "Year 2010-2011"]


def main() -> None:
    frames = [
        pd.read_excel(DATA_PATH, sheet_name=sheet)
        for sheet in SHEETS
    ]
    df = pd.concat(frames, ignore_index=True)

    df["InvoiceText"] = df["Invoice"].astype("string").str.strip()
    df["IsCancellation"] = (
        df["InvoiceText"].str.upper().str.startswith("C", na=False)
    )
    df["LineValue"] = df["Quantity"] * df["Price"]

    # 1. Negative quantities without a C-prefixed invoice.
    print("\n=== NEGATIVE QUANTITIES WITHOUT C PREFIX ===")
    negative_other = df[
        (df["Quantity"] < 0) & ~df["IsCancellation"]
    ]

    print(f"Rows: {len(negative_other):,}")
    print("\nInvoice prefix distribution:")
    print(
        negative_other["InvoiceText"]
        .str[:1]
        .value_counts(dropna=False)
        .to_string()
    )

    print("\nMost frequent descriptions:")
    print(
        negative_other["Description"]
        .value_counts(dropna=False)
        .head(20)
        .to_string()
    )

    print("\nSample records:")
    print(
        negative_other[
            [
                "Invoice",
                "StockCode",
                "Description",
                "Quantity",
                "InvoiceDate",
                "Price",
                "Customer ID",
            ]
        ]
        .head(30)
        .to_string(index=False)
    )

    # 2. Find exact positive/negative counterparts by product,
    # quantity magnitude, price and customer.
    print("\n=== POSSIBLE CANCELLATION COUNTERPARTS ===")

    candidates = df[
        (df["Quantity"] != 0) & (df["Price"] >= 0)
    ].copy()

    candidates["QuantityMagnitude"] = candidates["Quantity"].abs()

    keys = [
        "StockCode",
        "QuantityMagnitude",
        "Price",
        "Customer ID",
    ]

    positive = candidates[candidates["Quantity"] > 0]
    negative = candidates[candidates["Quantity"] < 0]

    positive_counts = (
        positive.groupby(keys, dropna=False)
        .size()
        .rename("positive_rows")
    )
    negative_counts = (
        negative.groupby(keys, dropna=False)
        .size()
        .rename("negative_rows")
    )

    matched = pd.concat(
        [positive_counts, negative_counts], axis=1
    ).fillna(0)

    matched = matched[
        (matched["positive_rows"] > 0)
        & (matched["negative_rows"] > 0)
    ]

    print(
        "Product/quantity/price/customer combinations with both signs:",
        f"{len(matched):,}",
    )
    print(
        "Positive rows in matching combinations:",
        f"{matched['positive_rows'].sum():,.0f}",
    )
    print(
        "Negative rows in matching combinations:",
        f"{matched['negative_rows'].sum():,.0f}",
    )

    # Show examples where both signs occur for the same product,
    # quantity magnitude, price and identifiable customer.
    examples = matched.reset_index()
    examples = examples[examples["Customer ID"].notna()].head(10)

    print("\nExample matching combinations:")
    print(examples.to_string(index=False))

    # 3. Zero-price records and financial adjustments.
    print("\n=== ZERO-PRICE RECORDS ===")
    zero_price = df[df["Price"] == 0]

    print(f"Rows: {len(zero_price):,}")
    print("\nInvoice prefix distribution:")
    print(
        zero_price["InvoiceText"]
        .str[:1]
        .value_counts(dropna=False)
        .to_string()
    )

    print("\nDescriptions:")
    print(
        zero_price["Description"]
        .value_counts(dropna=False)
        .head(20)
        .to_string()
    )

    print("\n=== SPECIAL INVOICE PREFIXES ===")
    prefix = df["InvoiceText"].str[:1].str.upper()

    print(
        pd.DataFrame(
            {
                "rows": df.groupby(prefix, dropna=False).size(),
                "negative_quantity_rows": df[
                    df["Quantity"] < 0
                ].groupby(prefix, dropna=False).size(),
                "negative_price_rows": df[
                    df["Price"] < 0
                ].groupby(prefix, dropna=False).size(),
            }
        ).fillna(0).to_string()
    )


if __name__ == "__main__":
    main()
