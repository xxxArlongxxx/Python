# 

# Série Histórica de Preços de Combustíveis e de GLP

## Dados de 01/01/2018 até 31/12/2024

### Fonte: [https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp]

### Biblioteca usada: Pandas

### Princpipais comandos:


## 📁 **Leitura de Dados**

| Comando             | Descrição               | Exemplo                           |
| ------------------- | ------------------------- | --------------------------------- |
| `pd.read_csv()`   | Lê arquivos CSV          | `pd.read_csv('arquivo.csv')`    |
| `pd.read_excel()` | Lê arquivos Excel        | `pd.read_excel('arquivo.xlsx')` |
| `pd.read_sql()`   | Lê dados de um banco SQL | `pd.read_sql(query, conn)`      |



## 🔍 **Visualização Inicial**

| Comando           | Descrição                                      |
| ----------------- | ------------------------------------------------ |
| `df.head(n)`    | Mostra as `n`primeiras linhas                  |
| `df.tail(n)`    | Mostra as `n`últimas linhas                   |
| `df.info()`     | Informações gerais do DataFrame                |
| `df.describe()` | Estatísticas descritivas (média, desvio, etc.) |


## 🔎 **Acesso aos Dados**

| Comando                  | Descrição                   | Exemplo        |
| ------------------------ | ----------------------------- | -------------- |
| `df['coluna']`         | Acessa uma coluna             | `df['Nome']` |
| `df[['col1', 'col2']]` | Acessa múltiplas colunas     |                |
| `df.loc[linha]`        | Acessa por**rótulo**   |                |
| `df.iloc[linha]`       | Acessa por**posição** |                |


## 🔧 **Manipulação**

| Comando                                  | Descrição             |
| ---------------------------------------- | ----------------------- |
| `df['nova'] = ...`                     | Cria nova coluna        |
| `df.drop('coluna', axis=1)`            | Remove coluna           |
| `df.rename(columns={'antigo':'novo'})` | Renomeia colunas        |
| `df.sort_values(by='coluna')`          | Ordena por coluna       |
| `df.fillna(valor)`                     | Preenche valores nulos  |
| `df.dropna()`                          | Remove linhas com nulos |


## 📈 **Estatísticas**

| Comando               | Descrição                 |
| --------------------- | --------------------------- |
| `df.mean()`         | Média                      |
| `df.median()`       | Mediana                     |
| `df.std()`          | Desvio padrão              |
| `df.value_counts()` | Contagem de valores únicos |


## 💾 **Exportação de Dados**

| Comando                                 | Descrição      |
| --------------------------------------- | ---------------- |
| `df.to_csv('saida.csv', index=False)` | Salva como CSV   |
| `df.to_excel('saida.xlsx')`           | Salva como Excel |
