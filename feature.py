import pandas as pd 
import os

pasta_atual = os.getcwd()
df = pd.read_csv(os.path.join(pasta_atual,"pipeline de dados\data\processed\desemprego_tratado.csv"))
df["media_movel_3"] = df["taxa_de_desemprego"].rolling(3).mean()
df["media_movel_6"] = df["taxa_de_desemprego"].rolling(6).mean()
df["lag_1"] = df["taxa_de_desemprego"].shift(1)
df["lag_3"] = df["taxa_de_desemprego"].shift(3)
df = df.dropna()

X = df[["mes", "media_movel_3", "media_movel_6", "lag_1", "lag_3"]]
y = df["taxa_de_desemprego"]
