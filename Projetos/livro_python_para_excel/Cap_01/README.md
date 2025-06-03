# Cap 01 - Por que Python para Excel

-> Power Query utiliza linguagem M

-> Power Pivote utiliza liguagem DAX

->Python é uma linguagem de programção de alto nível, ela é interpretada.

### 🧠 **Resumo Comparativo**

|        Característica        |        **Power Query**        |           **Power Pivot**           |
| :----------------------------: | :----------------------------------: | :---------------------------------------: |
|       Função principal       | ETL (Extrair, Transformar, Carregar) |           Modelagem e análise           |
|        Linguagem usada        |                  M                  |                    DAX                    |
| Trabalha com múltiplas fontes |                 Sim                 |  Sim, após importação via Power Query  |
|      Cria relacionamentos      |                 Não                 |                    Sim                    |
|       Cria medidas/KPIs       |                 Não                 |                    Sim                    |
|         Processamento         |       Antes da carga no Excel       | Depois da carga, dentro do modelo tabular |
|        Utilidade comum        |  Limpeza e padronização dos dados  |    Análise e visualização de dados    |

-> Python foi criado em 1991, 6 anos após o excel.

-> Em 2005 foi lançada a biblioteca NumPy.

## 🧪 O que é a NumPy?

**NumPy** (Numerical Python) é uma **biblioteca open source** para Python, especializada em computação numérica e científica. Ela fornece:

* Um  **objeto central chamado `ndarray`** , que representa arrays multidimensionais de alta performance;
* Funções eficientes para operações matemáticas vetoriais e matriciais;
* Ferramentas para  **álgebra linear** ,  **estatística** ,  **transformadas de Fourier** , entre outras.

-> Em 2008 foi lançada a biblioteca Pandas.

## 🐼 O que é o Pandas?

**Pandas** é uma **biblioteca de código aberto** para análise e manipulação de dados em Python. Ela fornece  **estruturas de dados poderosas e flexíveis** , com foco em tabelas e séries temporais, altamente inspiradas nos dataframes da linguagem R.

O nome "Pandas" vem de  **"Panel Data"** , um termo econométrico.


---



# Separação de conceitos:

## 🧩 O que é Modularidade?

A **modularidade** é o  **princípio de decompor um sistema complexo em partes menores e independentes** , chamadas  **módulos** , de forma que cada módulo execute uma função específica, podendo ser desenvolvido, testado e mantido de forma isolada.

## Camadas:

* **Camada de apresentação:** Interface com o **usuário final**
* **Camada de negócio:** Contém **as regras de negócio** e a lógica que define o comportamento do sistema.
* **Camada de dados:** Gerencia o  **acesso aos dados persistentes** .

## 🎯 Benefícios da Arquitetura em Camadas

* 📦  **Organização do código** : cada parte com uma função bem definida;
* 🔁  **Reutilização** : mesma lógica pode ser usada com diferentes interfaces ou bancos;
* 🧪  **Testabilidade** : permite testar camadas separadamente;
* 🔒  **Segurança e controle** : o acesso aos dados pode ser restringido e auditado.

## 🎓 Aplicações práticas:

* **No Power Apps** : dividir um app em telas (módulos) como: cadastro, inspeção, análise.
* **Em Python** : criar arquivos distintos para banco de dados, interface e lógica de negócio.
* **Na manutenção industrial** : segmentar um sistema de produção em módulos operacionais independentes, permitindo manutenções setorizadas e minimizando paradas totais.



---

# Princípio DRY


Esse conceito é apresentado no livro O Progrogramador Pragmático, de Hunt e Thomas (Bookman).

DRY significa:

***Don't repeat yourself (Não se repita)***
