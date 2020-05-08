tablaSimbolos = ""
tablaErrores = ""


def guardarSimbolo(tok):
  global tablaSimbolos
  tablaSimbolos = tablaSimbolos + ("Line: "+str(tok.lineno)+"\t"+str(tok.type)+" ~~  "+ str(tok.value)) + "\n"

def guardarError(tok):
  global tablaErrores
  error = tok.value[0]
  for x in error:
    tablaErrores = tablaErrores + ("Linea: "+str(tok.lineno)+"\t=== "+x)
