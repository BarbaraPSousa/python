import random

def  jogo():
    print('*********************************')
    print('Bem Vindo no jogo de Adivinhação!')
    print('*********************************')

    #Variavel do Jogo
    numero_secreto = random.randrange(1,101)
    print(numero_secreto)
    total_de_tentativas = 0
    pontos = 1000

    #Nivel do Jogo
    print('Qual nível de dificuldade?')
    print('(1)Facíl (2)Médio (3)Difícil')

    nivel = int(input('Digite o Nível: '))

    if nivel == 1:
        total_de_tentativas = 10
    elif nivel == 2:
        total_de_tentativas = 5
    else:
        total_de_tentativas = 3

    #Acertou ou errou
    for rodada in range( 1, total_de_tentativas + 1 ):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu numero: ")
        print('Você digitou:', chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print('Número inválido!, Você deve digita entre 1 e 100')
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto


        if (acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break

        else:
            if(maior):
                print('Voce errou!, seu chute foi Maior que o numero secreto.')
            elif(menor):
                print('Voce errou!, seu chute foi Menor que o numero secreto.')

                pontos_perdidos = abs(numero_secreto - chute) #numeros absolutos(ignora numeros negativos)
                pontos = pontos - pontos_perdidos

    print('***************')
    print('**Fim do Jogo**')
    print('****************')

if(__name__ ==  "__main__"):
    jogo()