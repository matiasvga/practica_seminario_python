from pathlib import Path
datos_estudiantes = [
    {'DNI': 12345, 'name': 'Guido Van Rossum', 'pts_teoria':100,
     'pts_practica': 50, 'city': 'Haarlem', 'group': 'info:TM'},
    {'DNI': 11111, 'name': 'Ada Lovelace', 'pts_teoria': 100,
    'pts_practica': 50, 'city': 'Londres', 'group': 'info:TM'},
    {'DNI': 12345, 'name': 'Alan Turing', 'pts_teoria': 100,
    'pts_practica': 50, 'city': 'Londres', 'group': 'info_TT'},
    {'DNI': 11111, 'name': 'Joan Clarke', 'pts_teoria': 100,
    'pts_practica': 50, 'city': 'Londres', 'group': 'info_TT'}
]

dir_archivo = Path('estudiantes.txt')
archivo = open(dir_archivo, 'wt')

lineas = []
for estudiante in datos_estudiantes:
    aux = ''    
    for llave in list(estudiante.keys()):
        aux += f'{llave}:{estudiante[llave]},'
    aux += '\n'
    lineas.append(aux)
    
archivo.writelines(lineas)
archivo.close()

#print(list(datos_estudiantes[0].keys())[0])