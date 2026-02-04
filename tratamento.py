import pandas as pd

class Tratamento():
    def __init__(self, df:pd.DataFrame):
        self.df = df
    
    def trata_arquivo(self):
        df = self.df.copy()
        df = df.sort_values("periodo")
        df.isna().sum()
        df = df.dropna()
        df["periodo"] = pd.to_datetime(df["periodo"])
        df["ano"]= df["periodo"].dt.year
        df["mes"] = df["periodo"].dt.month

        return df
