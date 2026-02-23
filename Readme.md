<h1>IBGE Unemployment Pipeline: ETL & Predictive Modeling</h1>
<p align="center">
  <img src="imagens/pipeline_ibge.png" alt="IBGE Unemployment Pipeline: ETL & Predictive Modeling" width="400px">
</p>
<p>O acompanhamento de indicadores macroeconômicos, como a taxa de desemprego, frequentemente esbarra na necessidade de coleta manual em portais públicos e na falta de ferramentas que antecipem tendências de curto prazo para suporte à decisão. Foi desenvolvida uma solução de dados ponta a ponta (End-to-End) que automatiza a extração de dados da API do IBGE via Python, realiza o processamento de variáveis sazonais e treina um modelo de Regressão Linear. Todo o ecossistema é orquestrado por uma pipeline de CI/CD que garante a atualização recorrente dos dados. A implementação resultou na eliminação total de intervenção manual no ciclo de vida do dado e na criação de uma camada preditiva monitorada. Isso permite que gestores comparem dados reais com projeções através de métricas de erro como MAE e MAPE, acelerando a identificação de mudanças no cenário econômico.</p>

<h2>Diferenciais do Projeto</h2>
<ul>
    <li>Pipeline Modular: Código desenvolvido em Python utilizando Programação Orientada a Objetos (POO) para facilitar a manutenção.</li>
    <li>Machine Learning em Produção: Modelo preditivo treinado e executado automaticamente via CI/CD.</li>
    <li>Automação Total: Orquestração via GitHub Actions, eliminando processos manuais.</li>
    <li>Conexão Direta com BI: O Power BI consome os dados diretamente do repositório, garantindo atualização constante.</li>
</ul>

<details open="open">

<summary><h2>📋 Sumário</h2></summary>

- [1. Visão Geral da Arquitetura](#visao_geral)
- [2. Tecnologias Utilizadas](#tecnologias)
- [3. Estrutura do Projeto](#estrutura)
- [4. Como executar](#executar)
- [5. Análise e Visualização](#power_bi)


</details>

<h2 id="visao_geral">1. Visão Geral da Arquitetura</h2>
<p>
A solução foi desenhada para ser resiliente e independente de intervenção manual:
    <ul>
        <li>Ingestão: Consumo de JSON da API de Agregados do IBGE.</li>
        <li>Transformação: Limpeza, tipagem de dados e ordenação temporal.</li>
        <li>Feature Engineering: Criação de médias móveis e lags temporais.</li>
        <li>Machine Learning: Regressão via Linear Regression para estimar a taxa de desemprego.</li>
        <li>Deployment: GitHub Actions executa o script e faz o commit do CSV atualizado.</li>
        <li>Visualização: Power BI lê o arquivo diretamente do repositório via link Web.</li>
    </ul>
</p>

<h2 id="tecnologias">2. Tecnologias Utilizadas</h2>

<ul>
    <li>Linguagem: Python 3.11</li>
    <li>Manipulação de Dados: Pandas, Numpy</li>
    <li>Machine Learning: Scikit-Learn (LinearRegression)</li>
    <li>API: Requests (IBGE API v3)</li>
    <li>Orquestração: GitHub Actions (YAML)</li>
    <li>Visualização: Power BI</li>
</ul>


<h2 id="estrutura">3. Estrutura do Projeto</h2>
<p>O projeto foi construído sob os princípios de Programação Orientada a Objetos (POO), dividido em módulos especializados:
<ul>
    <li>Ingestão (ingestao.py): Consumo da API de Agregados do IBGE, tratando a resposta JSON e convertendo-a em uma estrutura tabular de séries temporais.</li>
    <li>Tratamento de Dados (tratamento.py): Normalização de períodos e tratamento de valores ausentes (Forward Fill), garantindo a integridade da série histórica.</li>
    <li>Feature Engineering (feature.py): Criação de janelas de Média Móvel (3 e 6 meses) e Defasagens (Lags) para capturar a memória estatística da série e alimentar o modelo preditivo.</li>
    <li>Treinamento do Modelo (modelo.py): Aplicação de Regressão Linear com separação temporal de treino e teste. O modelo é avaliado pelo Erro Médio Absoluto (MAE) para garantir a confiabilidade das projeções.</li>
    <li>Automação (pipeline.yml): Utilização do GitHub Actions para execução do script main.py de forma agendada (semanalmente), realizando o commit automático do dataset atualizado no repositório.</li>
</ul>
</p>


```plaintext
📦 supply-chain-analytics
 ├── 📂 .github/workflows
 │   └── ⚙️ main.yml            # Pipeline de CI/CD (GitHub Actions)
 ├── 📂 data
 │   └── 📂 output
 │       └── 📊 previsao_desemprego.csv  # Dataset processado para o Power BI
 ├── 🐍 ingestao.py            # Módulo de extração de dados via API
 ├── 🐍 tratamento.py          # Script de limpeza e Data Wrangling
 ├── 🐍 feature.py             # Engenharia de variáveis temporais
 ├── 🐍 modelo.py              # Script de treinamento do modelo preditivo
 ├── 🚀 main.py                # Ponto de entrada (Orquestrador do fluxo)
 └── 📋 requirements.txt       # Lista de dependências do ambiente
```

<h2 id="executar">4. Como Executar 🚀</h2>
Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute manualmente: python main.py

```bash
python main.py
```

O arquivo final será gerado em data/output/previsao_desemprego.csv, contendo as colunas de taxa real, previsão do modelo e o erro calculado.

<h2 id="power_bi">5. Análise e Visualização</h2>
<p align="center">
  <img src="imagens/power_bi.png" alt="Power BI" width="400px">
</p>
<p>O dashboard integrado atua como a camada de monitoramento do modelo, permitindo a validação estatística das previsões frente aos dados reais coletados da API.</p>
<h3>Métricas de Performance do Modelo</h3>
<p>Para medir a precisão e a confiabilidade das projeções, foram utilizadas as seguintes métricas técnicas:<p>
<ul>
    <li>MAE (Mean Absolute Error): Representa o Erro Médio Absoluto de 0,06. Esta métrica indica que, em média, as previsões do modelo divergem apenas 0,06 pontos percentuais da taxa real, demonstrando uma alta aderência aos dados históricos.</li>
    <li>MAPE (Mean Absolute Percentage Error): Calculado em 0,89%, esta métrica expressa o erro em termos percentuais. Um erro abaixo de 1% reforça a precisão do modelo para fins de planejamento e análise macroeconômica.</li>
    <li>Bias (Viés): Registrado em -0,02, o viés indica se o modelo tende a subestimar ou superestimar a taxa real. O valor próximo de zero demonstra que o modelo é equilibrado, sem tendências sistemáticas de erro para mais ou para menos.</li>

</ul>

<h3>Indicadores Atuais</h3>
<p>Taxa Atual vs. Previsão: O dashboard apresenta a Taxa Atual de 5,10 em comparação à Previsão de 5,06.<p>
<ul>
    <li>Variação Mensal: Registra uma queda de -0,10, permitindo a leitura rápida da tendência de curto prazo no mercado de trabalho.</li>
</ul>

<h3>Gráfico de Correlação: Taxa Real x Prevista</h3>
<p>O gráfico de dispersão (Scatter Chart) é utilizado para validar a performance da Regressão Linear:</p>
<ul>
    <li>Distribuição: Os pontos seguem uma tendência diagonal clara, indicando uma forte correlação positiva entre os valores reais e as previsões.</li>
    <li>Análise de Outliers: A proximidade dos pontos em relação à linha imaginária de tendência confirma que o modelo consegue capturar a variabilidade da taxa de desemprego com baixo desvio, validando a escolha das features (médias móveis e lags) utilizadas no treinamento.</li>
</ul>

<h3>Análise de Erro por Período</h3>
<p>O gráfico de barras lateral detalha o % Erro por mês/ano, permitindo identificar sazonalidades ou períodos específicos (como o final de 2024 e início de 2025) onde o desvio do modelo foi ligeiramente maior ou menor.</p>
