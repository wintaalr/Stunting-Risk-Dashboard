import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "Dataset_bersih.xlsx"

print("Loading dataset from:", DATA_PATH)
df = pd.read_excel(DATA_PATH)
print(df.head())
print("\nShape:", df.shape)
