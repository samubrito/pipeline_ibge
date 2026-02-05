from ingestao import IBGEClient
from tratamento import Tratamento
from feature import FeatureEngineer
from modelo import Modelo

def main():
    link = "https://servicodados.ibge.gov.br/api/v3/agregados/4099/periodos/all/variaveis/4099?localidades=N1[all]"

    cliente = IBGEClient(link)
    df_raw = cliente.busca_base()

    df_processed = Tratamento(df_raw)
    df_processed = df_processed.trata_arquivo()

    ft = FeatureEngineer(df_processed)
    df_feature = ft.create_feature()

    modelo = Modelo()
    idx, previsoes, mae = modelo.train(df_feature)

    print(f"MAE do modelo: {mae:.2f}")

    resultado = df_feature.loc[idx].copy()
    resultado["previsao"] = previsoes
    resultado["erro"] = resultado["taxa_de_desemprego"] - resultado["previsao"]

    resultado.to_csv("previsao_desemprego.csv", index=False)

if __name__ == "__main__":
    main()