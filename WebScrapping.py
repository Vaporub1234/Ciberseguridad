import re
from colorama import Fore
import requests

website = "https://www.vulnhub.com/"
resultado = requests.get(website)
content = resultado.text
print(content)

patron = r"/entry/[\w-]"
maquinas_repetidas = re.findall(patron, str(content))
sin_duplicados = list(set(maquinas_repetidas))

maquinas_final = []

for i  in sin_duplicados:
    nombre_maquinas = i.replace("/entry", "")
    maquinas_final.append(nombre_maquinas)
    print(nombre_maquinas)

#

maquina_noob = "noob-1"
existe_noob = False

for a in maquinas_final:
    if a == maquina_noob:
        existe_noob = True
        break
Color_verde = Fore.GREEN
Color_amarillo = Fore.YELLOW

if existe_noob == True:
    print(Color_verde + "No hay ninguna maquina nueva")
else:
    print(Color_amarillo + "Maquina Nueva!")
