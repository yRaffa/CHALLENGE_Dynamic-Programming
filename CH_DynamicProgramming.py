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

# Função que adiciona um novo item ao dicionário
def dicAdicionar(dic):
    adicionar_id = max(dic['ID']) + 1 # Gera novo ID automaticamente
    dic['ID'].append(adicionar_id)
    print('\n > ADICIONAR dados de insumo a tabela: \n')
    for key in tipos.keys(): # Pede os dados conforme os tipos definidos
        adicionar = tipos[key](f'{key}: ')
        dic[key].append(adicionar)
    return

# Função que consulta e exibe os dados de um item do dicionário com base no ID informado
def dicConsultar(dic, chave):
    consultar = inputDic('Digite o ID do insumo que deseja CONSULTAR: ', dic, chave)
    # indice_consultar = dic[chave].index(int(consultar)) # Notação O Grande: O(n) (menos eficiente)
    indice_consultar = buscaBinaria(dic[chave], int(consultar)) # Notação O Grande: O(log n) (mais eficiente)
    print('\n > Informações do insumo selecionado: \n')
    for key in dic.keys():
        print(key, end = ': ')
        print(dic[key][indice_consultar])
    return

# Função que atualiza os dados de um item do dicionário com base no ID informado
def dicAtualizar(dic, chave):
    atualizar = inputDic('Digite o ID do insumo que deseja ATUALIZAR: ', dic, chave)
    # indice_atualizar = dic[chave].index(int(atualizar)) # Notação O Grande: O(n) (menos eficiente)
    indice_atualizar = buscaBinaria(dic[chave], int(atualizar)) # Notação O Grande: O(log n) (mais eficiente)
    nome_insumo = dic['Nome_Insumo'][indice_atualizar]
    chaves = list(tipos.keys())
    opcoes_atualizar = list(map(str, range(0, len(chaves) + 1)))
    print('\n > Opções de Atualizações: \n')
    print('0 - Todos os Dados')
    for i, chave_nome in enumerate(chaves, start = 1):
        print(f'{i} - {chave_nome}')
    tipo_atualizar = inputOpcoes(f'Quais dados voce quer ATUALIZAR de {nome_insumo}? ', opcoes_atualizar)
    match tipo_atualizar:
        case '0':  # Atualiza todos os campos
            for key in tipos.keys():
                mudanca = tipos[key](f'Atualizar {key}: ')
                dic[key][indice_atualizar] = mudanca
        case _: # Atualiza campos individuais
            chave_atualizar = chaves[int(tipo_atualizar) - 1]
            mudanca = tipos[chave_atualizar](f'Atualizar {chave_atualizar}: ')
            dic[chave_atualizar][indice_atualizar] = mudanca
    return

# Função que exclui os dados de um item do dicionário com base no ID informado
def dicExcluir(dic, chave):
    excluir = inputDic('Digite o ID do incêndio que deseja EXCLUIR: ', dic, chave)
    # indice_excluir = dic[chave].index(int(excluir)) # Notação O Grande: O(n) (menos eficiente)
    indice_excluir = buscaBinaria(dic[chave], int(excluir)) # Notação O Grande: O(log n) (mais eficiente)
    for key in dic.keys():
        dic[key].pop(indice_excluir) # Remove os dados de todas as colunas para esse índice
    return

# Função que adiciona quantidade a um item do dicionário
def dicAdicionarQuantidade(dic, chave):
    adicionar = inputDic('Digite o ID do insumo que deseja ADICIONAR QUANTIDADE ao estoque: ', dic, chave)
    # indice_adicionar = dic[chave].index(int(adicionar)) # Notação O Grande: O(n) (menos eficiente)
    indice_adicionar = buscaBinaria(dic[chave], int(adicionar)) # Notação O Grande: O(log n) (mais eficiente)
    nome_insumo = dic['Nome_Insumo'][indice_adicionar]
    quantidade = inputInt(f'Digite a quantidade que deseja adicionar ao insumo {nome_insumo}: ')
    dic['Estoque'][indice_adicionar] += quantidade
    return

def dicListarQuantidade(dic, chave):
    return

def dicRetirarQuantidade(dic, chave):
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
opcoes_menu = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

### CODIGO ###

while True: # Laço principal do sistema com menu de navegação
    print('\n----- Estoque -----\n\n'
          '1 - VISUALIZAR estoque de insumos \n'
          '2 - ADICIONAR dados de um NOVO insumo ao estoque \n'
          '3 - ADICIONAR QUANTIDADE de insumo EXISTENTE ao estoque \n'
          '4 - CONSULTAR dados de insumo no estoque \n'
          '5 - ATUALIZAR dados de insumo no estoque \n'
          '6 - LISTAR insumos por QUANTIDADE no estoque \n'
          '7 - EXCLUIR dados de insumo no estoque \n'
          '8 - RETIRAR insumo do estoque \n'
          '0 - SAIR do sistema')
    
    # Escolha da opção do menu
    opcao = inputOpcoes('Escolha uma opção: ', opcoes_menu)

    match opcao:
        case '1':
            visualizarTabela(insumos)
            input('\nPressione qualquer tecla para voltar... ')
        case '2':
            dicAdicionar(insumos)
            input('\nNOVOS Dados foram ADICIONADOS!!!\nPressione qualquer tecla para voltar... ')
        case '3':
            visualizarTabela(insumos)
            dicAdicionarQuantidade(insumos, 'ID')
            input('\nQUANTIDADE de estoque ADICIONADA!!!\nPressione qualquer tecla para voltar... ')
        case '4':
            visualizarTabela(insumos)
            dicConsultar(insumos, 'ID')
            input('\nDados CONSULTADOS!!!\nPressione qualquer tecla para voltar... ')
        case '5':
            visualizarTabela(insumos)
            dicAtualizar(insumos, 'ID')
            input('\nDados ATUALIZADOS!!!\nPressione qualquer tecla para voltar... ')
        case '6':
            visualizarTabela(insumos)
            dicListarQuantidade(insumos, 'ID')
            input('\nInsumos LISTADOS!!!\nPressione qualquer tecla para voltar... ')
        case '7':
            visualizarTabela(insumos)
            dicExcluir(insumos, 'ID')
            input('\nDados EXCLUIDOS!!!\nPressione qualquer tecla para voltar... ')
        case '8':
            visualizarTabela(insumos)
            dicRetirarQuantidade(insumos, 'ID')
            input('\nInsumos RETIRADOS!!!\nPressione qualquer tecla para voltar... ')
        case '0': # Saida do sistema
            print('\n > SISTEMA FECHADO... \n')
            break