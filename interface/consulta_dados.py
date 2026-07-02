from src.consulta import (
    Listar_Calendario, 
    jogos_por_grupo, 
    jogos_por_fase, 
    jogos_por_id, 
    consulta_palpite
    )

from gabarito import (
    Visualizar_Gabarito_Oficial,
    Visualizar_Resultados_Pendentes
    )

from armazenamento.manipulacao_arquivo_gabarito import Carregar_Gabarito

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
        return False

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
    #elif opcao == "6":
    elif opcao == "7":
        Visualizar_Gabarito_Oficial(jogos_gabarito)
    elif opcao == "8":
        Visualizar_Resultados_Pendentes(jogos_gabarito)
    else:
        print("Pressionou o numero errado paezao.")

    input("\nPressione enter para continuar...")
