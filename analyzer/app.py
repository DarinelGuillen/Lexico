# analyzer/app.py
from flask import Flask, render_template, request
from lexer import analyze_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', code='', tokens=[])

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form.get('codigo', '')
    tokens = analyze_code(code)
    return render_template('index.html', code=code, tokens=tokens)

if __name__ == '__main__':
    app.run(debug=True)
