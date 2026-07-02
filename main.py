from armazenamento.manipulacao_arquivos_apostador import (
    Carregar_Palpites,
    Cadastrar_Apostador,
    Atualizar_Arquivo_Palpites,
    )

from armazenamento.manipulacao_arquivos_partidas import (
    Carregar_Selecoes,
    Criar_Arquivo_Padrao,
)

from armazenamento.manipulacao_arquivo_gabarito import (
    Carregar_Gabarito,
    Atualizar_Arquivo_Gabarito
    )

from src.partidas import (
    Gerar_Primeira_Fase,
    Gerar_Proxima_Fase,
    )

from src.palpites import (
    Completar_Palpites_Aleatoriamente,
    Exibir_Tutorial_Cadastro_Lote
    )

from src.utilitários import (
    Validar_Apostador, 
    Existe_Gabarito
    )

from src.gabarito import Cadastrar_Gabarito

from classificacao_apostadores import (
    Resultado_Final_Bolao,
    Calcular_Pontuacao_Apostador,
    Relatorio_Completo
    )

from interface.menu_cadastro_palpites import SubMenu_Interativo
from interface.consulta_dados import Consultar_Dados


def Menu_Principal():
    while (True):

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
                Carregar_Selecoes()
                input('Seleções carregadas, Primeira Fase gerada. Pressione enter para continuar \n')
            except:
                input('Erro ao carregar as seleções e gerar Fase. Pressione enter para continuar')

        elif opcao == "2":
            apostador = input("Insira o nome do novo apostador: ")
            Cadastrar_Apostador(apostador)

        elif opcao == "3":
            modo = input("Escolha o modo de cadastro de palpites (A - Interativo / B - Lote): ")
            
            if (modo.lower() != 'a' and modo.lower() != 'b'):
                print("ERRO: jogador não selecionou uma opção válida!")
                continue
                    
            apostador = input("Nome do apostador: ")
            if (modo.lower() == 'a'):

                if (Validar_Apostador(apostador)):
                    SubMenu_Interativo(apostador)
                    
                else:
                    print("Erro! Apostador não cadastrado no sistema.")
                    continue
            else:
                Exibir_Tutorial_Cadastro_Lote(apostador)
                break
            

        elif opcao == "4":
            apostador = input("Nome do apostador: ")
            if Validar_Apostador(apostador):
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
            if (not Existe_Gabarito):
                print("ERRO: o gabarito oficial ainda não foi criado. Pressione enter para continuar")
                continue
        
            apostador = input("Nome do apostador: ")
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
                Relatorio_Completo(apostador, jogos_gabarito)

        elif opcao == "8":
            Resultado_Final_Bolao()

        elif opcao == "9":
            Consultar_Dados()
            continue

        elif opcao == "10":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("ERRO: a opção selecionada não existe.")


Menu_Principal()