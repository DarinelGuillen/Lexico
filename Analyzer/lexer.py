import ply.lex as lex

# Lista de tokens
tokens = [
    'PR', 'PRJ', 'PRC', 'ID', 'CAD', 'PI', 'PD', 'LI', 'LD', 'PC', 'EX'
]

# Palabras reservadas por lenguaje
reserved_python = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'try', 'while', 'yield', 'print', 'program', 'match', 'case', 'with',
    'type', 'dir', 'len', 'repr', 'eval', 'exec', 'print', 'else'
}

reserved_javascript = {
    'break'
}

reserved_csharp = {
    'abstract'
}

# Asignar el tipo de token PR correcto a cada palabra reservada
reserved = {word: 'PR' for word in reserved_python}
reserved.update({word: 'PRJ' for word in reserved_javascript})
reserved.update({word: 'PRC' for word in reserved_csharp})

# Actualización de la lista de tokens con las palabras reservadas
tokens = list(set(tokens + list(reserved.values())))

# Definiciones de tokens no basados en palabras
t_CAD = r'\"[^"]*\"'
t_PI  = r'\('
t_PD  = r'\)'
t_LI  = r'\{'
t_LD  = r'\}'
t_PC  = r'\;'

# Función para identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    if t.type == 'ID' and t.value not in ['suma', 'a', 'b', 'c']:
        t.type = 'EX'
    return t

# Definir una regla para manejar errores léxicos
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
