import psycopg2

# =====================================================================
# MODEL: AUTOR
# O que é o Model?
# Imagine que o Model é o "guardião do depósito" (banco de dados).
# É ele quem sabe como guardar, procurar, mudar e apagar informações
# dos autores no banco de dados PostgreSQL.
# =====================================================================

class Autor:
    def __init__(self):
        """
        Ao criar um objeto Autor, nós nos conectamos ao banco de dados.
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

    def cadastrar_autor(self, nome, nacionalidade):
        """
        Guarda um novo autor no banco de dados.
        Recebe: nome e nacionalidade.
        """
        if not self.conexao:
            print("\n[Erro] Sem conexão com o banco de dados.")
            return False

        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s)",
                (nome, nacionalidade)
            )
            self.conexao.commit()
            cursor.close()
            return True
        except psycopg2.Error as e:
            # O rollback cancela a transação com erro para não travar o banco!
            if self.conexao:
                self.conexao.rollback()
            print(f"\n[Erro ao cadastrar autor]: {e}")
            return False

    def listar_autor(self):
        """
        Busca todos os autores cadastrados na tabela 'autor'.
        Retorna uma lista com os autores encontrados.
        """
        if not self.conexao:
            print("\n[Erro] Sem conexão com o banco de dados.")
            return []

        try:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id, nome, nacionalidade FROM autor ORDER BY id")
            autores = cursor.fetchall()
            cursor.close()
            return autores
        except psycopg2.Error as e:
            if self.conexao:
                self.conexao.rollback()
            print(f"\n[Erro ao listar autores]: {e}")
            return []

    def atualizar_autor(self, nome, nacionalidade, id_autor):
        """
        Altera as informações de um autor que já existe.
        Recebe: novo nome, nova nacionalidade e o ID do autor.
        """
        if not self.conexao:
            print("\n[Erro] Sem conexão com o banco de dados.")
            return False

        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                "UPDATE autor SET nome = %s, nacionalidade = %s WHERE id = %s",
                (nome, nacionalidade, id_autor)
            )
            self.conexao.commit()
            linhas_afetadas = cursor.rowcount
            cursor.close()
            if linhas_afetadas == 0:
                print(f"\n[Aviso] Nenhum autor encontrado com o ID {id_autor}.")
                return False
            return True
        except psycopg2.Error as e:
            if self.conexao:
                self.conexao.rollback()
            print(f"\n[Erro ao atualizar autor]: {e}")
            return False

    def excluir_autor(self, id_autor):
        """
        Remove um autor do banco de dados pelo seu ID.
        """
        if not self.conexao:
            print("\n[Erro] Sem conexão com o banco de dados.")
            return False

        try:
            cursor = self.conexao.cursor()
            cursor.execute("DELETE FROM autor WHERE id = %s", (id_autor,))
            self.conexao.commit()
            linhas_afetadas = cursor.rowcount
            cursor.close()
            if linhas_afetadas == 0:
                print(f"\n[Aviso] Nenhum autor encontrado com o ID {id_autor}.")
                return False
            return True
        except psycopg2.errors.ForeignKeyViolation:
            # Esse erro acontece quando o autor tem livros cadastrados!
            if self.conexao:
                self.conexao.rollback()
            print(f"\n[Aviso] Não é possível excluir o autor ID {id_autor} pois ele possui livro(s) cadastrado(s)!")
            print("=> Para excluir este autor, você deve excluir primeiro os livros dele no menu 'Gerenciar livro'.")
            return False
        except psycopg2.Error as e:
            if self.conexao:
                self.conexao.rollback()
            print(f"\n[Erro ao excluir autor]: {e}")
            return False
