from flask import Flask, request, render_template_string
import ply.lex as lex

app = Flask(__name__)

# Tokens
tokens = (
    'CONST', 'IDENTIFIER', 'EQUALS', 'ARROW', 'RETURN', 'DIV_OPEN', 'DIV_CLOSE', 'H1_OPEN', 'H1_CLOSE', 'TEXT', 'SEMICOLON'
)

# Regular expressions for simple tokens
t_CONST = r'const'
t_EQUALS = r'='
t_ARROW = r'\(\)\s*=>'
t_RETURN = r'return'
t_DIV_OPEN = r'<div>'
t_DIV_CLOSE = r'</div>'
t_H1_OPEN = r'<h1>'
t_H1_CLOSE = r'</h1>'
t_SEMICOLON = r';'

# Complex tokens
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_TEXT(t):
    r'[^<>]+'
    return t

# Ignored characters (spaces and tabs)
t_ignore = ' \t\n'

# Error handling
def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

valid_code_pattern = r'''
    const\s+[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*\(\)\s*=>\s*\{\s*return\s*\(\s*<div>\s*<h1>[^<>]*<\/h1>\s*<\/div>\s*\)\s*;\s*\};
'''

@app.route('/')
def index():
    return render_template_string(open("index.html").read())

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form['code']
    lexer.input(code)

    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_list.append((tok.type, tok.value))

    is_valid = re.fullmatch(valid_code_pattern, code, re.VERBOSE) is not None
    error_message = "" if is_valid else "Error: Invalid code format"

    result_html = f'''
    <h2>Analysis Result</h2>
    <table>
        <tr>
            <th>Token</th>
            <th>Value</th>
        </tr>
        {''.join(f'<tr><td>{token[0]}</td><td>{token[1]}</td></tr>' for token in tokens_list)}
    </table>
    <h2>{error_message}</h2>
    '''

    return render_template_string(result_html)

if __name__ == '__main__':
    app.run(debug=True)
