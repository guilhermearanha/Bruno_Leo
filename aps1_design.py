import sys
#sys.exit()

import random

#sorteio dado 1 e 2 "Come Out"
def d1():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    soma = x + y
    return soma

#fichas iniciais
fichas = 100

pergunta = input("Você quer apostar?")

if pergunta == "sim" or pergunta == "s":

    print("Início da rodada: fase Come Out")

    jogo = input("Qual tipo de aposta você deseja fazer? Pass Line Bet/ Field/ Any Craps/ Twelve")

    #Pass Line Bet(disponível apenas na rodada Come Out): Se a soma dos dados for 7 ou 11, você ganha a mesma quantidade de fichas que apostou. Já se a soma dos dados for 2, 3 ou 12(Craps), você perde tudo. Agora, caso a soma dos dados de 4, 5, 6, 8, 9 ou 10, você avança para a proxima fase: fase Point.
    #Field(disponível em qual fase do jogo): Se a soma der 5, 6, 7 ou 8, o jogador perde tudo. Já se a soma der 3, 4, 9, 10, ou 11, o jogador ganha o mesmo valor que apostou.
    #Any Craps(disponível em qual fase do jogo): Se a soma der 2, 3 ou 12, o jogador ganha 7 vezes o valor de sua aposta. Caso o contrário, ele perde tudo que apostou.
    #Twelve(disponível em qual fase do jogo): Se a soma der 12, o jogador ganha 30 o valor de sua aposta. Caso o contrário, ele perde tudo.
    
    if jogo == "Pass Line Bet":
#Pass Line Bet(disponível apenas na rodada Come Out): Se a soma dos dados for 7 ou 11, você ganha a mesma quantidade de fichas que apostou. Já se a soma dos dados for 2, 3 ou 12(Craps), você perde tudo. Agora, caso a soma dos dados de 4, 5, 6, 8, 9 ou 10, você avança para a proxima fase: fase Point.
        aposta = int(input("Quanto você quer apostar?"))
        
        if soma == 7 or soma == 11:
            fichas += aposta
        elif soma == 2 or soma == 3 or soma == 12: #Craps
            fichas -= aposta
        elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
            print("Início da fase Point")
            soma_anterior = soma
            while a = False:
                d1()
                if soma_anterior == soma:
                    fichas += aposta
                    a = True
                elif soma == 7:
                    ficha -= aposta
                    a = True
                else:
        print("Você tem {0}".format(fichas))
         
    elif jogo == "Field":
#Field(disponível em qual fase do jogo): Se a soma der 5, 6, 7 ou 8, o jogador perde tudo. Já se a soma der 3, 4, 9, 10, ou 11, o jogador ganha o mesmo valor que apostou.
        aposta = int(input("Quanto você quer apostar?"))
        if soma == 5 or soma == 6 or soma == 7 or soma == 8:
            fichas -= aposta
        elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
            fichas += aposta
        elif:
            fichas += aposta*2
        else:
            fichas += aposta*3
    print("Você tem {0}".format(fichas))

    elif jogo == "Any Craps":
#Any Craps(disponível em qual fase do jogo): Se a soma der 2, 3 ou 12, o jogador ganha 7 vezes o valor de sua aposta. Caso o contrário, ele perde tudo que apostou.
        aposta = int(input("Quanto você quer apostar?"))
        if soma == 2 or soma == 3 or soma == 12:
            fichas += aposta*7
        else:
            fichas -= aposta
    print("Você tem {0}".format(fichas))
    elif jogo == "Twelve":
#Twelve(disponível em qual fase do jogo): Se a soma der 12, o jogador ganha 30 o valor de sua aposta. Caso o contrário, ele perde tudo.
        if soma == 12:
            fichas += aposta*30
        else:
            soma -= aposta
else:
    print("O jogo acabou.")