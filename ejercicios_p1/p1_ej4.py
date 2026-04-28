numero = int(input("Ingresar número: "))
lista = []
for n in range(numero):
    indice = n + 1
    if indice % 5 == 0:
        continue
    print(indice)