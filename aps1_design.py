import sys
#sys.exit()

import random

#sorteio dado 1 e 2 "Come Out"
def d1():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    soma1 = x + y
    return soma1

#sorteio dado 1 e 2 "Point"
def d2():
    w = random.randint(1, 6)
    f = random.randint(1, 6)
    soma2 = w + f
    return soma2


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

        aposta = int(input("Quanto você quer apostar?"))
        
        if soma1 == 7 or soma1 == 11:
            fichas += aposta
        if soma1 == 2 or soma1 == 3 or soma1 == 12: #Craps
            fichas -= aposta
        if soma1 == 4 or soma1 == 5 or soma1 == 6 or soma1 == 8 or soma1 == 9 or soma1 == 10:
            print("Início da fase Point")


    if jogo == "Field":

else:
    print("O jogo acabou.")