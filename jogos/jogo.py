import forca
import adivihacao

def escolhe_jogo():

    print('*************************')
    print('*** escolha seu Jogo! ***')
    print('*************************')

    print('(1)forca (2)Adivinhação')

    jogo = int(input('Qual Jogo? '))

    if jogo == 1:
        print('Jogo Forca')
        forca.jogo()
    elif jogo == 2:
        print('Jogo Adivihacao')
        adivihacao.jogo()

if(__name__ ==  "__main__"):
    escolhe_jogo()