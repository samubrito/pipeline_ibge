import requests
import pandas as pd

class IBGEClient:
    def __init__(self, link):
        self.link = link

    def busca_base(self) -> pd.DataFrame:
        req = requests.get(self.link)
        dados = req.json()
        serie = dados[0]["resultados"][0]["series"][0]["serie"]
        
        df = pd.DataFrame.from_dict(serie, orient="index", columns=["taxa_de_desemprego"]).reset_index().rename(columns={"index":"periodo"})
        df["taxa_de_desemprego"] = df["taxa_de_desemprego"].astype(float)
        df["periodo"] = pd.to_datetime(df["periodo"], format="%Y%m")

        return df



