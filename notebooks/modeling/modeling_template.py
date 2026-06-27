import pandas as pd
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "Dataset_bersih.xlsx"

df = pd.read_excel(DATA_PATH)
print(df.head())

# Placeholder: replace with your actual feature/target selection
X = df[["Sanitasi", "Air Bersih", "Imunisasi"]]
y = df["Persentase Stunting"]

model = LinearRegression()
model.fit(X, y)
pred = model.predict(X)

print("MAE:", mean_absolute_error(y, pred))
print("RMSE:", mean_squared_error(y, pred, squared=False))
print("R2:", r2_score(y, pred))
