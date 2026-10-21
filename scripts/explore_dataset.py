
from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/raw_data/online_retail_II.xlsx")

SHEETS = ["Year 2009-2010", "Year 2010-2011"]

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


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH.resolve()}"
        )

    frames = []

    for sheet in SHEETS:
        df = pd.read_excel(
            DATA_PATH,
            sheet_name=sheet,
            engine="openpyxl",
        )

        print(f"\n{'=' * 60}")
        print(f"WORKSHEET: {sheet}")
        print(f"Rows: {len(df):,}")
        print(f"Columns: {len(df.columns)}")
        print("Column names:", df.columns.tolist())

        missing_columns = set(EXPECTED_COLUMNS) - set(df.columns)
        if missing_columns:
            raise ValueError(
                f"Unexpected schema. Missing columns: {missing_columns}"
            )

        df["InvoiceDate"] = pd.to_datetime(
            df["InvoiceDate"], errors="coerce"
        )

        print("\nData types:")
        print(df.dtypes.to_string())

        print("\nMissing values:")
        print(
            df.isna().sum()
            .sort_values(ascending=False)
            .to_string()
        )

        print("\nNumeric summaries:")
        print(df[["Quantity", "Price"]].describe().to_string())

        print("\nPotential data quality issues:")
        print(f"Fully duplicated rows: {df.duplicated().sum():,}")
        print(f"Invalid dates: {df['InvoiceDate'].isna().sum():,}")
        print(f"Negative quantities: {(df['Quantity'] < 0).sum():,}")
        print(f"Zero quantities: {(df['Quantity'] == 0).sum():,}")
        print(f"Negative prices: {(df['Price'] < 0).sum():,}")
        print(f"Zero prices: {(df['Price'] == 0).sum():,}")

        invoice_text = df["Invoice"].astype("string").str.strip()
        cancellations = invoice_text.str.upper().str.startswith(
            "C", na=False
        )
        print(f"Invoice IDs starting with C: {cancellations.sum():,}")

        print("\nDate range:")
        print(f"Minimum: {df['InvoiceDate'].min()}")
        print(f"Maximum: {df['InvoiceDate'].max()}")

        print("\nDistinct values:")
        for column in ["Invoice", "StockCode", "Customer ID", "Country"]:
            print(f"{column}: {df[column].nunique(dropna=True):,}")

        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)

    print(f"\n{'=' * 60}")
    print("COMBINED DATASET")
    print(f"Total rows: {len(combined):,}")
    print(f"Total columns: {len(combined.columns)}")
    print(
        "Fully duplicated rows across both sheets:",
        f"{combined.duplicated().sum():,}",
    )
    print(f"Date range: {combined['InvoiceDate'].min()} to "
          f"{combined['InvoiceDate'].max()}")
    print("\nCombined missing values:")
    print(combined.isna().sum().sort_values(ascending=False).to_string())


if __name__ == "__main__":
    main()
