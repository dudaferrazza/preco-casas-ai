import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("dataset.csv")

X = df[["area", "quartos", "banheiros"]]
y = df["preco"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Modelo treinado com sucesso!")