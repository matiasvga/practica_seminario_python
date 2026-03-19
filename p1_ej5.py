total = 0
nuevo = -1
print("Comience a ingresar precios. Con el precio 0 finaliza la carga.")
while(nuevo != 0):
    nuevo = float(input())
    total += nuevo
print(f"El valor total es ${total}")