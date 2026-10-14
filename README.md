# 📚 Sistema de Biblioteca Universitária

Projeto desenvolvido em **Python** integrado ao banco de dados relacional **PostgreSQL**, estruturado no padrão de arquitetura **MVC (Model-View-Controller)** para gerenciamento completo de autores e livros de uma biblioteca.

---

## 🎥 Demonstração em Vídeo

O vídeo com o teste completo de todas as funções do sistema em execução está disponível diretamente no repositório:

👉 **[Clique aqui para assistir: video_do_programa_em_execucao.mp4](video_do_programa_em_execucao.mp4)**

*(O GitHub reproduz o vídeo diretamente no navegador).*

---

## ✨ O que o sistema faz?

O programa roda via linha de comando com menus interativos e navegação por loops, oferecendo um CRUD completo:

### ✍️ Gerenciamento de Autores
- **Cadastrar autor**: Registro com validação de nome e nacionalidade obrigatórios.
- **Listar autores**: Tabela organizada com ID, nome e nacionalidade.
- **Atualizar autor**: Edição dos dados pelo ID.
- **Excluir autor**: Exclusão com proteção de integridade (impede deletar autor que ainda possui livros vinculados).

### 📖 Gerenciamento de Livros
- **Cadastrar livro**: Registro de título, ano de publicação e vínculo ao ID do autor existente (com validação de chave estrangeira).
- **Listar livros**: Listagem detalhada utilizando `LEFT JOIN` para exibir o nome do autor associado ao invés de apenas seu ID.
- **Atualizar livro**: Edição dos dados e reatribuição de autor.
- **Excluir livro**: Remoção individual de livros do acervo.

### 🛡️ Tratamento de Erros e Segurança
- Validações de entradas (impede campos vazios e letras onde são esperados números).
- Tratamento de exceções com rollback automático no banco para evitar transações travadas.
- Tratamento de `ForeignKeyViolation` (avisa de forma amigável quando um autor não existe ou quando há dependência de livros).

---

## 📁 Estrutura do Repositório (Padrão MVC)

```text
sistema_de_biblioteca_universitaria/
│
├── controllers/                  # 🎮 Camada de Controle
│   ├── autor_controller.py       # Gerencia o fluxo e regras das opções de autores
│   └── livro_controller.py       # Gerencia o fluxo e regras das opções de livros
│
├── models/                       # 🗄️ Camada de Modelo (Acesso ao Banco)
│   ├── autor_model.py            # Queries e operações SQL da tabela 'autor'
│   └── livro_model.py            # Queries, JOINs e operações SQL da tabela 'livro'
│
├── views/                        # 🖥️ Camada de Visão (Interface com o Usuário)
│   └── menu.py                   # Menus no terminal, entradas (inputs) e saídas formatadas
│
├── banco.sql                     # 📜 Script DDL de criação do banco e tabelas no PostgreSQL
├── main.py                       # 🚀 Ponto de entrada que inicia a aplicação
├── requirements.txt              # 📦 Dependências do Python
├── video_do_programa_em_execucao.mp4  # 🎬 Vídeo demonstrativo da execução
└── .gitignore                    # 🙈 Arquivos ignorados pelo Git
```

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11+
- **Banco de Dados:** PostgreSQL
- **Conector:** `psycopg2-binary`
- **Padrão de Projeto:** MVC (Model-View-Controller)

---

## 🚀 Como Executar o Projeto

Siga o passo a passo abaixo para rodar o projeto em sua máquina:

### 1. Clonar o repositório
```bash
git clone https://github.com/dudsstar16/sistema_de_biblioteca_universitaria.git
cd sistema_de_biblioteca_universitaria
```

### 2. Configurar o Banco de Dados (PostgreSQL)
1. Abra o **pgAdmin** ou o terminal `psql`.
2. Crie a base de dados:
   ```sql
   CREATE DATABASE biblioteca_universitaria;
   ```
3. Conecte-se ao banco `biblioteca_universitaria` e execute o script contido em [banco.sql](banco.sql).

*(Opcional: o arquivo [banco.sql](banco.sql) possui linhas comentadas no final caso queira inserir alguns dados iniciais de teste).*

### 3. Verificar Credenciais de Acesso
Por padrão, o projeto conecta com as seguintes credenciais nos arquivos `models/autor_model.py` e `models/livro_model.py`:
- **Host:** `localhost`
- **Database:** `biblioteca_universitaria`
- **User:** `postgres`
- **Password:** `1234`

> Caso sua senha do PostgreSQL local seja diferente de `1234`, altere o campo `password` no método `__init__` desses dois arquivos.

### 4. Instalar as Dependências
Com o Python instalado, instale o driver de conexão com o PostgreSQL:
```bash
pip install -r requirements.txt
```

### 5. Iniciar a Aplicação
Execute o arquivo principal:
```bash
python main.py
```

O menu principal será carregado no terminal e estará pronto para uso! 🚀

---

## 👥 Autores e Colaboradores

Projeto acadêmico desenvolvido em equipe por:

- **Eduarda Reis** ([@dudsstar16](https://github.com/dudsstar16))
- **Alderiana** ([@alderiana](https://github.com/alderiana))

