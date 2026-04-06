from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []
contador_id = 1


@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)


@app.route('/add', methods=['POST'])
def add():
    global contador_id
    nome = request.form.get('nome')

    if nome:
        tarefas.append({
            "id": contador_id,
            "nome": nome,
            "feito": False
        })
        contador_id += 1

    return redirect('/')


@app.route('/toggle/<int:id>', methods=['POST'])
def toggle(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["feito"] = not tarefa["feito"]
            break

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
