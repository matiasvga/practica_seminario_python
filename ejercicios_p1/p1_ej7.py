palabras = []
oracion = ""
print("(Para terminar con el programa ingrese 'AAA')")
palabra_nueva = input("Ingrese una palabra: ")
while(palabra_nueva != "AAA"):
    palabras.append(palabra_nueva)
    palabra_nueva = input("Ingrese una palabra: ")
for p in palabras:
    if len(p) > 3:
        oracion += " " + p
print(oracion)
