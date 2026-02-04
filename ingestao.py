import requests
import pandas as pd
import os
import json

pasta = r"C:\Users\samue\Desktop\pipeline de dados\data"
link = r"https://servicodados.ibge.gov.br/api/v3/agregados/4099/periodos/all/variaveis/4099?localidades=N1[all]"

req = requests.get(link)
dados = req.json()
serie = dados[0]["resultados"][0]["series"][0]["serie"]
df = pd.DataFrame.from_dict(serie, orient="index", columns=["taxa_de_desemprego"]).reset_index().rename(columns={"index":"periodo"})
df["taxa_de_desemprego"] = df["taxa_de_desemprego"].astype(float)
df["periodo"] = pd.to_datetime(df["periodo"], format="%Y%m")

arquivo_csv = os.path.join(pasta,"raw\desemprego_ibge.csv")
df.to_csv(arquivo_csv, index=False)


arquivo_json = json.dumps(serie, indent=1, ensure_ascii=False)


