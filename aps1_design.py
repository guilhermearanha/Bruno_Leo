import sys
#sys.exit()

import random

#sorteio dado 1 e 2 "Come Out"

soma = 0

def d1():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    soma = x + y
    return soma
soma = d1()

#fichas iniciais
fichas = 100
print("Você tem: 100 fichas")
print("Para desistir do jogo a qualquer momento, escreva (desligar)"

pergunta = input("Você quer apostar?")

if pergunta == "desligar":
    print("O jogo acabou!")

while pergunta == "sim" or pergunta == "s" or pergunta == "Sim" or fichas != 0 and pergunta != "desligar":

    print("Início da rodada.")
    print("Você tem: {0} fichas".format(fichas))

    jogo = input("Qual tipo de aposta você deseja fazer? Pass Line Bet / Field / Any Craps / Twelve:")
    
    #Pass Line Bet(disponível apenas na rodada Come Out): Se a soma dos dados for 7 ou 11, você ganha a mesma quantidade de fichas que apostou. Já se a soma dos dados for 2, 3 ou 12(Craps), você perde tudo. Agora, caso a soma dos dados de 4, 5, 6, 8, 9 ou 10, você avança para a proxima fase: fase Point.
    #Field(disponível em qual fase do jogo): Se a soma der 5, 6, 7 ou 8, o jogador perde tudo. Já se a soma der 3, 4, 9, 10, ou 11, o jogador ganha o mesmo valor que apostou.
    #Any Craps(disponível em qual fase do jogo): Se a soma der 2, 3 ou 12, o jogador ganha 7 vezes o valor de sua aposta. Caso o contrário, ele perde tudo que apostou.
    #Twelve(disponível em qual fase do jogo): Se a soma der 12, o jogador ganha 30 o valor de sua aposta. Caso o contrário, ele perde tudo.
    
    if jogo == "Pass Line Bet" or jogo == "pass line bet":
#Pass Line Bet(disponível apenas na rodada Come Out): Se a soma dos dados for 7 ou 11, você ganha a mesma quantidade de fichas que apostou. Já se a soma dos dados for 2, 3 ou 12(Craps), você perde tudo. Agora, caso a soma dos dados de 4, 5, 6, 8, 9 ou 10, você avança para a proxima fase: fase Point.
        
        aposta = int(input("Quanto você quer apostar?"))
        
        d1()
        print("A soma deu {0}".format(soma))

        if soma == 7 or soma == 11:
            fichas += aposta
        elif soma == 2 or soma == 3 or soma == 12: #Craps
            fichas -= aposta
        elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
            print("Início da fase Point")
            #colar aqui
        elif aposta == "desligar":
            print("O jogo acabou!")

    fichas == fichas
         
    if jogo == "Field" or jogo == "field":
#Field(disponível em qual fase do jogo): Se a soma der 5, 6, 7 ou 8, o jogador perde tudo. Já se a soma der 3, 4, 9, 10, ou 11, o jogador ganha o mesmo valor que apostou.
        
        aposta = int(input("Quanto você quer apostar?"))
        
        d1()
        print("A soma deu {0}".format(soma))

        if soma == 5 or soma == 6 or soma == 7 or soma == 8:
            fichas -= aposta
        elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
            fichas += aposta
        elif soma == 2:
            fichas += aposta*2
        elif soma == 12:
            fichas += aposta*3
        elif aposta == "desligar":
            print("O jogo acabou!")

    fichas == fichas

    if jogo == "Any Craps" or jogo == "any craps":
#Any Craps(disponível em qual fase do jogo): Se a soma der 2, 3 ou 12, o jogador ganha 7 vezes o valor de sua aposta. Caso o contrário, ele perde tudo que apostou.
        
        aposta = int(input("Quanto você quer apostar?"))
        
        d1()
        print("A soma deu {0}".format(soma))

        if soma == 2 or soma == 3 or soma == 12:
            fichas += aposta*7
        elif aposta == "desligar":
            print("O jogo acabou!")
        else:
            fichas -= aposta

    fichas == fichas

    if jogo == "Twelve" or jogo == "twelve":
#Twelve(disponível em qual fase do jogo): Se a soma der 12, o jogador ganha 30 o valor de sua aposta. Caso o contrário, ele perde tudo.
        
        aposta = int(input("Quanto você quer apostar?"))
        
        d1()
        print("A soma deu {0}".format(soma))

        if soma == 12:
            fichas += aposta*30
        elif aposta == "desligar":
            print("O jogo acabou!")
        else:
            fichas -= aposta
        
    fichas == fichas

    print("Você tem: {0} fichas".format(fichas))

    if jogo != "Pass Line Bet" or jogo != "pass line bet" or jogo != "Field" or jogo != "field" or jogo != "Any Craps" or jogo != "any craps" or jogo != "Twelve" or jogo != "twelve":
        print("Digite o nome do jogo corretamente.")

else:
    print("O jogo acabou!")

    #colar lá
    # soma_anterior = soma
    #         while a =False:
    #             d1()
    #             if soma_anterior == soma:
    #                 fichas += aposta
    #                 a = True
    #             elif soma == 7:
    #                 ficha -= aposta
    #                 a = True
    #             else: