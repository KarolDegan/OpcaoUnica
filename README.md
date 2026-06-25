# 📌 OpcaoUnica

## 📖 O que é este projeto

Aplicação web desenvolvida com **Flask** para gerenciamento de clientes, veículos, seguradoras e cotações de seguros.

O sistema implementa um CRUD completo (Create, Read, Update, Delete) utilizando **SQLite** como banco de dados local e **templates Jinja2** para renderização das páginas.

---

## 🧱 Stack utilizada

- **Linguagem principal:** Python
- **Frontend:** HTML, CSS, JavaScript
- **Framework backend:** Flask
- **Template engine:** Jinja2
- **Banco de dados:** SQLite (`projetoES3.db`)
- **Bibliotecas padrão:** sqlite3

---

## 📁 Estrutura do projeto

```
OpcaoUnica/
├── app.py                    # Ponto de entrada da aplicação Flask
├── routes.py                 # Rotas HTTP e lógica de controle
├── models.py                 # Acesso ao banco de dados (CRUD e queries)
├── projetoES3.db             # Banco de dados SQLite
├── requirements.txt          # Dependências do projeto
├── templates/                # Páginas HTML com Jinja2
├── static/
│   ├── css/                  # Estilos (CSS)
│   ├── imagem/               # Imagens e logos
│   └── script/               # Scripts JavaScript
├── .github/                  # Configurações do GitHub
└── __pycache__/              # Cache do Python
```

---

## 🔄 Como o sistema funciona

- `app.py` inicializa o servidor Flask
- `routes.py` gerencia as rotas e requisições HTTP
- `models.py` executa operações no banco de dados SQLite
- `templates/` renderiza as páginas dinâmicas com Jinja2
- `static/` contém arquivos estáticos (CSS, JS e imagens)

---

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/KarolDegan/OpcaoUnica.git
cd OpcaoUnica
```

### 2. Criar um ambiente virtual (recomendado)

```bash
python -m venv venv
```

**Ativar o ambiente virtual:**

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / Mac:**
```bash
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

Caso necessário instalar Flask manualmente:
```bash
pip install flask
```

### 4. Executar a aplicação

```bash
python app.py
```

A aplicação estará disponível em: **http://localhost:5002**

---

## 🗄️ Banco de dados

- Utiliza o arquivo `projetoES3.db`
- Banco SQLite local já com dados de exemplo
- CRUD implementado em `models.py`

---

## ⚠️ Observações importantes

### 🔐 Segurança

- Credenciais estão definidas diretamente em `routes.py`
- Em produção, recomenda-se:
  - Uso de variáveis de ambiente
  - Autenticação segura

### 🧾 Banco de dados

- Queries devem ser parametrizadas para evitar SQL Injection
- SQLite é usado apenas para fins de estudo

### ⚙️ Ambiente

- Recomendado Python 3.8+

---

## 🌐 Rotas principais

### 🔑 Autenticação
- `/login.html` (GET/POST)

### 👤 Clientes
- `/clientes.html`
- `/cadastrar_cliente`
- `/consultar_cliente1.html`

### 🚗 Veículos
- `/veiculo`
- `/cadastrar_veiculo`
- `/visualizar_veiculo.html`

### 🏢 Seguradoras
- `/seguradoras.html`
- `/cadastrar_seguradora`

### 📄 Seguros
- `/seguros.html`
- `/cadastrar_seguros`

### 💰 Cotações
- `/cotações.html`
- `/cadastrar_cotação
