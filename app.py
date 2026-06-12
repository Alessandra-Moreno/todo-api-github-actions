from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

# Variável de ambiente (atende ao requisito da atividade)
APP_ENV = os.getenv("APP_ENV", "development")

tarefas = []


# ROTA DA PÁGINA HTML
@app.route("/")
def home():
    return render_template("index.html", tarefas=tarefas)


# LISTAR TAREFAS (API)
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return {"tarefas": tarefas}, 200


# ADICIONAR TAREFA
@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    nome = request.form.get("nome")

    if not nome:
        return {"erro": "Nome da tarefa é obrigatório"}, 400

    nova = {
        "id": len(tarefas) + 1,
        "nome": nome,
        "feito": False
    }

    tarefas.append(nova)

    return redirect("/")


# MARCAR COMO FEITA / DESFEITA
@app.route("/toggle/<int:id>", methods=["POST"])
def toggle_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["feito"] = not tarefa["feito"]
            break

    return redirect("/")


if __name__ == "__main__":
    print(f"Ambiente: {APP_ENV}")
    app.run(host="0.0.0.0", port=5000)