
from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/raw_data/online_retail_II.xlsx")
SHEETS = ["Year 2009-2010", "Year 2010-2011"]


def main() -> None:
    frames = []

    for sheet in SHEETS:
        df = pd.read_excel(
            DATA_PATH,
            sheet_name=sheet,
            engine="openpyxl",
        )
        df["SourceWorksheet"] = sheet
        frames.append(df)

    df = pd.concat(frames, ignore_index=True)

    invoice = df["Invoice"].astype("string").str.strip()
    cancellation = invoice.str.upper().str.startswith("C", na=False)
    negative_quantity = df["Quantity"] < 0
    zero_price = df["Price"] == 0
    negative_price = df["Price"] < 0
    exact_duplicate = df.duplicated(
        subset=[
            "Invoice",
            "StockCode",
            "Description",
            "Quantity",
            "InvoiceDate",
            "Price",
            "Customer ID",
            "Country",
        ],
        keep=False,
    )

    print("\n=== CANCELLATIONS AND NEGATIVE QUANTITIES ===")
    print(f"Rows with C-prefixed invoice: {cancellation.sum():,}")
    print(
        "Distinct C-prefixed invoices:",
        f"{invoice[cancellation].nunique():,}",
    )
    print(f"Rows with negative quantity: {negative_quantity.sum():,}")
    print(
        "Negative quantity + C-prefixed invoice:",
        f"{(negative_quantity & cancellation).sum():,}",
    )
    print(
        "Negative quantity without C prefix:",
        f"{(negative_quantity & ~cancellation).sum():,}",
    )
    print(
        "C-prefixed invoices with positive quantities:",
        f"{(cancellation & (df['Quantity'] > 0)).sum():,}",
    )

    print("\n=== INVOICE-LEVEL INVESTIGATION ===")
    invoice_df = df.assign(
        InvoiceNormalized=invoice,
        IsCancellation=cancellation,
        IsNegativeQuantity=negative_quantity,
        LineValue=df["Quantity"] * df["Price"],
    )

    invoice_summary = invoice_df.groupby(
        "InvoiceNormalized", dropna=False
    ).agg(
        row_count=("Invoice", "size"),
        negative_quantity_rows=("IsNegativeQuantity", "sum"),
        cancellation_rows=("IsCancellation", "sum"),
        line_value=("LineValue", "sum"),
    )

    print(
        "Invoices with multiple rows:",
        f"{(invoice_summary['row_count'] > 1).sum():,}",
    )
    print(
        "Invoices containing negative quantities:",
        f"{(invoice_summary['negative_quantity_rows'] > 0).sum():,}",
    )
    print(
        "Invoices containing C-prefixed rows:",
        f"{(invoice_summary['cancellation_rows'] > 0).sum():,}",
    )

    print("\n=== DUPLICATE INVESTIGATION ===")
    print(
        "Rows belonging to repeated exact-row groups:",
        f"{exact_duplicate.sum():,}",
    )
    print(
        "Repeated occurrences beyond the first:",
        f"{df.duplicated(subset=EXPECTED_COLUMNS, keep='first').sum():,}",
    )

    duplicate_groups = (
        df.loc[exact_duplicate]
        .groupby(EXPECTED_COLUMNS, dropna=False)
        .size()
        .sort_values(ascending=False)
    )

    print("Number of repeated exact-row groups:", f"{len(duplicate_groups):,}")
    print("Top 10 repeated groups:")
    print(duplicate_groups.head(10).to_string())

    print("\n=== PRICE INVESTIGATION ===")
    print(f"Zero-price rows: {zero_price.sum():,}")
    print(f"Negative-price rows: {negative_price.sum():,}")

    print("\nMost common products with zero prices:")
    print(
        df.loc[zero_price]
        .groupby(["StockCode", "Description"], dropna=False)
        .size()
        .sort_values(ascending=False)
        .head(15)
        .to_string()
    )

    print("\nNegative-price records:")
    print(
        df.loc[
            negative_price,
            [
                "Invoice",
                "StockCode",
                "Description",
                "Quantity",
                "InvoiceDate",
                "Price",
                "Customer ID",
            ],
        ]
        .to_string(index=False)
    )

    print("\n=== EXTREME VALUES ===")
    print("\nLargest positive quantities:")
    print(
        df.nlargest(10, "Quantity")[
            ["Invoice", "StockCode", "Description", "Quantity", "Price"]
        ].to_string(index=False)
    )

    print("\nLargest absolute line values:")
    df["LineValue"] = df["Quantity"] * df["Price"]
    print(
        df.loc[df["LineValue"].abs().nlargest(10).index, [
            "Invoice",
            "StockCode",
            "Description",
            "Quantity",
            "Price",
            "LineValue",
        ]].to_string(index=False)
    )


EXPECTED_COLUMNS = [
    "Invoice",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "Price",
    "Customer ID",
    "Country",
]


if __name__ == "__main__":
    main()
