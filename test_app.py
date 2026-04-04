from app import app

def test_listar():
    client = app.test_client()
    response = client.get("/tarefas")
    assert response.status_code == 200

def test_adicionar():
    client = app.test_client()
    response = client.post("/tarefas", json={"titulo": "Estudar"})
    assert response.status_code == 200