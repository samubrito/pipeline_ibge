import pandas as pd
import os
import ingestao

df = pd.read_csv(ingestao.arquivo_csv)
df = df.sort_values("periodo")
df.isna().sum()
df = df.dropna()
df["periodo"] = pd.to_datetime(df["periodo"])
df["ano"]= df["periodo"].dt.year
df["mes"] = df["periodo"].dt.month
arquivo_csv = os.path.join(ingestao.pasta, "processed\desemprego_tratado.csv")
df.to_csv(arquivo_csv, index=False)
