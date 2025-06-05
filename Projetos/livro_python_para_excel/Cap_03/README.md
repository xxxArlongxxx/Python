# Primeiros Passos com Python

## Váriavel:

Uma váriavel é um valor atribuido a um elemento, pode ser do tipo:

* Integer
* Float
* String
* Bool
* Etc

## Indexação:

No Python os elementos possuem um indice que começa com 0, indo da esquerda para a direita.

Caso se queira o ultimo número, podesse utilizar o -1 para retornar esse elemento, exemplo:

p = python

p[0]

return:p


## 🔹 Lista (`list`)

### 📌 Características:

* Ordenada (mantém a ordem de inserção).
* Mutável (pode ser modificada após a criação).
* Permite elementos duplicados.
* Aceita tipos mistos de dados.

### 📜 Sintaxe:

minha_lista = [10, 'manutenção', 3.14, True]

### 🛠️ Métodos comuns:

* `append()`: adiciona um item no final.
* `remove()`: remove um item específico.
* `sort()`: ordena os elementos.
* `pop()`: remove um item por índice.

### 📌 Uso típico:

Para armazenar sequências de dados que podem mudar ao longo do tempo, como uma lista de ordens de serviço.

---

## 🔹 Dicionário (`dict`)

### 📌 Características:

* Não ordenado até o Python 3.6; ordenado a partir do Python 3.7+ (preserva a ordem de inserção).
* Mutável.
* Não permite chaves duplicadas.
* Armazena pares  **chave: valor** .

### 📜 Sintaxe:

meu_dicionario = {'equipamento': 'Bomba', 'status': 'Ativo', 'horas': 1200}

### 🛠️ Métodos comuns:

* `keys()`: retorna as chaves.
* `values()`: retorna os valores.
* `items()`: retorna pares (chave, valor).
* `get()`: acessa valores com segurança.

### 📌 Uso típico:

Para representar entidades com atributos, como um equipamento e suas propriedades.

---

## 🔹 Tupla (`tuple`)

### 📌 Características:

* Ordenada.
* Imutável (não pode ser modificada após a criação).
* Permite elementos duplicados.
* Tipos mistos são permitidos.

### 📜 Sintaxe:

minha_tupla = (10, 'motor', 3.5)

### 🛠️ Métodos comuns:

* `count()`: conta quantas vezes um valor aparece.
* `index()`: retorna o índice de um valor.

### 📌 Uso típico:

Para representar conjuntos fixos de dados, como coordenadas ou configurações que não devem ser alteradas.

---

## 🔹 Conjunto (`set`)

### 📌 Características:

* Não ordenado.
* Mutável.
* **Não permite valores duplicados** .
* Tipos mistos permitidos (desde que sejam hashables).

### 📜 Sintaxe:

meu_set = {1, 2, 3, 'equipamento'}

### 🛠️ Métodos comuns:

* `add()`: adiciona um elemento.
* `remove()`: remove um elemento.
* `union()`: união de conjuntos.
* `intersection()`: interseção entre conjuntos.
* `difference()`: diferença entre conjuntos.

### 📌 Uso típico:

Para armazenar itens únicos, como códigos únicos de inspeção ou operadores distintos em um turno.

---

## 📊 Comparativo Geral

| Estrutura   | Ordenada  | Mutável | Duplicados  | Tipos Mistos  | Uso Principal                  |
| ----------- | --------- | -------- | ----------- | ------------- | ------------------------------ |
| Lista       | ✅        | ✅       | ✅          | ✅            | Sequências flexíveis         |
| Dicionário | ✅ (3.7+) | ✅       | ❌ (chaves) | ✅            | Pares chave:valor              |
| Tupla       | ✅        | ❌       | ✅          | ✅            | Dados imutáveis e fixos       |
| Set         | ❌        | ✅       | ❌          | ✅ (hashable) | Conjuntos únicos de elementos |
