import psycopg2

# =====================================================================
# MODEL: LIVRO
# O que é o Model?
# É o responsável por guardar, buscar, atualizar e deletar os livros
# na tabela 'livro' do banco de dados PostgreSQL.
# Repare que cada livro tem uma ligação com um Autor (id_autor).
# =====================================================================

class Livro:
    def __init__(self):
        """
        Ao criar um objeto Livro, nós nos conectamos ao banco de dados.
        """
        self.conexao = None
        try:
            self.conexao = psycopg2.connect(
                host="localhost",   
                database="biblioteca_universitaria",
                user="postgres",
                password="1234"
            )
        except psycopg2.Error as e:
            print(f"\n[Aviso] Erro ao conectar ao banco de dados: {e}")

    def cadastrar_livro(self, titulo, ano_publicacao, id_autor):
        """
        Salva um novo livro no banco de dados.
        Recebe: título, ano de publicação e o ID do autor que escreveu.
        """
        if not self.conexao:
            print("\n[Erro] Sem conexão com o banco de dados.")
            return False

        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "INSERT INTO livro (titulo, ano_publicacao, id_autor) VALUES (%s, %s, %s)", 
                (titulo, ano_publicacao, id_autor)
            )
            self.conexao.commit()
            cursor.close()
            return True
        except psycopg2.errors.ForeignKeyViolation:
            if self.conexao:
                self.conexao.rollback()
            print(f"\n[Aviso] O autor com ID {id_autor} não existe! Cadastre o autor primeiro.")
            return False
        except psycopg2.Error as e:
            if self.conexao:
                self.conexao.rollback()
            print(f"\n[Erro ao cadastrar livro]: {e}")
            return False

    def listar_livro(self):
        """
        Busca todos os livros e traz o NOME DO AUTOR junto (usando JOIN).
        Retorna: lista de tuplas contendo (id, titulo, ano_publicacao, nome_autor).
        """
        if not self.conexao:
            print("\n[Erro] Sem conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            # O LEFT JOIN junta a tabela livro com a tabela autor
            # pelo campo l.id_autor = a.id para mostrar o nome do autor!
            cursor.execute("""
                SELECT l.id, l.titulo, l.ano_publicacao, a.nome 
                FROM livro l
                LEFT JOIN autor a ON l.id_autor = a.id
                ORDER BY l.id
            """)
            livros = cursor.fetchall()
            cursor.close()
            return livros
        except psycopg2.Error as e:
            if self.conexao:
                self.conexao.rollback()
            print(f"\n[Erro ao listar livros]: {e}")
            return []

    def atualizar_livro(self, titulo, ano_publicacao, id_autor, id_livro):
        """
        Atualiza os dados de um livro existente.
        Recebe: novo título, novo ano, novo id_autor e o id_livro.
        """
        if not self.conexao:
            print("\n[Erro] Sem conexão com o banco de dados.")
            return False

        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "UPDATE livro SET titulo = %s, ano_publicacao = %s, id_autor = %s WHERE id = %s", 
                (titulo, ano_publicacao, id_autor, id_livro)
            )
            self.conexao.commit()
            linhas_afetadas = cursor.rowcount
            cursor.close()
            if linhas_afetadas == 0:
                print(f"\n[Aviso] Nenhum livro encontrado com o ID {id_livro}.")
                return False
            return True
        except psycopg2.errors.ForeignKeyViolation:
            if self.conexao:
                self.conexao.rollback()
            print(f"\n[Aviso] O autor com ID {id_autor} não existe! Verifique o ID do autor.")
            return False
        except psycopg2.Error as e:
            if self.conexao:
                self.conexao.rollback()
            print(f"\n[Erro ao atualizar livro]: {e}")
            return False

    def excluir_livro(self, id_livro):
        """
        Exclui um livro pelo seu ID.
        """
        if not self.conexao:
            print("\n[Erro] Sem conexão com o banco de dados.")
            return False

        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM livro WHERE id = %s", (id_livro,))
            self.conexao.commit()
            linhas_afetadas = cursor.rowcount
            cursor.close()
            if linhas_afetadas == 0:
                print(f"\n[Aviso] Nenhum livro encontrado com o ID {id_livro}.")
                return False
            return True
        except psycopg2.Error as e:
            if self.conexao:
                self.conexao.rollback()
            print(f"\n[Erro ao deletar livro]: {e}")
            return False
