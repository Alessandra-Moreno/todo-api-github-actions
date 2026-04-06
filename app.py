from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

tarefas = []


# 👉 ROTA DA PÁGINA HTML
@app.route("/")
def home():
    return render_template("index.html")


# 👉 LISTAR TAREFAS
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)


# 👉 ADICIONAR TAREFA
@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    data = request.get_json()

    nova = {
        "id": len(tarefas) + 1,
        "titulo": data["titulo"],
        "concluida": False
    }

    tarefas.append(nova)

    return jsonify(nova), 201


# 👉 MARCAR COMO CONCLUÍDA
@app.route("/tarefas/<int:id>", methods=["PUT"])
def concluir_tarefa(id):
    for t in tarefas:
        if t["id"] == id:
            t["concluida"] = not t["concluida"]
            return jsonify(t)

    return jsonify({"erro": "não encontrada"}), 404


if __name__ == "__main__":
    app.run(debug=True)