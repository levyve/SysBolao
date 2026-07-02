from src.partidas import (
    Carregar_Selecoes,
    Gerar_Primeira_Fase,
    Gerar_Proxima_Fase,
    )

from src.apostador import (
    Cadastrar_Apostador,
    Completar_Palpites_Aleatoriamente,
    Validar_Jogador,
    Carregar_Palpites,
    Atualizar_Arquivo_Palpites,
    )

from src.submenu_registrar_palpites import (
    Cadastrar_Palpites
    )
from src.gabarito import (
    Cadastrar_Gabarito,
    Carregar_Gabarito,
    Atualizar_Arquivo_Gabarito,
    Visualizar_Gabarito_Oficial,
    Visualizar_Resultados_Pendentes,
    )

from src.consulta import (
    Listar_Calendario, 
    jogos_por_grupo, 
    jogos_por_fase, 
    jogos_por_id, 
    consulta_palpite,
    consulta_palpite_pendentes,
    )

from src.classificacao import (
    Resultado_Final_Bolao,
    Calcular_Pontuacao_Apostador,
    relatorio_completo,

    )


def Consultar_Dados():
    print("\n******** Consulta de Dados ********")
    print("1. Listar calendário completo de jogos")
    print("2. Listar jogos por fase")
    print("3. Listar jogos por grupo")
    print("4. Buscar jogo por ID")
    print("5. Visualizar palpites de um apostador")
    print("6. Visualizar apenas palpites pendentes de um apostador")
    print("7. Visualizar gabarito oficial")
    print("8. Visualizar resultados pendentes no gabarito")
    print("9. Voltar ao menu principal")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "9":
        Menu_Principal()
        return

    try:
        jogos_gabarito = Carregar_Gabarito()
    except:
        jogos_gabarito = None

    if opcao in ["1", "2", "3", "4"] and jogos_gabarito is None:
        print("ERRO: o gabarito oficial ainda não foi criado.")
    elif opcao == "1":
        Listar_Calendario(jogos_gabarito)
    elif opcao == "2":
        jogos_por_fase(jogos_gabarito)
    elif opcao == "3":
        jogos_por_grupo(jogos_gabarito)
    elif opcao == "4":
        jogos_por_id(jogos_gabarito)
    elif opcao == "5":
        consulta_palpite()
    elif opcao == "6":
        consulta_palpite_pendentes()
    elif opcao == "7":
        Visualizar_Gabarito_Oficial(jogos_gabarito)
    elif opcao == "8":
        Visualizar_Resultados_Pendentes(jogos_gabarito)
    else:
        print("Pressionou o numero errado paezao.")

    input("\nPressione enter para continuar...")
    Consultar_Dados()


def Menu_Principal():
    print("\n==========================================")
    print("          SISTEMA BOLÃO DA COPA           ")
    print("==========================================")
    print("1. Carregar Seleções")
    print("2. Cadastrar Apostador")
    print("3. Registrar Palpites")
    print("4. Completar Palpites Aleatoriamente")
    print("5. Gerar Próxima Fase")
    print("6. Cadastrar Gabarito")
    print("7. Consultar Pontuação de Apostador")
    print("8. Resultado Final do Bolão")
    print("9. Consultar Dados do Sistema")
    print("10. Sair")
    print("==========================================")
    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        try:
            Carregar_Selecoes('Archives/txt/selecoes.txt')
            input('Seleções carregadas, Primeira Fase gerada. Pressione enter para continuar \n')
        except:
            input('Erro ao carregar as seleções e gerar Fase. Pressione enter para continuar')

    elif opcao == "2":
        apostador = input("Insira o nome do novo apostador: ")
        Cadastrar_Apostador(apostador)

    elif opcao == "3":
        modo = input("Escolha o modo de cadastro de palpites (A - Interativo / B - Lote): ")
        Cadastrar_Palpites(modo)

    elif opcao == "4":
        apostador = input("Nome do apostador: ")
        if Validar_Jogador(apostador):
            jogos = Carregar_Palpites(apostador)
            Completar_Palpites_Aleatoriamente(apostador, jogos)
        else:
            print("Erro! Apostador não cadastrado no sistema.")

    elif opcao == "5":
        try:
            jogos_gabarito = Carregar_Gabarito()
        except :
            input("o gabarito oficial provavelmente nao foi criado. Pressione enter para continuar")
        else:
            novos_jogos = Gerar_Proxima_Fase(jogos_gabarito)
            if novos_jogos is None:
                input("Ainda há jogos pendentes. Pressione enter para continuar")
            else:
                Atualizar_Arquivo_Gabarito(jogos_gabarito + novos_jogos)
                with open('Archives/txt/apostadores.txt', 'r', encoding='utf-8') as arq:
                    apostadores = [linha.strip() for linha in arq if linha.strip() != ""]
                for apostador in apostadores:
                    try:
                        jogos_apostador = Carregar_Palpites(apostador)
                        Atualizar_Arquivo_Palpites(jogos_apostador + novos_jogos, apostador)
                    except:
                        pass
                input("Próxima fase gerada com sucesso! Pressione enter para continuar")

    elif opcao == "6":
        Cadastrar_Gabarito()

    elif opcao == "7":
        apostador = input("Nome do apostador: ")
        try:
            jogos_gabarito = Carregar_Gabarito()
        except :
            input("ERRO: o gabarito oficial ainda não foi criado. Pressione enter para continuar")
        else:
            estatisticas = Calcular_Pontuacao_Apostador(apostador, jogos_gabarito)
            print(f"""
    Pontuação de {apostador}:
    Pontos: {estatisticas['pontos']}
    Exatos: {estatisticas['exatos']}
    Parciais: {estatisticas['parciais']}
    Resultados: {estatisticas['resultados']}
    Erros: {estatisticas['erros']}
            """)
            expandir = input(" digite 1 para voltar ao menu \ndigte 2 para ver a comparação de todos os jogos do bolão com os resultados oficiais")
            if expandir == "2":
                relatorio_completo(apostador, jogos_gabarito)

    elif opcao == "8":
        Resultado_Final_Bolao()

    elif opcao == "9":
        Consultar_Dados()
        return

    elif opcao == "10":
        print("Saindo do sistema. Até mais!")
        return

    else:
        print("ERRO: a opção selecionada não existe.")

    Menu_Principal()


Menu_Principal()