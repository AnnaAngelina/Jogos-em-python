import os
import csv
import random
from colorama import Fore, Back, Style


lim = True
linhas_caract = []
colunas_caract = []
jogadores = 1
jogadas = 0

def limpartela():
    os.system('cls')

def dadosconver(registro):
    dado = []
    with open(registro, mode='r', encoding='utf-8') as arquivo_csv:
        arquivo_csv = csv.DictReader(arquivo_csv, delimiter=',')
        for i in arquivo_csv:
            dado.append(i)
    return dado

def atualizar(registro, dado):
    cabecalho = dado[0].keys()
    with open(registro, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        arquivo_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalho, delimiter=',')
        arquivo_csv.writeheader()
        for i in dado:
            arquivo_csv.writerow(i)

def jogadores_name(dado):
    lim = 0
    global jogador1, jogador2
    jogador1 = input('Digite o nome do Jogador 1: ')
    for linha in dado:
        if str(linha['nome']).upper() == jogador1.upper():
            lim = 1
            print(f'Bem vindo(a) {jogador1}')
    if lim == 0:
        esc = input('Parece que você não está cadastrado(a).\nVocê deseja fazer o cadastro ou entrar sem conta? ')
        if esc.upper() == 'FAZER CADASTRO':
            limpartela()
            nome = input('Digite seu nome: ')
            novo = {'nome': nome, 'vitorias': 0}
            dado.append(novo)
            limpartela()
        elif esc.upper() == 'Entrar sem conta':
            limpartela()
            num = random.randint(10,99)
            nome = 'usuario' + str(num)
            novo = {'nome': nome, 'vitorias': 0}
            dado.append(novo)

    jogador2 = input('Digite o nome do jogador 2: ')
    for linha in dado:
        if str(linha['nome']).upper() == jogador2.upper():
            lim = 1
            print(f'Bem vindo(a) {jogador2}')
    if lim == 0:
        esc = input('Parece que você não está cadastrado(a).\nVocê deseja fazer o cadastro ou entrar sem conta? ')
        if esc.upper() == 'FAZER CADASTRO':
            limpartela()
            nome = input('Digite seu nome: ')
            novo = {'nome': nome, 'vitorias': 0}
            dado.append(novo)
            limpartela()
        elif esc.upper() == 'Entrar sem conta':
            limpartela()
            num = random.randint(10,99)
            nome = 'usuario' + str(num)
            novo = {'nome': nome, 'vitorias': 0}
            dado.append(novo)
    return jogador1, jogador2

def jogadorunic_name(dado):
    unic_jogador = input('Digite seu nome: ')
    for linha in dado:
        if str(linha['nome']).upper() == unic_jogador.upper():
            lim = 1
            print(f'Bem vindo(a) {unic_jogador}')
    if lim == 0:
        esc = input('Parece que você não está cadastrado(a).\nVocê deseja fazer o cadastro ou entrar sem conta? ')
        if esc.upper() == 'FAZER CADASTRO':
            nome = input('Digite seu nome: ')
            novo = {'nome': nome, 'vitorias': 0}
            dado.append(novo)
            limpartela()
        elif esc.upper() == 'Entrar sem conta':
            num = random.randint(10,99)
            nome = 'usuario' + str(num)
            novo = {'nome': nome, 'vitorias': 0}
            dado.append(novo)
    return unic_jogador

def interface():
    print(52* '*')
    print(13* '*' + Fore.BLUE + 'BEM VINDO AO JOGO DA VELHA' + Fore.RESET + 13* '*')
    print(52* '*')
interface()
    
def escolha_jogadores():
    escolha = input('Você deseja jogar no modo single player ou multiplayer?\n')
    return escolha
escolha = escolha_jogadores()
limpartela()

def jogadorunic_name():
    unic_jogador = input('Digite seu nome: ')
    return unic_jogador

linhas_caract = []
colunas_caract = []
jogadores = 2
jogadas = 0
vitoriaj1 = 0
vitoriaj2 = 0

graficos = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']]


def velha():
    print('    0   1   2')
    print('0   ' + graficos[0][0] + ' | ' + graficos[0][1] + ' | ' + graficos[0][2])
    print(' ', 13*'-')
    print('1   ' + graficos[1][0] + ' | ' + graficos[1][1] + ' | ' + graficos[1][2])
    print(' ', 13*'-')
    print('2   ' + graficos[2][0] + ' | ' + graficos[2][1] + ' | ' + graficos[2][2])
    print(13* '-')
    print('jogadas:', jogadas)
    print(13* '-')

def single_player():
    global jogadas
    global jogadores
    lets = []
    linauto = random.randrange(0,3)
    coluauto = random.randrange(0,3)
    if linauto not in lets and coluauto not in lets:
        if jogadores == 2 and jogadas < 9:
            if graficos[linauto][coluauto] == ' ':
                graficos[linauto][coluauto] = 'O'
                jogadas += 1
                jogadores = 1
                lets.append(linauto)
                lets.append(coluauto)
    else:
        linauto = random.randrange(0,3)
        coluauto = random.randrange(0,3) 

def vez_jogador1():
    global jogadas
    global jogadores
    if escolha.upper() == 'MULTIPLAYER':
        print('Vez do(a)', jogador1)
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if jogadores == 1 and jogadas < 9:
        if graficos[linha][coluna] == ' ':
            graficos[linha][coluna] = 'X'
            jogadas += 1
            jogadores = 2
        else:
            print('A coluna', coluna, 'da linha', linha, 'já está ocupada, tente novamente.' )

    velha()


def vez_jogador2():
    global jogadas
    global jogadores
    print('Vez do(a)', jogador2)
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if jogadores == 2 and jogadas < 9:
        if graficos[linha][coluna] == ' ':
            graficos[linha][coluna] = 'O'
            jogadas += 1
            jogadores = 1
        else:
            print('A coluna', coluna, 'da linha', linha, 'já está ocupada, tente novamente.' )
    velha()

def verificar_vitoria1(vitoriaj1, vitoriaj2):
    global lim
    vito = 0
    a = 0
    simb = ['X', 'O']
    for s in simb:
        for row in range(len(graficos)):
            vito = 0
            for i in range(len(graficos[a])):
                if graficos[row][i] == s:
                    vito +=1
            if vito == 3 and s == 'X':
                print(f'Parabéns, o {jogador1} ganhou!')
                vitoriaj1 += 1
                return True
            elif vito == 3 and s == 'O':
                print(f'Parabéns, o {jogador2} ganhou!')
                vitoriaj2 += 1

    for s in range(len(simb)):        
        for row in range(len(graficos)):
            vito = 0
            for i in range(len(graficos[0])):
                if graficos[i][row] == simb[s]:
                    vito +=1
            if vito == 3 and s == 'X':
                print(f'Parabéns, o {jogador1} ganhou!')
                vitoriaj1 += 1
                return True
            elif vito == 3 and s == 'O':
                print(f'Parabéns, o {jogador2} ganhou!')
                vitoriaj2 += 1

    for s in simb:
        vito = 0
        for i in range(len(graficos)):
            if graficos[i][i] == s:
                vito += 1
        if vito == 3 and s == 'X':
            print(f'Parabéns, o {jogador1} ganhou!')
            vitoriaj1 += 1
            return True
        elif vito == 3 and s == 'O':
            print(f'Parabéns, o {jogador2} ganhou!')
            vitoriaj2 += 1
        
    for s in simb:
        vito = 0
        for i in range(len(graficos)):
            if graficos[i][len(graficos) - 1 - i] == s:
                vito += 1
        if vito == 3 and s == 'X':
            print(f'Parabéns, o {jogador1} ganhou!')
            vitoriaj1 += 1
            return True
        elif vito == 3 and s == 'O':
            print(f'Parabéns, o {jogador2} ganhou!')
            vitoriaj2 += 1
    return False

def verificar_vitoria2(vitoriaj1):
    global lim
    vito = 0
    a = 0
    simb = ['X', 'O']
    for s in simb:
        for row in range(len(graficos)):
            vito = 0
            for i in range(len(graficos[a])):
                if graficos[row][i] == s:
                    vito +=1
            if vito == 3:
                if s == 'X':
                    print('Parabéns, você ganhou!')
                    vitoriaj1 += 1
                    return True
                else:
                    print('Você perdeu!')
                    return True

    for s in range(len(simb)):        
        for row in range(len(graficos)):
            vito = 0
            for i in range(len(graficos[0])):
                if graficos[i][row] == simb[s]:
                    vito +=1
            if vito == 3:
                if s == 'X':
                    print('Parabéns, você ganhou!')
                    return True
                else:
                    print('Você perdeu!')
                    return True

    for s in simb:
        vito = 0
        for i in range(len(graficos)):
            if graficos[i][i] == s:
                vito += 1
        if vito == 3:
            if s == 'X':
                print('Parabéns, você ganhou!')
                return True
            else:
                print('Você perdeu!')
                return True
        
    for s in simb:
        vito = 0
        for i in range(len(graficos)):
            if graficos[i][len(graficos) - 1 - i] == s:
                vito += 1
        if vito == 3:
            if s == 'X':
                print('Parabéns, você ganhou!')
                return True
            else:
                print('Você perdeu!')
                return True
    return False

jog_registrados = dadosconver('jogadores.csv')

while True:
    velha
    if escolha.upper() == 'MULTIPLAYER':
        jogador1, jogador2 = jogadores_name(jog_registrados)
        atualizar('jogadores.csv', jog_registrados)
        limpartela()
        vez_jogador2()
        if verificar_vitoria1(vitoriaj1, vitoriaj2):
            break
        vez_jogador1()
        if verificar_vitoria1(vitoriaj1, vitoriaj2):
            break
    else:
        unic_jogador = jogadorunic_name(jog_registrados)
        atualizar('jogadores.csv', jog_registrados)
        limpartela()
        single_player()
        if verificar_vitoria2(vitoriaj1):
            break
        vez_jogador1()
        if verificar_vitoria2(vitoriaj1):
            break
