import sys
import ply.lex as lex


tokens = (

    'FUNCION', 
    'IF', 
    'VAR',
    'PRINT',
    'DO',
    'FOR',
    'ELSE',
    'WHILE',
    'TRUE',
    'FALSE',

    'MAS',
    'MASXDOS',
    'MENOS',
    'MULT',
    'DIVIDIR',
    'MENOR',
    'MAYORIGUALQ',
    'MENORIGUALQ',
    'MAYOR',
    'IGUAL',
    'IGUALXDOS',
    'PUNTOCOMA',
    'COMA',
    'LPAREN',
    'RPAREN',
    'LBLOCK',
    'RBLOCK',
    'DOSPUNTOS',
    'HASHTAG',
    'QUOTES',
    'APOSTROPHE',
    'COMENTARIOS',
    'ID',
    'NUMERO',
    'CADENA',
)

t_MAS            = r'\+'
t_MENOS          = r'-'
t_MULT           = r'\*'
t_DIVIDIR        = r'/'
t_IGUAL          = r'='
t_MENOR          = r'<'
t_MAYOR          = r'>'
t_PUNTOCOMA      = r';'
t_COMA           = r','
t_LPAREN         = r'\('
t_RPAREN         = r'\)'
t_LBLOCK         = r'{'
t_RBLOCK         = r'}'
t_DOSPUNTOS      = r':'
t_HASHTAG        = r'\#'
t_QUOTES         = r'\"'
t_APOSTROPHE     = r'\''
t_ignore         = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_VAR(t):
    r'var'
    return t
    
def t_DO(t):
    r'HACER'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCION(t):
    r'FUNCION'
    return t

def t_IF(t):
    r'if'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_MENORIGUALQ(t):
    r'<='
    return t

def t_MAYORIGUALQ(t):
    r'>='
    return t

def t_IGUALXDOS(t):
    r'=='
    return t

def t_MASXDOS(t):
    r'\+\+'
    return t

def t_COMENTARIOS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(\w\d)*'
    return t

def t_CADENA(t):
    r'(("[^"]*")|(\'[^\']*\')|(\`[^\`]*\`))'
    return t


def t_error(t):
    error = t.value[0]
    for x in error:
        print("Error Token")
        print("Linea: "+str(t.lexer.lineno)+"\t=== "+x)

    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == '__main__':
    if (len(sys.argv) > 1):
        script = sys.argv[1]

        scriptfile = open(script, 'r')
        scriptdata = scriptfile.read()
        lexer.input(scriptdata)

        print ("INICIA ANALISIS LEXICO")
        i = 1
        while True:
            tok = lexer.token()
            if not tok:
                break
            print ("\t"+str(i)+" - "+"Line: "+str(tok.lineno)+"\t"+str(tok.type)+"\t            ~~  "+str(tok.value))
            i += 1
        
        print ("TERMINA ANALISIS LEXICO")
    else:
        print ("COMPILA")


