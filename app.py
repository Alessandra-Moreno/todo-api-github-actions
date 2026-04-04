from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = []

# 🔹 Listar todas as tarefas
@app.route("/tarefas", methods=["GET"])
def listar():
    return jsonify(tarefas)

# 🔹 Adicionar nova tarefa
@app.route("/tarefas", methods=["POST"])
def adicionar():
    data = request.json

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": data["titulo"],
        "descricao": data.get("descricao", ""),  # 👈 AQUI FOI ADICIONADO
        "concluida": False
    }

    tarefas.append(tarefa)
    return jsonify(tarefa)

# 🔹 Marcar tarefa como concluída
@app.route("/tarefas/<int:id>", methods=["PUT"])
def concluir(id):
    for t in tarefas:
        if t["id"] == id:
            t["concluida"] = True
            return jsonify(t)
    return {"erro": "Tarefa não encontrada"}, 404


if __name__ == "__main__":
    app.run(debug=True)