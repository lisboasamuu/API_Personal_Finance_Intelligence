# 💰 Personal Finance Intelligence API

API REST inteligente para gerenciamento de finanças pessoais, desenvolvida com Python + Flask.

Criei esta minha primeira aplicação que permite cadastrar transações financeiras, categorizar automaticamente despesas e gerar insights financeiros com base nos hábitos do usuário.

---

# 🚀 Funcionalidades

- ✅ CRUD completo de transações
- ✅ Categorização automática inteligente
- ✅ Filtros por categoria e data
- ✅ Resumo financeiro por categorias
- ✅ Insights financeiros automáticos
- ✅ Validação de dados
- ✅ Arquitetura organizada em camadas
- ✅ Banco SQLite com suporte fácil para PostgreSQL

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| Python 3.10+ | Linguagem principal |
| Flask | Framework web |
| SQLAlchemy | ORM |
| SQLite | Banco de dados |
| REST API | Arquitetura da API |

---

# 📁 Estrutura do Projeto

```bash
Personal_Finance_Intelligence_API/
│
├── src/
│   ├── api/
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── health.py
│   │       ├── transactions.py
│   │       ├── summary.py
│   │       └── insights.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── transaction.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── transaction_schema.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── categorization.py
│   │   ├── transaction_service.py
│   │   ├── summary_service.py
│   │   └── insights_service.py
│   │
│   └── app.py
│
├── requirements.txt
├── run.py
├── README.md
└── .gitignore
```

---

# ⚙️ Instalação

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/Personal_Finance_Intelligence_API.git

cd Personal_Finance_Intelligence_API
```

---

## 2️⃣ Crie o ambiente virtual

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Execute a aplicação

```bash
python run.py
```

Servidor disponível em:

```bash
http://127.0.0.1:5000
```

---

# 📌 Endpoints

# 🩺 Health Check

## GET `/health`

Verifica se a API está online.

### Response

```json
{
  "status": "ok"
}
```

---

# 💳 Transações

## POST `/transactions`

Cria uma nova transação.

### Request

```json
{
  "description": "Uber viagem",
  "amount": 35.90,
  "date": "2026-04-25"
}
```

### Response

```json
{
  "id": 1,
  "description": "Uber viagem",
  "amount": 35.90,
  "date": "2026-04-25",
  "category": "transporte"
}
```

---

## GET `/transactions`

Lista todas as transações.

### Filtro por categoria

```http
GET /transactions?category=transporte
```

### Filtro por mês

```http
GET /transactions?date=2026-04
```

---

## GET `/transactions/{id}`

Busca uma transação específica.

### Response

```json
{
  "id": 1,
  "description": "Uber viagem",
  "amount": 35.90,
  "date": "2026-04-25",
  "category": "transporte"
}
```

---

## PUT `/transactions/{id}`

Atualiza uma transação.

### Request

```json
{
  "amount": 40.00
}
```

---

## DELETE `/transactions/{id}`

Remove uma transação.

### Response

```http
204 No Content
```

---

# 📊 Resumo Financeiro

## GET `/summary`

Retorna o resumo financeiro.

### Response

```json
{
  "total": 285.90,
  "por_categoria": {
    "transporte": 35.90,
    "alimentacao": 250.00
  }
}
```

---

# 🤖 Insights Financeiros

## GET `/insights`

Gera insights automáticos.

### Response

```json
[
  "Você gastou muito com alimentação esse mês.",
  "Transporte aumentou em relação ao mês passado."
]
```

---

# 🧠 Categorização Automática

A API identifica automaticamente categorias com base na descrição da transação.

| Categoria | Palavras-chave |
|---|---|
| Transporte | uber, 99, taxi, ônibus |
| Alimentação | mercado, restaurante, pizza |
| Moradia | aluguel, luz, água |
| Lazer | netflix, cinema, spotify |
| Saúde | farmácia, exame, médico |

Caso nenhuma categoria seja encontrada:

```json
{
  "category": "outros"
}
```

---

# 🗄️ Banco de Dados

Por padrão a aplicação utiliza SQLite.

Arquivo:

```bash
finance.db
```

Para utilizar PostgreSQL:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://usuario:senha@localhost:5432/database"
```

---

# 🧪 Testes com cURL

## Criar transação

```bash
curl -X POST http://127.0.0.1:5000/transactions \
-H "Content-Type: application/json" \
-d "{\"description\":\"Uber\",\"amount\":35.90,\"date\":\"2026-04-25\"}"
```

---

## Buscar resumo

```bash
curl http://127.0.0.1:5000/summary
```

---

# 📈 Roadmap

- [ ] JWT Authentication
- [ ] Docker
- [ ] PostgreSQL
- [ ] Paginação
- [ ] Dashboard financeiro
- [ ] Upload de comprovantes
- [ ] Exportação CSV/PDF
- [ ] Testes automatizados
- [ ] Deploy em cloud

---

# 🤝 Contribuição

Contribuições são bem-vindas.

```bash
# Fork o projeto

# Crie sua branch
git checkout -b feature/minha-feature

# Commit
git commit -m "feat: minha nova feature"

# Push
git push origin feature/minha-feature
```

Depois abra um Pull Request 🚀

---

# 📄 Licença

Este projeto está sob a licença MIT.

---

# 👨‍💻 Autor

Samuel Lisboa

- GitHub: https://github.com/lisboasamuu
- LinkedIn: https://www.linkedin.com/in/samuel-l-02b2712b0/

---

# ⭐ Apoie o Projeto

Se este projeto te ajudou, deixe uma estrela no repositório ⭐