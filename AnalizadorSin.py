import sys
import ply.yacc as yacc
from AnalizadorLex import tokens
    

VERBOSE = 1


def p_programa(p):
    'programa : KART ID MonedaO MonedaR RayoL declaracionLista RayoR'
    pass

def p_declaracionLista(p):
    '''declaracionLista : declaracionLista  declaracion
                                            | declaracion
    '''
    pass


def p_declaracion(p):
  # let a;
  # a = 2;
  # let a = number;
    '''declaracion : tipo ID HuevoBirdo
                    | ID Toad var HuevoBirdo
                    | tipo ID Toad var HuevoBirdo
                    | if_condicion
                    | var HuevoBirdo
                    | do_condicion
                    | while_condicion
    '''
    pass


def p_OperacionKart(p):
  # a = 3+4;
    '''declaracion : tipo ID Toad expresionKart HuevoBirdo
                  | ID Toad expresionKart HuevoBirdo
                  | tipo ID Toad expresionKart_avanced HuevoBirdo
                  | ID Toad expresionKart_avanced HuevoBirdo
    '''
    pass


def p_expresionKart(p):
    '''expresionKart : var Mario var
                  | var Luigi var
                  | var Koopa var
                  | var Waluigi var
    '''
    pass


def p_expresionKart_avanced(p):
    '''expresionKart_avanced : var Mario MonedaO  expresionKart MonedaR
                   | var Luigi MonedaO  expresionKart MonedaR
                   | var  Koopa MonedaO  expresionKart MonedaR
                   | var  MonedaO  expresionKart MonedaR
     '''
    pass


def p_expresionKart_bool(p):
    '''expresionKart_bool : var Furor var
                   | var Peach var
                   | var Daysi var
                   | var DonkeyKong var
                   | var DiddyKong var
     '''
    pass

def p_if_condicion(p):
    '''if_condicion : IF MonedaO expresionKart_bool MonedaR RayoL declaracionLista RayoR
                | IF MonedaO expresionKart_bool MonedaR RayoL declaracionLista RayoR ELSE RayoL declaracionLista RayoR
    '''
    pass


def p_do_condicion(p):
    '''do_condicion : DO RayoL declaracionLista RayoR WHILE MonedaO expresionKart_bool MonedaR 
    '''
    pass


def p_while_condicion(p):
    '''while_condicion : 
                | WHILE MonedaO expresionKart_bool MonedaR RayoL declaracionLista RayoR 
    '''
    pass


def p_tipo(p):
    '''tipo : VAR
    '''
    pass


def p_var(p):
    '''var : ID
           | Puntos
           | Texto
     '''
    pass


def p_error(p):
    
    if VERBOSE: 
        
        if p is not None:
            print("ERROR Sintactico")
            print("Linea: "+str(p.lexer.lineno)+"\t== "+str(p.value))



parser = yacc.yacc()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]
        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        print("INICIA ANALISIS SINTACTICO")
        parser.parse(scriptdata, tracking=False)
        print("TERMINA ANALISIS SINTACTICO")

    else:
        print(chr(27)+"[0;31m"+"COMPILA")
