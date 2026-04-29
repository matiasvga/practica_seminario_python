from pathlib import Path
import json

dir_archivo = Path('practica/max_verstappen_lyrics.json')
letra = """Tu-tu-du-du
Max Verstappen
Tu-tu-du-du
Max Verstappen
Tu-tu-du-du
Max Verstappen
Tu-tu-du-du
Max Verstappn
Let's shake it to the Max
Put your hands up, hands up
Let's shake it to the Max
Put your hands up, hands up
Let's go!
Let's go!
Let's go!
Let's go!
Let's go! (go, go, go, go)
Max Verstappe
Tu-tu-du-du
Max Verstappen
Tu-tu-du-du
Max Verstappen
Tu-tu-du-du
Max Verstappen
Tu-tu-du-du
Max Verstappe
(That's how we do it)
(Simply, simply lovely)
(Yes! Woo!)
(Hahahaha
(Yeah, here we go again)
(Oh my lord, Max!)
Yes! Yes!
Oh my God!
Woohoo!
Yes! Max Verstappen
You are the world champion
The world champio
Tu-tu-du-du
Max Verstappen
Tu-tu-du-du
Max Verstappen
Tu-tu-du-du
Max Verstappen
Tu-tu-du-du
Max Verstappen
ó
"""

lista = letra.splitlines()

with open(dir_archivo, 'w') as f:
    json.dump(lista, f, indent=1)
    
with open(dir_archivo, 'r', encoding= 'utf-8') as f:
    for line in f:
        print(line)

with open(dir_archivo, 'a') as f:
    json.dump(letra, f, indent= 1)
letra_json = json.dumps(letra)
print(letra_json)