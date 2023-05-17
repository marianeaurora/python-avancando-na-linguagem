numero = int(input("Digite um número \n"))

print("Os divisores de {} são:".format(numero))

for i in range(1, numero+1):
    if numero % i == 0:
        print(i)