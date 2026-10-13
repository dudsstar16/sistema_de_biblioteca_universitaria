from models.livro_model import Livro
from views.menu import BibliotecaView

# =====================================================================
# CONTROLLER: LIVRO
# O que é o Controller?
# É o cérebro que cuida dos livros:
# - Ele pergunta o que a pessoa quer no menu de livros (View).
# - Manda o Model fazer a busca, cadastro, edição ou exclusão.
# - Devolve o resultado formatado para a tela (View).
# O submenu também fica em repetição contínua (loop) até escolher voltar.
# =====================================================================

class LivroController:
    def __init__(self):
        self.model = Livro()
        self.view = BibliotecaView

    def iniciar(self):
        """
        Inicia o submenu de Livro e fica em loop até o usuário escolher voltar (opção 5).
        """
        while True:
            opcao = self.view.menu_livro()

            if opcao == 1:
                # 1. Cadastrar livro
                titulo, ano, id_autor = self.view.cadastrar_livro()
                if titulo and ano is not None and id_autor is not None:
                    sucesso = self.model.cadastrar_livro(titulo, ano, id_autor)
                    if sucesso:
                        self.view.mensagem("Livro cadastrado com sucesso!")

            elif opcao == 2:
                # 2. Listar livros (mostra o autor associado)
                livros = self.model.listar_livro()
                self.view.listar_livros(livros)

            elif opcao == 3:
                # 3. Atualizar livro
                titulo, ano, id_autor, id_livro = self.view.atualizar_livro()
                if id_livro is not None and titulo and ano is not None and id_autor is not None:
                    sucesso = self.model.atualizar_livro(titulo, ano, id_autor, id_livro)
                    if sucesso:
                        self.view.mensagem("Livro atualizado com sucesso!")

            elif opcao == 4:
                # 4. Excluir livro
                id_livro = self.view.excluir_livro()
                if id_livro is not None:
                    sucesso = self.model.excluir_livro(id_livro)
                    if sucesso:
                        self.view.mensagem("Livro excluído com sucesso!")

            elif opcao == 5:
                # 5. Voltar ao menu principal
                self.view.mensagem("Retornando ao Menu Principal...")
                break

            else:
                self.view.mensagem("Opção inválida! Por favor, digite um número entre 1 e 5.")
