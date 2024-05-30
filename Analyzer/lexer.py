import ply.lex as lex

# Lista de tokens
tokens = [
    'PRP', 'PRJ', 'PRC', 'ID', 'CAD', 'PI', 'PD', 'LI', 'LD', 'PC', 'EX'
]

# Palabras reservadas por lenguaje
reserved_python = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
    'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
    'return', 'try', 'while', 'yield', 'print', 'program', 'match', 'case', 'with',
    'type', 'dir', 'len', 'repr', 'eval', 'exec'
}


reserved_javascript = {
    'break', 'case', 'catch', 'class', 'const', 'continue', 'debugger', 'default', 'delete', 'do',
    'else', 'export', 'extends', 'finally', 'for', 'function', 'if', 'import', 'in', 'instanceof',
    'new', 'return', 'super', 'switch', 'this', 'throw', 'try', 'typeof', 'var', 'while',
    'let', 'yield', 'consolelog', 'async', 'await', 'null', 'true', 'false', 'NaN', 'undefined',
    'Infinity'
}


reserved_csharp = {
    'abstract', 'System', 'as', 'base', 'bool', 'break', 'byte', 'case', 'catch', 'char', 'class',
    'const', 'continue', 'decimal', 'default', 'delegate', 'do', 'double', 'else', 'enum', 'event',
    'explicit', 'extern', 'false', 'finally', 'fixed', 'float', 'for', 'foreach', 'goto', 'if',
    'in', 'int', 'lock', 'long', 'namespace', 'new', 'null', 'object', 'operator', 'out',
    'override', 'params', 'private', 'protected', 'public', 'readonly', 'ref', 'return', 'sbyte', 'sealed',
    'sizeof', 'stackalloc', 'static', 'string', 'struct', 'switch', 'this', 'throw', 'true', 'try',
    'typeof', 'uint', 'ulong', 'unchecked', 'unsafe', 'ushort', 'using', 'virtual', 'void', 'volatile',
    'while', 'ConsoleWriteLine', 'async', 'await', 'dynamic', 'yield', 'add', 'remove', 'get', 'set'
}


# Asignar el tipo de token PR correcto a cada palabra reservada
reserved = {word: 'PRP' for word in reserved_python}
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
