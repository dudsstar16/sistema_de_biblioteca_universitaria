from views.menu import BibliotecaView
from controllers.autor_controller import AutorController
from controllers.livro_controller import LivroController

# =====================================================================
# PROGRAMA PRINCIPAL (Ponto de Entrada)
# Como funciona a brincadeira?
# 1. O sistema acorda e mostra o Menu Principal na tela.
# 2. Se a pessoa apertar 1: chama o gerente dos Autores (AutorController).
# 3. Se a pessoa apertar 2: chama o gerente dos Livros (LivroController).
# 4. Quando o gerente termina a tarefa dele, o programa volta para cá,
#    mostrando o Menu Principal novamente!
# 5. Se apertar 3: dá tchau e desliga!
# =====================================================================

def main():
    autor_ctrl = AutorController()
    livro_ctrl = LivroController()

    while True:
        opcao = BibliotecaView.menu_principal()

        if opcao == 1:
            # Vai para o submenu de gerenciar autores
            autor_ctrl.iniciar()

        elif opcao == 2:
            # Vai para o submenu de gerenciar livros
            livro_ctrl.iniciar()

        elif opcao == 3:
            # Encerra o sistema
            BibliotecaView.mensagem("Obrigado por usar o Sistema de Biblioteca Universitária. Até logo!")
            break

        else:
            BibliotecaView.mensagem("Opção inválida! Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
