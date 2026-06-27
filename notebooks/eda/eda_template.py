import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "Dataset_bersih.xlsx"

df = pd.read_excel(DATA_PATH)
print(df.head())
print("\nColumns:", list(df.columns))
print("\nDescriptive statistics:\n", df.describe())
