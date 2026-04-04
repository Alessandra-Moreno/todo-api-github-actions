from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Estudar a materia", "concluida": False}
]


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)


@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    nova_tarefa = request.json

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": nova_tarefa["titulo"],
        "concluida": False
    }

    tarefas.append(tarefa)
    return jsonify(tarefa), 201


@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            dados = request.json
            tarefa["titulo"] = dados.get("titulo", tarefa["titulo"])
            tarefa["concluida"] = dados.get("concluida", tarefa["concluida"])
            return jsonify(tarefa)

    return jsonify({"erro": "Tarefa não encontrada"}), 404


@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "Tarefa removida"})

    return jsonify({"erro": "Tarefa não encontrada"}), 404


if __name__ == "__main__":
    app.run(debug=True)