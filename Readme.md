<h1>IBGE Unemployment Pipeline: ETL & Predictive Modeling</h1>
<p align="center">
  <img src="imagens/pipeline_ibge.png" alt="IBGE Unemployment Pipeline: ETL & Predictive Modeling" width="400px">
</p>
<p>Este projeto estabelece um fluxo de dados completo (End-to-End) que monitora, processa e prevê a Taxa de Desocupação no Brasil utilizando dados oficiais da API do IBGE (PNAD Contínua). A solução é 100% automatizada, rodando em nuvem e servindo dados tratados para um dashboard executivo no Power BI.</p>

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
- [4. Detalhes da implementação](#detalhes)
    - [4.1. Engenharia de Atributos (Features)](#features)
    - [4.2. Modelagem Preditiva (Linear Regression)](#modelagem)
    - [4.3. Automação github actions (CI/CD)](#automacao)
- [5. Como executar](#executar)
- [6. Power BI](#power_bi)


</details>

<h2 id="visao_geral">1. Visão Geral da Arquitetura 🏗</h2>
<p>
A solução foi desenhada para ser resiliente e independente de intervenção humana:
    <ul>
        <li>Ingestão: Consumo de JSON da API de Agregados do IBGE.</li>
        <li>Transformação: Limpeza, tipagem de dados e ordenação temporal.</li>
        <li>Feature Engineering: Criação de médias móveis e lags temporais.</li>
        <li>Machine Learning: Regressão via Linear Regression para estimar a taxa de desemprego.</li>
        <li>Deployment: GitHub Actions executa o script e faz o commit do CSV atualizado.</li>
        <li>Visualização: Power BI lê o arquivo diretamente do repositório via link Web.</li>
    </ul>
</p>

<h2 id="tecnologias">2. Tecnologias Utilizadas 🛠</h2>

<ul>
    <li>Linguagem: Python 3.11</li>
    <li>Manipulação de Dados: Pandas, Numpy</li>
    <li>Machine Learning: Scikit-Learn (RandomForestRegressor)</li>
    <li>API: Requests (IBGE API v3)</li>
    <li>Orquestração: GitHub Actions (YAML)</li>
    <li>Visualização: Power BI</li>
</ul>


<h2 id="estrutura">3. Estrutura do Projeto 📂</h2>

### 🏗️ Estrutura do Projeto

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

<h2 id="detalhes">4. Detalhes da Implementação ⚙️</h2>

<h3 id="features">4.1. Engenharia de Atributos (Features)<h3>
Para capturar a sazonalidade e a tendência do desemprego, foram criadas:

Médias Móveis (3 e 6 meses): Suavizam ruídos e mostram a tendência de curto/médio prazo.

Lags (1 e 3 meses): Permitem que o modelo entenda o valor imediatamente anterior (autocorrelação).

<h3 id="modelagem">4.2. O Modelo de Machine Learning</h3>
Utilizou-se o algoritmo Random Forest Regressor com 200 árvores de decisão.

Nota técnica: O split de dados foi feito de forma temporal (shuffle=False), garantindo que o modelo seja testado no futuro e não em dados aleatórios do passado, simulando um cenário real de previsão.

<h3 id="automacao">4.3. Automação com GitHub Actions</h3>
O pipeline está configurado para rodar automaticamente (atualmente em um intervalo de 5 minutos para fins de teste/demonstração), realizando o commit dos novos dados no repositório. Isso garante que o Power BI sempre tenha dados frescos ao ser atualizado.

<h2 id="executar">5. Como Executar 🚀</h2>
Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute manualmente: python main.py

```bash
python main.py
```

O arquivo final será gerado em data/output/previsao_desemprego.csv, contendo as colunas de taxa real, previsão do modelo e o erro calculado.

<h2 id="power_bi">6. Power BI 📈</h2>