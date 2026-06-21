from src.apostador import Carregar_Palpites, Atualizar_Palpites
from src.partidas import Encontrar_Jogo, Exibir_Jogo

def Sub_Menu_Interativo(apostador: str):
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

            print("""
            =========================================
                     LISTA DE TODOS OS JOGOS      
            =========================================
            """)

            for jogo in jogos:
                Exibir_Jogo(jogo)

                print(f"""
    Seu palpite:
    {jogo['selecao1']} {jogo['gols1']} x {jogo['gols2']} {jogo['selecao2']}
            """)
                
                print("""
    -----------------------------------------""")

        elif (int(opcao) == 2):
            
            print("""
            ========================================
                       JOGOS SEM PALPITES      
            ========================================
            """)
            
            for jogo in jogos:
                if(jogo['gols1'] == -1 or jogo['gols2'] == -1):
                    Exibir_Jogo(jogo)

                    print(f"""
    Palpite:
    {jogo['selecao1']} {jogo['gols1']} x {jogo['gols2']} {jogo['selecao2']}
                """)
                    
                    print("""
    -----------------------------------------""")

        elif (int(opcao) == 3):
            
            id_partida = input("Digite o ID do jogo: ")
            while (not id_partida.isdigit()):
                print("ERRO! O ID informado não é um ID válido.")
                id_partida = input("Por favor, digite um ID válido (Número): ")
            
            jogo = Encontrar_Jogo(jogos, id_partida)
            if (jogo == None):
                continue
            
            print("""
    Jogo encontrado:""")

            Exibir_Jogo(jogo)

            print(f"""
    Palpite atual:
    {jogo['selecao1']} {jogo['gols1']} x {jogo['gols2']} {jogo['selecao2']}
            """)
            
            novo_gols1 = input(f"Digite o número de gols do {jogo['selecao1']}: ")
            while (not novo_gols1.isdigit()):
                print("\nERRO! O número de gols informado não é um número.")
                id_partida = input(f"Por favor, digite uma quantidade de gols válida para {jogo['selecao1']}: ")
            
            novo_gols2 = input(f"Digite o número de gols do {jogo['selecao2']}: ")
            while (not novo_gols2.isdigit()):
                print("\nERRO! O número de gols informado não é um número.")
                id_partida = input(f"Por favor, digite uma quantidade de gols válida para {jogo['selecao2']}: ")

            Atualizar_Palpites(apostador, jogos, id_partida, novo_gols1, novo_gols2)

            print("\nPalpite cadastrado com sucesso!")
            print(f"\n{jogo['selecao1']} {novo_gols1} x {novo_gols2} {jogo['selecao2']}")

        elif (int(opcao) == 4):
            break