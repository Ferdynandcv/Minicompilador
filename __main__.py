import eel
import os
from sys import path
path.insert(0,"./analizadores/")
import tablas
from platform import system

@eel.expose
def analizar(texto):
  # obtenemos las variables desde utils
  if len(tablas.tablaSimbolos) > 0:
    print("simbolos")
  if len(tablas.tablaErrores) > 0:
    print("errores")
  else:
    eel.showGif("noError")

def __init__():
  eel.init('./gui')
  eel.start('index.html', size = (960, 540))

if __name__ == "__main__":
  __init__()
