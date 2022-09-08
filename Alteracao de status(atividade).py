from flask import Flask, jsonify, request
import json
app = Flask(__name__) 

tarefas = [
    {  'Responsavel':'Augusto',
        'tarefa':'Desenvolver metodo get',
        'status': 'concluido'
    },
    {
        'Responsavel':'Julia',
        'tarefa':'Desenvolvedor metodo post',
        'status':'pendente'
    }
]
@app.route('/dev/<int:id>/', methods=['GET', 'POST'])
def tarefa(id):
    if request.method == 'GET':
        tarefa = tarefas[id]
        print(tarefa)
        return jsonify(tarefa)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)    
if __name__ == '__main__':
    app.run(debug = True)