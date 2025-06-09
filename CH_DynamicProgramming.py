### INTEGRANTES ###

# RM 557709 - Augusto Ferreira Rogel de Souza
# RM 554823 - Heitor Anderson Prestes de Oliveira Filho
# RM 556668 - Lucca Ribeiro Cardinale
# RM 554445 - Mohamed Afif
# RM 554736 - Rafael Federici de Oliveira

### BIBLIOTECAS ###

import pandas as pd # Biblioteca usada para criar e exibir tabelas
from datetime import datetime # Biblioteca para tratar datas

### FUNÇÕES ###

# Função para inputs com validação de opções pré-definidas
def inputOpcoes(msg, opcoes):
    opcoes_str = ' | '.join(opcoes)
    while True:
        escolha = input(f'\nOPÇÕES -> [ {opcoes_str} ]\n\n{msg}')
        if escolha in opcoes:
            return escolha
        print('\n > Opção Inválida!!! \n')

# Função para entrada de valores numéricos do tipo float
def inputNum(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except ValueError:
            print('\n > Você deve digitar um valor numérico!!! \n')

# Função para entrada de valores numéricos do tipo inteiro
def inputInt(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print('\n > Você deve digitar um valor inteiro!!! \n')

# Função para entrada de datas no formato 'dd/mm/aaaa'
def inputData(msg):
    while True:
        try:
            data = input(msg)
            data = datetime.strptime(data, '%d/%m/%Y') # Converte a string em objeto datetime
            return data.strftime('%d/%m/%Y') # Retorna a data formatada
        except ValueError:
            print('\n > Formato de data invalido!!! \n')

# Função que valida se um valor inserido existe em uma lista de chaves do dicionário
def inputDic(msg, dic, chave):
    while True:
        key = input(msg)
        if key in [str(i) for i in dic[chave]]:
            return key
        print('\n > Digite uma opção existente \n')

# Função que procura e retorna o indice do maior elemento de uma lista
def maiorElementoLista(lista):
    maior = 0
    maior_elemento = lista[maior]
    for i in range(len(lista)):
        if lista[i] > maior_elemento:
            maior_elemento = lista[i]
            maior = i
    return maior

# Função que procura e retorna o indice do menor elemento de uma lista
def menorElementoLista(lista):
    indice_menor = 0
    menor_elemento = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor_elemento:
            menor_elemento = lista[i]
            indice_menor = i
    return indice_menor

# Função de busca binária em uma lista ordenada
# Em comparação ao uso de .index(), que faz uma busca linear O(n), a buscaBinaria() tem uma melhor eficiência O(log n).
def buscaBinaria(lista, num):
    ini = 0
    fim = len(lista) - 1
    while ini <= fim:
        i_chute = (ini + fim) // 2
        chute = lista[i_chute]
        if chute == num:
            return i_chute
        if chute > num:
            fim = i_chute - 1
        else:
            ini = i_chute + 1
    return -1

# Função que exibe o dicionário em formato de tabela usando o pandas
def visualizarTabela(dic):
    df = pd.DataFrame(dic)
    print(f'\n{df.to_string(index = False)}\n')
    return

### VARIÁVEIS GLOBAIS ###

# Dicionário principal com os dados do estoque de insumos
insumos = {
    'ID' : [],
    'Nome_Insumo' : ['Adrenalina', 'Dipirona', 'Gaze Esteril', 'Luvas Cirurgicas' , 'Mascaras N95', 'Seringas'],
    'Estoque' : [500, 1000, 3000, 2000, 300, 4000],
    'Estoque_Ideal' : [1000, 3000, 5000, 5000, 1000, 5000],
    'Custo_Unitario' : [5, 1.3, 0.4, 0.8, 4.3, 0.4]
}

# Preenche o campo ID com valores sequenciais
insumos['ID'] = [i for i, _ in enumerate(insumos['Nome_Insumo'])]

# Dicionário que define qual tipo de entrada de cada campo
tipos = {
    'Nome_Insumo' : input,
    'Estoque' : inputInt,
    'Estoque_Ideal' : inputInt,
    'Custo_Unitario' : inputNum
}

# Opções disponíveis no menu principal
opcoes_menu = ['0', '1', '2', '3', '4', '5', '6', '7']

### CODIGO ###

while True: # Laço principal do sistema com menu de navegação
    print('\n----- Estoque -----\n\n'
          '1 - ADICIONAR NOVO insumo ao estoque \n'
          '2 - ADICIONAR QUANTIDADE de insumo EXISTENTE ao estoque \n'
          '3 - CONSULTAR dados de insumo no estoque \n'
          '4 - ATUALIZAR dados de insumo no estoque \n'
          '5 - LISTAR insumos por QUANTIDADE no estoque \n'
          '6 - EXCLUIR dados de insumo no estoque \n'
          '7 - RETIRAR insumo do estoque \n'
          '0 - SAIR do sistema')
    
    # Escolha da opção do menu
    opcao = inputOpcoes('Escolha uma opção: ', opcoes_menu)

    match opcao:
        case '1':
            input('\n1\nPressione qualquer tecla para voltar... ')
        case '2':
            input('\n2\nPressione qualquer tecla para voltar... ')
        case '3':
            input('\n3\nPressione qualquer tecla para voltar... ')
        case '4':
            input('\n4\nPressione qualquer tecla para voltar... ')
        case '5':
            input('\n5\nPressione qualquer tecla para voltar... ')
        case '6':
            input('\n6\nPressione qualquer tecla para voltar... ')
        case '7':
            input('\n7\nPressione qualquer tecla para voltar... ')
        case '0': # Saida do sistema
            print('\n > SISTEMA FECHADO... \n')
            break