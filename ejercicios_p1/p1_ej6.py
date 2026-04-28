numero = int(input("Ingresar número: "))
otros = []
multiplos = []

for n in range(numero):
    indice = n + 1
    if indice % 5 == 0:
        multiplos.append(indice)
    else:
        otros.append(indice)
print(multiplos)
print(otros)