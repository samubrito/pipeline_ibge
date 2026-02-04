import pandas as pd 

class FeatureEngineer:
    def __init__(self, df:pd.DataFrame):
        self.df = df

    def create_feature(self) -> pd.DataFrame:
        df = self.df.copy()
        df["media_movel_3"] = df["taxa_de_desemprego"].rolling(3).mean()
        df["media_movel_6"] = df["taxa_de_desemprego"].rolling(6).mean()
        df["lag_1"] = df["taxa_de_desemprego"].shift(1)
        df["lag_3"] = df["taxa_de_desemprego"].shift(3)
        return df.dropna()

    
