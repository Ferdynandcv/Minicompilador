import sys
import ply.yacc as yacc
from AnalizadorLex import tokens
    

VERBOSE = 1


def p_programa(p):
    'programa : FUNCION ID LPAREN RPAREN LBLOCK declaracionLista RBLOCK'
    pass

def p_declaracionLista(p):
    '''declaracionLista : declaracionLista  declaration
                                            | declaration
    '''
    pass


def p_declaration(p):
  # let a;
  # a = 2;
  # let a = number;
    '''declaration : tipo ID PUNTOCOMA
                    | ID IGUAL var PUNTOCOMA
                    | tipo ID IGUAL var PUNTOCOMA
                    | if_condicion
                    | var PUNTOCOMA
                    | do_condicion
                    | while_condition
    '''
    pass


def p_operation(p):
  # let a = 2+2;
  # a = 3+4;
    '''declaration : tipo ID IGUAL expression PUNTOCOMA
                  | ID IGUAL expression PUNTOCOMA
                  | tipo ID IGUAL expression_avanced PUNTOCOMA
                  | ID IGUAL expression_avanced PUNTOCOMA
    '''
    pass


def p_expression(p):
    '''expression : var MAS var
                  | var MENOS var
                  | var  MULT var
                  | var DIVIDIR var
    '''
    pass


def p_expression_avanced(p):
    '''expression_avanced : var MAS LPAREN  expression RPAREN
                   | var MENOS LPAREN  expression RPAREN
                   | var  MULT LPAREN  expression RPAREN
                   | var DIVIDIR LPAREN  expression RPAREN
     '''
    pass


def p_expression_bool(p):
    '''expression_bool : var IGUALXDOS var
                   | var MENOR var
                   | var MAYOR var
                   | var MAYORIGUALQ var
                   | var MENORIGUALQ var
     '''
    pass

def p_if_condicion(p):
    '''if_condicion : IF LPAREN expression_bool RPAREN LBLOCK declaracionLista RBLOCK
                | IF LPAREN expression_bool RPAREN LBLOCK declaracionLista RBLOCK ELSE LBLOCK declaracionLista RBLOCK
    '''
    pass


def p_do_condicion(p):
    '''do_condicion : DO LBLOCK declaracionLista RBLOCK WHILE LPAREN expression_bool RPAREN 
    '''
    pass


def p_while_condition(p):
    '''while_condition : 
                | WHILE LPAREN expression_bool RPAREN LBLOCK declaracionLista RBLOCK 
    '''
    pass


def p_tipo(p):
    '''tipo : VAR
    '''
    pass


def p_var(p):
    '''var : ID
           | NUMERO
           | CADENA
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
