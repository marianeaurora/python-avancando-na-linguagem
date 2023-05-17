#Listas

pessoa1 = ['Niko',20]
pessoa2 = ['Thayna',25]
pessoa3 = ['Malcon',18]
pessoa5 = ['Adriel',26]

print('Uma lista de pessoas:')
print(pessoa1)
print(pessoa2)
print(pessoa3)

print('O nome da pessoa na posição 1 é:')
print(pessoa1[0])


amigos = [pessoa1, pessoa2,pessoa3]
print('Todos os meus amigos juntos são:')
print(amigos)

amigos.append(pessoa5)
print('E na lista sempre tem espaço para mais um:')
print(amigos)

#Tuplas - são imutáveis

melhores_amigos = (pessoa1,pessoa2,pessoa3,pessoa5)
print('As tuplas são imutáveis, pois sempre serão melhores amigos')
print(melhores_amigos)

amigos_sempre = tuple(amigos)
print(amigos_sempre)


