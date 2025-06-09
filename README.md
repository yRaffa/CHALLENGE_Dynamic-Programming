# **🌐 FIAP x DASA CHALLENGE 2025**

# 🐍 Dynamic Programing (2ESA)

## 👥 Integrantes

- RM 557709 - Augusto Ferreira Rogel de Souza
- RM 554823 - Heitor Anderson Prestes de Oliveira Filho
- RM 556668 - Lucca Ribeiro Cardinale
- RM 554445 - Mohamed Afif
- RM 554736 - Rafael Federici de Oliveira

## 📕 Sobre o Projeto

### 📦 Sistema de Gerenciamento de Estoque de Insumos Médicos

Este sistema foi desenvolvido em [Python](https://www.python.org/doc/) com o objetivo de gerenciar estoques de insumos médicos. Ele funciona inteiramente via terminal e utiliza estruturas de dados simples (dicionários com listas), além da biblioteca [Pandas](https://pandas.pydata.org/) para exibição organizada dos dados em formato de tabela.

## 🧩 Funcionalidades Principais

### 🔸 Visualizar Estoque

Exibe todos os insumos cadastrados em formato de tabela.

### 🔸 Adicionar Novo Insumo

Permite o cadastro de um novo insumo no estoque, solicitando os seguintes dados:
- Nome do Insumo
- Quantidade em Estoque
- Estoque Ideal
- Custo Unitário

### 🔸 Adicionar Quantidade a Insumo Existente

Incrementa a quantidade de um insumo já cadastrado no estoque.

### 🔸 Consultar Dados de Insumo

Mostra os dados detalhados de um insumo específico, selecionado por ID.

### 🔸 Atualizar Dados de Insumo

Permite alterar os dados de um insumo já registrado, seja todos os campos ou apenas um específico.

### 🔸 Listar Insumos por Quantidade

Exibe os insumos ordenados pela quantidade em estoque, do menor para o maior.

### 🔸 Excluir Insumo

Remove completamente um insumo do estoque com base no ID.

### 🔸 Retirar Quantidade do Estoque

Reduz a quantidade de um insumo no estoque, garantindo que não haja valores negativos.

### 🔸 Reabastecer Estoque

Automaticamente reabastece os insumos que estão abaixo do estoque ideal, gerando um relatório com o custo total.

### 🔸 Sair do Sistema

Encerra o programa de maneira segura.

## 🧠 Estrutura do Código

### 🔹 Funções de Input Personalizado

Estas funções ajudam a garantir que os dados inseridos estejam no formato correto:

``` inputOpcoes(): ``` Valida opções pré-definidas.

``` inputNum(): ``` Garante que seja inserido um número decimal (float).

``` inputInt(): ``` Garante que seja inserido um número inteiro.

``` inputDic(): ``` Valida se um valor existe em uma lista de chaves do dicionário. 

### 🔹 Busca Binária

``` buscaBinaria(): ``` Localiza rapidamente o índice de um ID na lista. A lista deve estar ordenada, como é o caso da lista de IDs.

Em comparação ao uso de ``` .index() ```, que faz uma busca linear **O(n)**, a ``` buscaBinaria() ``` tem uma melhor eficiência **O(log n)**.

### 🔹 Ordenação por Selection Sort

``` selectionSort(): ``` Ordena os insumos com base na quantidade em estoque, utilizando o algoritmo de ordenação por seleção.

### 🔹 Visualização com Pandas

``` visualizarTabela(): ``` Converte o dicionário em um DataFrame do [Pandas](https://pandas.pydata.org/) e imprime de formato de tabela.

### 🔹 Operações com o Dicionário

Essas funções manipulam os dados principais do sistema:

``` adicionar(): ``` Adiciona novos insumos ao estoque.

``` consultar(): ``` Consulta e exibe dados de um insumo específico.

``` atualizar(): ``` Atualiza dados de um insumo no estoque.

``` excluir(): ``` Remove todos os dados de um insumo do estoque.

``` adicionarQuantidade(): ``` Incrementa a quantidade de estoque de um insumo.

``` retirarQuantidade(): ``` Reduz a quantidade de estoque de um insumo.

``` reabastecerEstoque(): ``` Reabastece automaticamente os insumos abaixo do estoque ideal.

## 🎲 Estrutura dos Dados

Os dados dos insumos são armazenados no dicionário ``` insumos ```, onde cada chave representa um campo (coluna), e os valores são listas (linhas).

``` python
insumos = {
    'ID' : [0, 1, 2, 3, 4, 5],
    'Nome_Insumo' : ['Adrenalina', 'Dipirona', 'Gaze Esteril', 'Luvas Cirurgicas' , 'Mascaras N95', 'Seringas'],
    'Estoque' : [500, 1000, 3000, 2000, 300, 4000],
    'Estoque_Ideal' : [1000, 3000, 5000, 5000, 1000, 5000],
    'Custo_Unitario' : [5.00, 1.30, 0.40, 0.80, 4.30, 0.40]
}
```

O campo ``` 'ID' ``` é usado como chave primária para buscas e operações.

## 📌 Tabela de Tipos

O dicionário ``` tipos ``` define o tipo de input esperado para cada campo:

``` python
tipos = {
    'Nome_Insumo' : input,
    'Estoque' : inputInt,
    'Estoque_Ideal' : inputInt,
    'Custo_Unitario' : inputNum
}
```

## 📄 Documentação de Código

### 🔺 Hipóteses e Dados Considerados

**1. Eficiência em Busca:**

> A busca binária foi implementada para melhorar a eficiência na localização de insumos por ID, reduzindo a complexidade de O(n) para O(log n).

**2. Ordenação por Selection Sort:**

> O algoritmo de ordenação por seleção foi escolhido para ordenar os insumos por quantidade, garantindo uma implementação simples e eficaz para pequenos conjuntos de dados.

**3. Reabastecimento Automático:**

> A função ``` reabastecerEstoque() ``` verifica automaticamente os insumos abaixo do estoque ideal e calcula o custo total do reabastecimento, simulando um processo real de gestão de estoque.

**4. Validação de Entradas:**

> Todas as funções de input possuem validação para garantir que os dados inseridos estejam no formato correto, evitando erros durante a execução.

**5. Dicionário como Estrutura Principal:**

> O uso de dicionários com listas permite uma organização clara dos dados, facilitando operações de adição, consulta, atualização e exclusão.

**6. Uso do Pandas para Visualização:**

> A biblioteca Pandas foi utilizada para exibir os dados de forma tabular, melhorando a legibilidade e a experiência do usuário.

## 🔎 Conclusão

Este projeto demonstra a aplicação de conceitos de programação dinâmica, estruturas de dados e algoritmos de busca e ordenação em um contexto prático de gerenciamento de estoque.

## ▶️ Como Usar

- Execute o código em um terminal Python.
- Um menu será exibido com as opções principais.
- Digite o número da operação desejada.
- Siga as instruções no terminal para preencher ou visualizar os dados.

## ⚠️ Observação

O código utiliza validação básica de entrada, mas não possui persistência de dados. Ao encerrar o programa, os dados são perdidos.