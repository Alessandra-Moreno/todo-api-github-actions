from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = []
contador_id = 1


@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas), 200


@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    global contador_id

    dados = request.get_json()

    if not dados or 'titulo' not in dados:
        return jsonify({'erro': 'Título é obrigatório'}), 400

    nova_tarefa = {
        "id": contador_id,
        "titulo": dados['titulo'],
        "feito": False
    }

    tarefas.append(nova_tarefa)
    contador_id += 1

    return jsonify(nova_tarefa), 201


@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_status(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["feito"] = not tarefa["feito"]
            return jsonify(tarefa), 200

    return jsonify({'erro': 'Tarefa não encontrada'}), 404


if __name__ == '__main__':
    app.run(debug=True)

