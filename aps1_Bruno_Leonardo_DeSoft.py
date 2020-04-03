import random

soma = 0
soma2 = 0

gameon = False

#fichas iniciais
fichas = 100
aposta = 0

print('Regras do Jogo:')
print('  ')
print('1-É permitido apenas apostas com números inteiros.')
print('  ')
print('2-Não é permitido sair do jogo durante a fase de apostas (caso não seja a fase de apostas, para sair do jogo basta escrever "desligar").')
print('  ')
print('Serão jogados dois dados, e a soma dos dois dados dará rumo ao jogo. Esses são os tipos de aposta possíveis:')
print('  ')
print('Pass Line Bet(disponível apenas na rodada Come Out): Se a soma dos dados for 7 ou 11, você ganha a mesma quantidade de fichas que apostou. Já se a soma dos dados for 2, 3 ou 12(Craps), você perde tudo. Agora, caso a soma dos dados de 4, 5, 6, 8, 9 ou 10, você avança para a próxima fase: fase Point.')
print('  ')
print('Field(disponível em qual fase do jogo): Se a soma der 5, 6, 7 ou 8, o jogador perde tudo. Já se a soma der 3, 4, 9, 10, ou 11, o jogador ganha o mesmo valor que apostou.')
print('  ')
print('Any Craps(disponível em qual fase do jogo): Se a soma der 2, 3 ou 12, o jogador ganha 7 vezes o valor de sua aposta. Caso o contrário, ele perde tudo que apostou.')
print('  ')
print('Twelve(disponível em qual fase do jogo): Se a soma der 12, o jogador ganha 30 o valor de sua aposta. Caso o contrário, ele perde tudo.')
print('  ')
print("Você tem: 100 fichas")


pergunta = input("Você quer começar o jogo? (sim/não)")

if pergunta == "sim" or pergunta == "s" or pergunta == "Sim":
    gameon = True

while gameon == True and fichas != 0:
    print('  ')
    print('---------------------------')
    print("Início da rodada.")

    jogo = input("Qual tipo de aposta você deseja fazer? Pass Line Bet / Field / Any Craps / Twelve:")
    
    if jogo == 'desligar' or jogo == 'Desligar':
        gameon = False
    if jogo != "Pass Line Bet" and jogo != "pass line bet" and jogo != "Field" and jogo != "field" and jogo != "Any Craps" and jogo != "any craps" and jogo != "Twelve" and jogo != "twelve" and jogo != 'desligar' and jogo != 'Desligar':
        print("Digite o nome do jogo corretamente.")
    
    if jogo == "Pass Line Bet" or jogo == "pass line bet":
#Pass Line Bet(disponível apenas na rodada Come Out): Se a soma dos dados for 7 ou 11, você ganha a mesma quantidade de fichas que apostou. Já se a soma dos dados for 2, 3 ou 12(Craps), você perde tudo. Agora, caso a soma dos dados de 4, 5, 6, 8, 9 ou 10, você avança para a proxima fase: fase Point.

        aposta = int(input("Quanto você quer apostar?"))
        
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        soma = x + y
        
        print('')
        print("A soma dos dados deu: {0}".format(soma))

        if soma == 7 or soma == 11:
            fichas += aposta
        elif soma == 2 or soma == 3 or soma == 12: #Craps
            fichas -= aposta
        else:
            print("Início da fase Point")
            
            point = soma
            while soma2 != point and soma2 != 7:
                
                x = random.randint(1, 6)
                y = random.randint(1, 6)
                soma2 = x + y
                
                if soma2 == point:
                    fichas += aposta
                elif soma2 == 7:
                    fichas -= aposta #verificar regras

                print('')
                print("A soma dos dados deu: {0}".format(soma2))
            
    fichas == fichas
         
    if jogo == "Field" or jogo == "field":
#Field(disponível em qual fase do jogo): Se a soma der 5, 6, 7 ou 8, o jogador perde tudo. Já se a soma der 3, 4, 9, 10, ou 11, o jogador ganha o mesmo valor que apostou.
        
        aposta = int(input("Quanto você quer apostar?"))
        
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        soma = x + y
        
        print('')
        print("A soma dos dados deu: {0}".format(soma))

        if soma == 5 or soma == 6 or soma == 7 or soma == 8:
            fichas -= aposta
        elif soma == 3 or soma == 4 or soma == 9 or soma == 10 or soma == 11:
            fichas += aposta
        elif soma == 2:
            fichas += aposta*2
        elif soma == 12:
            fichas += aposta*3
        
    fichas == fichas

    if jogo == "Any Craps" or jogo == "any craps":
#Any Craps(disponível em qual fase do jogo): Se a soma der 2, 3 ou 12, o jogador ganha 7 vezes o valor de sua aposta. Caso o contrário, ele perde tudo que apostou.
        
        aposta = int(input("Quanto você quer apostar?"))
        
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        soma = x + y
        
        print('')
        print("A soma dos dados deu: {0}".format(soma))

        if soma == 2 or soma == 3 or soma == 12:
            fichas += aposta*7
       
        else:
            fichas -= aposta
        
    fichas == fichas

    if jogo == "Twelve" or jogo == "twelve":
#Twelve(disponível em qual fase do jogo): Se a soma der 12, o jogador ganha 30 o valor de sua aposta. Caso o contrário, ele perde tudo.
        
        aposta = int(input("Quanto você quer apostar?"))
        
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        soma = x + y
        
        print('')
        print("A soma dos dados deu: {0}".format(soma))

        if soma == 12:
            fichas += aposta*30
        elif aposta == "desligar":
            print("O jogo acabou!")
            gameon = False
        else:
            fichas -= aposta
        
    fichas == fichas
    
    print("   ")
    print('Você tem: {0} fichas.'.format(fichas))  

else:
    print('')
    print("O jogo acabou!")