numero = input("Ingrese el número para mostrar su tabla de multiplicar ")
numero = int(numero)
for i in range(10):
    resultado = int((i+1)) * numero
    print(f"{numero} x {i+1} = {resultado}")