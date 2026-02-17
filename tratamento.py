import pandas as pd

class Tratamento():
    def __init__(self, df:pd.DataFrame):
        self.df = df
    
    def trata_arquivo(self):
        df = self.df.copy()
        df.isna().sum()
        df = df.dropna()
        df["periodo"] = pd.to_datetime(df["periodo"])
        df = df.sort_values("periodo")
        
        df = df.set_index("periodo").asfreq("MS").reset_index()
        df["taxa_de_desemprego"] = df["taxa_de_desemprego"].ffill()
        
        df["ano"]= df["periodo"].dt.year
        df["mes"] = df["periodo"].dt.month

        return df
