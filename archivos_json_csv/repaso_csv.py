import csv
from pathlib import Path

ruta_archivo = Path(__file__).parent.parent / 'archive' / 'songs_normalize.csv'
#ruta_archivo = r'C:\Users\vegam\OneDrive\Escritorio\Código\FACULTAD\Python\practica_seminario_python\archive\mono.png'

with open(ruta_archivo, 'r', encoding= 'UTF-8') as f:
    csv_reader = csv.reader(f,delimiter= ',')
    header = csv_reader.__next__()
    for line in csv_reader:
        if line[0] == 'Britney Spears':
            print(line)
try:
    archivo = open('pp.txt')
    archivo.close()
except FileNotFoundError:
    print('No existe el archivo')
p = Path('archive/mono.png')
print(p)