import random
from termcolor import colored
vidas = 6
alfabeto = {'a': '🄰', 'b':'🄱', 'c':'🄲','d':'🄳','e':'🄴','f':'🄵','g':'🄶','h':'🄷','i':'🄸','j':'🄹','k':'🄺','l':'🄻','m':'🄼','n':'🄽','o':'🄾','p':'🄿','q':'🅀','r':'🅁','s':'🅂','t':'🅃','u':'🅄','v':'🅅','x':'🅇','z':'🅉'}
disponiveis = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z']

def instrucoes():
    print('\n\n', '-'*40, ' ▇▇▇▓▒░ 「 TERMO 」 ░▒▓▇▇▇ ', '-'*40,'\n')
    print('INSTRUÇÕES:')
    print('Descubra a palavra certa em 6 tentativas. Depois de cada tentativa, as peças mostram o quão perto você está da solução.\n')
    print(colored('T','green'),'U R M A')
    print('A letra', colored('T','green'), 'faz parte da palavra e está na posição correta\n')
    print('V I', colored('O','cyan'), 'L A')
    print('A letra', colored('O','cyan'), 'faz parte da palavra mas em outra posição\n')
    print('-'*110,'\n'*3)
    
                                                                    

def escolher_palavra():
    arquivo = open('termo.txt','r')
    arquivo = arquivo.read()
    lista = arquivo.split('\n')
    index = random.randint(0,len(lista))
    palavra = lista[index-1]
    return palavra



instrucoes()
palavra = escolher_palavra()
print(' '*28, end='')
for i in range(5):
    print('【   】 ', end='')
palavra_lista = list(palavra)
letras = set(palavra_lista)





while True:
    if vidas <=0:
        print('\n'*50, ' '*20,'Você perdeu todas as tentaivas')
        print(' '*25,f' A palavra era {palavra.upper()}','\n'*5)
        break
    
    while True:
        jogada = input('\nJOGADA: ').lower()
        if jogada.isdigit():
            print(colored('jogada inválida','red'))
        elif len(jogada) != 5:
             print(colored('jogada inválida','red'))
        elif 'w' in jogada or 'y' in jogada:
            print(colored('jogada inválida','red'))
        
        else:
            break
    
    print('\n\n')
    print(' '*28, end='')
    for i in range(5):
        
        if palavra[i] == jogada[i]:
            print('【',colored(f'{jogada[i].upper()}','green'),'】 ', end='')
            
           
        elif jogada[i] in letras:
            print('【',colored(f'{jogada[i].upper()}','cyan'),'】 ', end='')
            
        
        else:
             print(f'【 {jogada[i].upper()} 】 ', end='')
             try:
                 disponiveis.remove(jogada[i])
             except ValueError:
                pass
             
    if palavra == jogada:
            print('\n\nVOCÊ ACERTOU!')
            break
    else:
        vidas -= 1

    print('\n\n')
    print('彡[ʟᴇᴛʀᴀꜱ ᴅɪꜱᴘᴏɴɪᴠᴇɪꜱ]彡')
    print(' '*50)
    
    for i in disponiveis:
        print(f' {alfabeto[i]} ', end = '')

