from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

tarefas = []


@app.route("/")
def home():
    return render_template("index.html", tarefas=tarefas)


@app.route("/tarefas", methods=["GET"])
def listar():
    return jsonify(tarefas)


@app.route("/tarefas", methods=["POST"])
def adicionar():
    if request.is_json:
        data = request.json
        titulo = data.get("titulo")
    else:
        titulo = request.form.get("titulo")

    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "concluida": False
    }

    tarefas.append(tarefa)

    return redirect("/")  # volta pra página principal


@app.route("/tarefas/<int:id>", methods=["PUT"])
def concluir(id):
    for t in tarefas:
        if t["id"] == id:
            t["concluida"] = True
            return jsonify(t)

    return {"erro": "Tarefa não encontrada"}, 404


if __name__ == "__main__":
    app.run(debug=True)