# OpcaoUnica

## What this is
Aplicação web em Flask para gerenciamento de clientes, veículos, seguradoras e cotações (um sistema simples de CRUD para operações relacionadas a seguros). Fornece páginas HTML (Jinja2) para operações de criação, leitura, atualização e exclusão e usa um banco SQLite local (projetoES3.db) como armazenamento de dados de exemplo.

---

### Stack
- **Linguagens:** Python (backend), HTML/CSS/JavaScript (templates e scripts front-end)
- **Framework / runtime:** Flask
- **Bibliotecas notáveis:** Flask (render_template, request), sqlite3 (acesso direto ao DB), Jinja2 (templates).

---

## How it's organized
Árvore anotada dos principais arquivos/diretórios:

```
app.py                 # entrypoint: instancia e roda o Flask (porta 5002)
routes.py               # definções de rotas, validações, lógica de apresentação e handlers POST/GET
models.py               # funções de acesso ao banco e helpers (CRUD)
projetoES3.db           # banco SQLite com dados de exemplo
requirements.txt        # dependências (instalar com pip install -r requirements.txt)

templates/              # páginas Jinja2 (login, telas de cadastro, listas, visualizações, etc.)
static/
  css/                  # arquivos CSS (geral.css, visualizar_veiculo.css)
  imagem/               # logos e imagens usadas nas páginas
  script/               # JavaScript cliente para validação/submit/UX

.github/                # metadados do repositório
__pycache__/            # artefatos Python gerados
```

How it fits together:
- app.py cria a instância Flask e registra rotas contidas em routes.py.
- routes.py chama funções em models.py para operações de persistência no SQLite e retorna templates com render_template().
- As páginas em templates/ usam os scripts em static/script/ para melhorar a experiência do usuário (envio de formulários, listas dinâmicas).

---

## How to run it
Passo a passo mínimo para rodar localmente:

1) Clonar e entrar na pasta do projeto

```
git clone https://github.com/KarolDegan/OpcaoUnica.git
cd OpcaoUnica
```

2) Instalar dependências

```
pip install -r requirements.txt
# se não houver requirements.txt ou faltar dependência: pip install flask
```

3) Iniciar a aplicação

```
python app.py
# por padrão rodará em http://localhost:5002
```

Observações sobre o banco de dados
- O arquivo projetoES3.db está incluído no repositório e é usado pela aplicação como fonte de dados.
- Se precisar recriar o banco ou popular com dados de exemplo, verifique funções em models.py e adicione um script seed/SQL conforme desejado.

---

## Observações funcionais e pontos importantes
- Rotas e templates: O projeto contém muitas rotas mapeadas diretamente para templates (ex.: /cadastrar_cliente, /visualizar_veiculo, /lista_cotacoes). Leia routes.py para ver todas as rotas e parâmetros.
- Validações: Há validações no servidor (ex.: verificação de CPF com 11 dígitos) e validações no cliente via JS.
- Segurança:
  - Credenciais de desenvolvimento estão codificadas em routes.py (ex.: USERNAME/PASSWORD). Substitua por variáveis de ambiente ou um sistema de autenticação antes de usar em produção.
  - Uso direto de sqlite3: revise o uso de consultas para garantir parametrização e evitar possíveis vulnerabilidades (sempre prefira queries parametrizadas com placeholders).
- Dependências e compatibilidade: confirme versões em requirements.txt; recomenda-se Python 3.8+.

---

## Sugestões de melhorias na documentação (recomendado adicionar ao repositório)
1. README mais detalhado (este arquivo) — já adicionado.
2. API Reference básica: lista de rotas importantes (GET/POST) com os campos esperados e exemplos de formulários/JSON.
3. Script de migração/seed do banco (ex.: scripts/init_db.py ou seed.sql) para facilitar reprodução em outra máquina.
4. Security notes: remover credenciais hard-coded, usar variáveis de ambiente, e descrever como criar um usuário administrador.
5. CONTRIBUTING.md com orientações para abrir PR, rodar linters e testes (se houver).
6. LICENSE — adicionar uma licença clara para o projeto.

---

## Endpoints / rotas — visão rápida (exemplos extraídos de routes.py)
- /login.html [GET, POST] — autenticação (form: username, password)
- /tela_inicial.html [GET]
- /clientes.html, /cadastrar_cliente (GET/POST), /consultar_cliente1.html
- /veiculo, /cadastrar_veiculo, /consultar_veiculo1.html, /visualizar_veiculo.html
- /seguradoras.html, /cadastrar_seguradora, /consultar_seguradora1.html
- /seguros.html, /cadastrar_seguros, /consultar_seguros1.html
- /cotações.html, /cadastrar_cotação, /consultar_cotação1.html

(Consulte routes.py para lista completa e nomes de campos esperados nos formulários.)

---

## Perguntas úteis (para eu documentar mais automaticamente)
1. Deseja que eu crie também um script seed (init_db.py) que recrie as tabelas e popule com exemplos a partir do schema em models.py?
2. Prefere que eu remova as credenciais hard-coded e as substitua por configuração via variáveis de ambiente no código (ex.: usar os.environ)?
3. Quer que eu gere uma referência de API/rotas automática (um arquivo ROUTES.md) com cada rota, método e campos esperados extraídos de routes.py?

---

Se quiser, eu posso:
- atualizar o README.md com exemplos de requests mais detalhados;
- adicionar um script init_db.py/seed.sql que recrie o banco projetoES3.db vazio/populado;
- criar um small HOWTO para preparar o projeto para produção (Gunicorn + variáveis de ambiente + segurança).
