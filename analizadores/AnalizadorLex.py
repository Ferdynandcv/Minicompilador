import sys
import ply.lex as lex


tokens = (

    'KART', 
    'IF', 
    'VAR',
    'PRINT',
    'DO',
    'FOR',
    'ELSE',
    'WHILE',
    'TRUE',
    'FALSE',

    'Mario',
    'BebeMario',
    'Luigi',
    'Koopa',
    'Waluigi',
    'Peach',
    'DonkeyKong',
    'DiddyKong',
    'Daysi',
    'Toad',
    'Furor',
    'HuevoBirdo',
    'Bobombs',
    'MonedaO',
    'MonedaR',
    'RayoL',
    'RayoR',
    'HuevoYoshi',
    'DonPisoton',
    'QUOTES',
    'COMENTARIOS',
    'ID',
    'Puntos',
    'Texto',
)

t_Mario             = r'\+'
t_Luigi             = r'-'
t_Koopa             = r'\*'
t_Waluigi           = r'/'
t_Toad              = r'='
t_Peach             = r'<'
t_Daysi             = r'>'
t_HuevoBirdo        = r';'
t_Bobombs           = r','
t_MonedaO           = r'\('
t_MonedaR           = r'\)'
t_RayoL             = r'{'
t_RayoR             = r'}'
t_HuevoYoshi        = r':'
t_DonPisoton        = r'\#'
t_QUOTES            = r'\"'
t_ignore            = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_VAR(t):
    r'var'
    return t
    
def t_DO(t):
    r'BillBala'
    return t

def t_ELSE(t):
    r'CapPichos'
    return t

def t_FOR(t):
    r'CapRojo'
    return t

def t_KART(t):
    r'KART'
    return t

def t_IF(t):
    r'CapVerde'
    return t

def t_PRINT(t):
    r'Champiturbo'
    return t

def t_WHILE(t):
    r'platano'
    return t

def t_TRUE(t):
    r'FlorFuego'
    return t

def t_FALSE(t):
    r'FlorBoomerang'
    return t

def t_DiddyKong(t):
    r'<='
    return t

def t_DonkeyKong(t):
    r'>='
    return t

def t_Furor(t):
    r'=='
    return t

def t_BebeMario(t):
    r'\+\+'
    return t

def t_COMENTARIOS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

def t_Puntos(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(\w\d)*'
    return t

def t_Texto(t):
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


