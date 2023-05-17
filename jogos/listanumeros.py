
numeros = input("Digite uma lista de Numeros separados por virgula \n").split(",")
lista = [int(numero) for numero in numeros]
print(lista)

maior = lista[0]
menor = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print("O menor numero é {} e o maior é {}".format(menor,maior))