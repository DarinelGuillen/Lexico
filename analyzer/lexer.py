# analyzer/lexer.py
import ply.lex as lex

# Lista de tokens a reconocer
tokens = (
    'FOR',
    'DO',
    'WHILE',
    'IF',
    'ELSE',
    'LPAREN',
    'RPAREN',
)

# Reglas para los tokens
t_FOR = r'for'
t_DO = r'do'
t_WHILE = r'while'
t_IF = r'if'
t_ELSE = r'else'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de nuevas líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f"Carácter no válido '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el analizador léxico
lexer = lex.lex()

def analyze_code(code):
    lexer.input(code)
    tokens_found = []

    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_found.append(f"LINEA {tok.lineno} <{tok.type}> {tok.value}")
    return tokens_found
