from flask import Flask, request, render_template
import lexer  # Asegúrate de que lexer.py esté en el mismo directorio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.form['code']
        lexer.lexer.input(code)
        result = []
        # Actualización para incluir PRP, PRJ y PRC
        token_count = {'PRP': 0, 'PRJ': 0, 'PRC': 0, 'ID': 0, 'CAD': 0, 'EX': 0, 'PI': 0, 'PD': 0, 'LI': 0, 'LD': 0, 'PC': 0}
        while True:
            tok = lexer.lexer.token()
            if not tok:
                break
            result.append(tok)
            if tok.type in token_count:
                token_count[tok.type] += 1
        return render_template('main.html', result=result, token_count=token_count)
    return render_template('main.html', result=[], token_count=None)

if __name__ == '__main__':
    app.run(debug=True)
