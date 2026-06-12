# Todo API com GitHub Actions

Projeto de exemplo utilizando GitHub Actions, Docker e Docker Compose.

## Funcionalidades

- Adicionar tarefas
- Listar tarefas
- Concluir tarefas

## GitHub Actions

- Execução automática de testes
- Verificação de código (lint)
- Release automático por tag
- Build automático de imagem Docker
- Publicação automática da imagem no GitHub Container Registry (GHCR)

## Docker

A aplicação utiliza Docker Compose com 3 serviços:

- Flask (aplicação)
- PostgreSQL (banco de dados)
- Adminer (gerenciamento do banco)

Também utiliza:

- Variáveis de ambiente (.env)
- Volume Docker para persistência dos dados

## Como rodar com Python

```bash
pip install -r requirements.txt
python app.py
```

## Como rodar com Docker

```bash
docker compose up --build
```

Aplicação:

```text
http://localhost:5000
```

Adminer:

```text
http://localhost:8080
```
