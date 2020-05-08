import eel
import os
from sys import path
path.insert(0,"./analizadores/")
import tablas
from platform import system
from AnalizadorLex import escanear
from AnalizadorSin import parsear

@eel.expose
def clean():
  tablas.tablaSimbolos = ""
  tablas.tablaErrores= ""

@eel.expose
def analizar(texto):
  # obtenemos las variables desde utils
  escanear(texto)
  parsear(texto)
  if len(tablas.tablaSimbolos) > 0:
    eel.printGui(tablas.tablaSimbolos,"simbols")
  if len(tablas.tablaErrores) > 0:
    eel.printGui(tablas.tablaErrores,"errors")
    eel.showGif("error")
  else:
    eel.showGif("noError")

def __init__():
  eel.init('./gui')
  eel.start('index.html', size = (960, 540))

if __name__ == "__main__":
  __init__()
