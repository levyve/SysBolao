from armazenamento.manipulacao_arquivos_apostador import (
    Carregar_Palpites,
)

from src.palpites import (
    Listar_Bolao_Completo_Apostador,
    Listar_Jogos_Pendentes_Apostador,
    Cadastrar_Placar
)


def SubMenu_Interativo(apostador: str):
    """Submenu Interativo no qual o apostador pode listar jogos de seu bolão e alterar/cadastrar o placar de um jogo específico.

    :param apostador: nome do apostador.
    :type apostador: str
    """

    while (True):
        print(f"""
        ******** Palpites de {apostador} ********
        1. Listar todos os jogos do bolão
        2. Listar apenas jogos sem palpite
        3. Cadastrar ou alterar placar de um jogo
        4. Voltar ao menu principal
        """)

        opcao = input("Digite a opção desejada: ")
        while(len(opcao) != 1 or not opcao.isdigit()):
            print("\nErro: A opção inválida (opção não está entre as oferecidas, ou a opção digitada não é um número)")
            opcao = input("Por favor, digite uma opção válida: ")
        
        
        jogos = Carregar_Palpites(apostador)
        if (int(opcao) == 1):
            Listar_Bolao_Completo_Apostador(jogos)

        elif (int(opcao) == 2):
            Listar_Jogos_Pendentes_Apostador(jogos)

        elif (int(opcao) == 3):
            Cadastrar_Placar(jogos, apostador)
            if (not Cadastrar_Placar):
                continue

        elif (int(opcao) == 4):
            break

