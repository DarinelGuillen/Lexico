from flask import Flask, request, render_template, jsonify
import ply.lex as lex

app = Flask(__name__)

# Tokens
tokens = [
    'FOR', 'IF', 'DO', 'WHILE', 'ELSE',
    'LPAREN', 'RPAREN'
]

# Regular expression rules for simple tokens
t_FOR = r'for'
t_IF = r'if'
t_DO = r'do'
t_WHILE = r'while'
t_ELSE = r'else'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignored characters (whitespace)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_code():
    data = request.json
    code = data.get('code', '')

    # Tokenize the input code
    lexer.input(code)
    results = []
    line_num = 1
    line_tokens = []

    while True:
        tok = lexer.token()
        if not tok:
            if line_tokens:
                results.append({'line': line_num, 'tokens': line_tokens})
            break
        if tok.lineno != line_num:
            results.append({'line': line_num, 'tokens': line_tokens})
            line_num = tok.lineno
            line_tokens = []

        line_tokens.append({'type': tok.type, 'value': tok.value})

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
