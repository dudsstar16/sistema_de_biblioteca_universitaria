from models.autor_model import Autor
from views.menu import BibliotecaView

# =====================================================================
# CONTROLLER: AUTOR
# O que é o Controller?
# Imagine que o Controller é o "gerente":
# - Ele ouve o que o cliente quer na tela (View).
# - Ele vai até o depósito (Model) e pede para fazer o que foi pedido.
# - Depois volta e mostra a resposta na tela (View).
# O submenu fica rodando em loop (repetição) até o usuário pedir para voltar.
# =====================================================================

class AutorController:
    def __init__(self):
        self.model = Autor()
        self.view = BibliotecaView

    def iniciar(self):
        """
        Inicia o submenu de Autor e fica em loop até o usuário escolher voltar (opção 5).
        """
        while True:
            opcao = self.view.menu_autor()

            if opcao == 1:
                # 1. Cadastrar autor
                nome, nacionalidade = self.view.cadastrar_autor()
                if nome and nacionalidade:
                    sucesso = self.model.cadastrar_autor(nome, nacionalidade)
                    if sucesso:
                        self.view.mensagem("Autor cadastrado com sucesso!")

            elif opcao == 2:
                # 2. Listar autores
                autores = self.model.listar_autor()
                self.view.listar_autores(autores)

            elif opcao == 3:
                # 3. Atualizar autor
                nome, nacionalidade, id_autor = self.view.atualizar_autor()
                if id_autor is not None and nome and nacionalidade:
                    sucesso = self.model.atualizar_autor(nome, nacionalidade, id_autor)
                    if sucesso:
                        self.view.mensagem("Autor atualizado com sucesso!")

            elif opcao == 4:
                # 4. Excluir autor
                id_autor = self.view.excluir_autor()
                if id_autor is not None:
                    sucesso = self.model.excluir_autor(id_autor)
                    if sucesso:
                        self.view.mensagem("Autor excluído com sucesso!")

            elif opcao == 5:
                # 5. Voltar ao menu principal
                self.view.mensagem("Retornando ao Menu Principal...")
                break

            else:
                self.view.mensagem("Opção inválida! Por favor, digite um número entre 1 e 5.")
