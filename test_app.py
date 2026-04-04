import json

from app import app


def test_listar_tarefas():
    client = app.test_client()

    response = client.get("/tarefas")

    assert response.status_code == 200


def test_adicionar_tarefa():
    client = app.test_client()

    nova_tarefa = {"titulo": "Nova tarefa"}

    response = client.post(
        "/tarefas",
        data=json.dumps(nova_tarefa),
        content_type="application/json"
    )

    assert response.status_code == 201

