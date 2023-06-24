from flask import Flask, render_template, request

app = Flask(__name__)

dados = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar.html')
def cadastrar():
    return render_template('cadastro.html')

@app.route('/inserir', methods=['POST'])
def inserir():
    id = request.form['id']
    titulo = request.form['titulo']
    ano = request.form['ano']
    
    if id in dados:
        return render_template('cadastro.html', mensagem='Id já cadastrado')
    else:
        dados[id] = {'titulo': titulo, 'ano': ano}
        return render_template('cadastro.html', mensagem = 'Filme cadastrado com sucesso!')

@app.route('/listagem.html')
def listagem():
    return render_template('listagem.html', dados = dados)

app.run(host = '0.0.0.0', port=81)