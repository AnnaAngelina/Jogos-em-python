import os
import random
from colorama import Fore, Back, Style

lim = True
linhas_caract = []
colunas_caract = []
jogadores = 1
jogadas = 0

def limpartela():
    os.system('cls')

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

def jogadores_name():
    jogador1 = input('Digite o nome do Jogador 1: ')
    jogador2 = input('Digite o nome do jogador 2: ')
    return jogador1, jogador2

def jogadorunic_name():
    unic_jogador = input('Digite seu nome: ')
    return unic_jogador

linhas_caract = []
colunas_caract = []
jogadores = 2
jogadas = 0

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
            print('oi')
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

def verificar_vitoria1():
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
                print(f'Parabéns, o {jogador1 if s == "X" else jogador2} ganhou!')
                return True

    for s in range(len(simb)):        
        for row in range(len(graficos)):
            vito = 0
            for i in range(len(graficos[0])):
                if graficos[i][row] == simb[s]:
                    vito +=1
            if vito == 3:
                print(f'Parabéns, o {jogador1 if s == "X" else jogador2} ganhou!')
                return True

    for s in simb:
        vito = 0
        for i in range(len(graficos)):
            if graficos[i][i] == s:
                vito += 1
        if vito == 3:
            print(f'Parabéns, o {jogador1 if s == "X" else jogador2} ganhou!')
            return True
        
    for s in simb:
        vito = 0
        for i in range(len(graficos)):
            if graficos[i][len(graficos) - 1 - i] == s:
                vito += 1
        if vito == 3:
            print(f'Parabéns, o {jogador1 if s == "X" else jogador2} ganhou!')
            return True
    return False

def verificar_vitoria2():
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

while True:
    velha
    if escolha.upper() == 'MULTIPLAYER':
        jogador1, jogador2 = jogadores_name()
        limpartela()
        vez_jogador2()
        if verificar_vitoria1():
            break
        vez_jogador1()
        if verificar_vitoria1():
            break
    else:
        unic_jogador = jogadorunic_name()
        limpartela()
        single_player()
        if verificar_vitoria2():
            break
        vez_jogador1()
        if verificar_vitoria2():
            break
