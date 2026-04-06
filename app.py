from flask import Flask, request, render_template, redirect

app = Flask(__name__)

tarefas = []


# ROTA DA PÁGINA HTML
@app.route("/")
def home():
    return render_template("index.html", tarefas=tarefas)


# LISTAR TAREFAS (opcional, API)
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return {"tarefas": tarefas}


# ADICIONAR TAREFA
@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    nome = request.form["nome"]

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
    app.run(debug=True)