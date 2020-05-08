import eel
import os
from platform import system

@eel.expose
def analizar(texto):
  # obtenemos las variables desde utils
  tabla_simbolos = "LexToken(tepo,15,2)\nLexToken(tepo,15,2)\nLexToken(tepo,15,2)\nLexToken(tepo,15,2)\nLexToken(tepo,15,2)\nLexToken(tepo,15,2)"
  tabla_errores = ""
  # tabla_errores ="LexToken(error,15,2)"
  if len(tabla_simbolos) > 0:
    print("simbolos")
  if len(tabla_errores) > 0:
    print("errores")
  else:
    eel.showGif("noError")

def __init__():
  eel.init('./gui')
  eel.start('index.html', size = (960, 540))

if __name__ == "__main__":
  __init__()
