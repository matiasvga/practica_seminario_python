#Ejercicio 2 de la práctica 1
total = input("Ingrese la cantidad de segundos\n")
segundos = int(total)
horas = segundos // (60*60)
segundos = segundos % (60*60)
minutos = segundos // 60
segundos = segundos % 60
print(f"{total} segundos equivalen a {horas} h, {minutos} m, {segundos} s")