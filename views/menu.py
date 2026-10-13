# =====================================================================
# VIEW: MENU E TELAS DO SISTEMA
# O que é a View?
# Imagine que a View é a "TV" ou a "tela" do nosso programa.
# Ela é a ÚNICA que conversa diretamente com a pessoa:
# - Mostra menus e mensagens bonitas (com print).
# - Pede para a pessoa digitar números e textos (com input).
# A View NÃO mexe no banco de dados e NÃO toma decisões difíceis.
# =====================================================================

class BibliotecaView:

    # -------------------------------------------------------------
    # 1. MENUS PRINCIPAL E SECUNDÁRIOS
    # -------------------------------------------------------------

    @staticmethod
    def menu_principal():
        """
        Exibe a tela inicial com as opções principais.
        Retorna o número que a pessoa escolheu.
        """
        print("\n" + "=" * 30)
        print("       MENU PRINCIPAL")
        print("=" * 30)
        print("1. Gerenciar autor")
        print("2. Gerenciar livro")
        print("3. Sair")
        print("-" * 30)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    @staticmethod
    def menu_autor():
        """
        Exibe a tela com as opções para gerenciar autores.
        Retorna o número que a pessoa escolheu.
        """
        print("\n" + "=" * 30)
        print("       GERENCIAR AUTOR")
        print("=" * 30)
        print("1. Cadastrar autor")
        print("2. Listar autores")
        print("3. Atualizar autor")
        print("4. Excluir autor")
        print("5. Voltar ao menu principal")
        print("-" * 30)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    @staticmethod
    def menu_livro():
        """
        Exibe a tela com as opções para gerenciar livros.
        Retorna o número que a pessoa escolheu.
        """
        print("\n" + "=" * 30)
        print("       GERENCIAR LIVRO")
        print("=" * 30)
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar livro")
        print("4. Excluir livro")
        print("5. Voltar ao menu principal")
        print("-" * 30)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    # -------------------------------------------------------------
    # 2. TELAS DE AUTOR (Entrada e Saída)
    # -------------------------------------------------------------

    @staticmethod
    def cadastrar_autor():
        """
        Pergunta os dados de um novo autor para a pessoa.
        """
        print("\n--- Cadastrar Novo Autor ---")
        nome = input("Nome do autor: ").strip()
        nacionalidade = input("Nacionalidade do autor: ").strip()

        if not nome or not nacionalidade:
            print("\n[Aviso] Nome e nacionalidade não podem ficar vazios!")
            return None, None

        return nome, nacionalidade

    @staticmethod
    def listar_autores(autores):
        """
        Mostra a lista de autores na tela de forma organizada.
        """
        if not autores:
            print("\nNenhum autor cadastrado até o momento.")
            return

        print("\n" + "=" * 55)
        print("                  LISTA DE AUTORES")
        print("=" * 55)
        for a in autores:
            # a[0] = id, a[1] = nome, a[2] = nacionalidade
            print(f"ID: {a[0]} | Nome: {a[1]} | Nacionalidade: {a[2]}")
        print("=" * 55)

    @staticmethod
    def atualizar_autor():
        """
        Pergunta qual autor atualizar e quais serão os novos dados.
        """
        print("\n--- Atualizar Dados do Autor ---")
        try:
            id_autor = int(input("ID do autor que deseja atualizar: "))
            nome = input("Novo nome do autor: ").strip()
            nacionalidade = input("Nova nacionalidade: ").strip()

            if not nome or not nacionalidade:
                print("\n[Aviso] Nome e nacionalidade não podem ficar vazios!")
                return None, None, None

            return nome, nacionalidade, id_autor
        except ValueError:
            print("\n[Erro] O ID precisa ser um número inteiro.")
            return None, None, None

    @staticmethod
    def excluir_autor():
        """
        Pergunta o ID do autor que a pessoa quer deletar.
        """
        print("\n--- Excluir Autor ---")
        try:
            id_autor = int(input("Digite o ID do autor a ser excluído: "))
            return id_autor
        except ValueError:
            print("\n[Erro] O ID precisa ser um número inteiro.")
            return None

    # -------------------------------------------------------------
    # 3. TELAS DE LIVRO (Entrada e Saída)
    # -------------------------------------------------------------

    @staticmethod
    def cadastrar_livro():
        """
        Pergunta os dados de um novo livro para a pessoa.
        """
        print("\n--- Cadastrar Novo Livro ---")
        titulo = input("Título do livro: ").strip()
        if not titulo:
            print("\n[Aviso] O título não pode ficar vazio!")
            return None, None, None

        try:
            ano = int(input("Ano de publicação: "))
            id_autor = int(input("ID do autor do livro: "))
            return titulo, ano, id_autor
        except ValueError:
            print("\n[Erro] Ano e ID do autor devem ser números inteiros.")
            return None, None, None

    @staticmethod
    def listar_livros(livros):
        """
        Mostra a lista de livros na tela com o nome do autor associado.
        """
        if not livros:
            print("\nNenhum livro cadastrado até o momento.")
            return

        print("\n" + "=" * 65)
        print("                        LISTA DE LIVROS")
        print("=" * 65)
        for l in livros:
            # l[0] = id, l[1] = titulo, l[2] = ano, l[3] = nome do autor
            autor_nome = l[3] if l[3] else "Autor não encontrado"
            print(f"ID: {l[0]} | Título: {l[1]} | Ano: {l[2]} | Autor Associado: {autor_nome}")
        print("=" * 65)

    @staticmethod
    def atualizar_livro():
        """
        Pergunta qual livro atualizar e os novos dados.
        """
        print("\n--- Atualizar Dados do Livro ---")
        try:
            id_livro = int(input("ID do livro que deseja atualizar: "))
            titulo = input("Novo título do livro: ").strip()
            if not titulo:
                print("\n[Aviso] O título não pode ficar vazio!")
                return None, None, None, None

            ano = int(input("Novo ano de publicação: "))
            id_autor = int(input("Novo ID do autor: "))
            return titulo, ano, id_autor, id_livro
        except ValueError:
            print("\n[Erro] Entrada inválida. Ano, ID do livro e ID do autor devem ser números.")
            return None, None, None, None

    @staticmethod
    def excluir_livro():
        """
        Pergunta o ID do livro a ser excluído.
        """
        print("\n--- Excluir Livro ---")
        try:
            id_livro = int(input("Digite o ID do livro a ser excluído: "))
            return id_livro
        except ValueError:
            print("\n[Erro] O ID precisa ser um número inteiro.")
            return None

    # -------------------------------------------------------------
    # 4. MENSAGEM GERAL
    # -------------------------------------------------------------

    @staticmethod
    def mensagem(msg):
        """
        Mostra qualquer aviso ou mensagem de sucesso/erro na tela.
        """
        print(f"\n=> {msg}")
