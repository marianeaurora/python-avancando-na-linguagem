from unidecode import unidecode
import random


def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():


    with open("palavras.txt", "r", encoding="UTF-8") as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]
def input_chute():
    chute = input ("Qual a letra?\n") 
    chute = chute.strip().upper()
    return chute
def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (unidecode(chute).upper() == unidecode(letra).upper()):
            letras_acertadas[index] = letra
        #index = index + 1
        index += 1
        
def mensagem_ganhador():
    print("Você Ganhou!")

def mensagem_perdedor(palavra_secreta):
    print("AH Não...Você Perdeu!")
    print("A palavra secreta era {}".format(palavra_secreta))

def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if(tentativas == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(tentativas== 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(tentativas == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(tentativas == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (tentativas == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():

    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while(not enforcou and not acertou):

        desenha_forca(tentativas)
        
        chute = input_chute()

        if(chute in palavra_secreta or unidecode(chute) in unidecode(palavra_secreta)):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            #tentativas = tentativas + 1
            tentativas += 1

        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

        if(acertou):
            mensagem_ganhador()
        elif(enforcou):
            mensagem_perdedor(palavra_secreta)

        
    

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
