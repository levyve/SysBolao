from src.partidas import Gerar_Primeira_Fase, Carregar_Selecoes, Encontrar_Jogo
from src.apostador import Cadastrar_Apostador
from src.consulta import Listar_Calendario, jogos_por_grupo, jogos_por_fase, jogos_por_id, consulta_palpite
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
    if opcao == "1":
        Listar_Calendario()
    if opcao == "2":
        jogos_por_fase()
    if opcao == "3":
        jogos_por_grupo()
    if opcao == "4":
        Encontrar_Jogo()
    if opcao == "5":
        consulta_palpite()
    if opcao == "6":
        Palpites_Pendentes()
    if opcao == "7":
        Gabarito_Oficial()
    if opcao == "8":
        Resultados_Pendentes()
    if opcao == "9":
        Menu_Principal()

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
            Gerar_Primeira_Fase(Carregar_Selecoes('Archives/txt/selecoes.tx'))
            input('Selecoes carregadas, Primeira Fase gerada. Pressione enter para continuar \n')
        except:
            input('Erro ao Carregar as selecoes e gerar Fase, Pressione enter para continuar')
    if opcao == "2":
       Cadastrar_Apostador()
    if opcao == "3":
        Registrar_Palpites()
    if opcao == "4":
        Completar_Palpites()
    if opcao == "5":
        Gerar_Fase()
    if opcao == "6":
        Cadastrar_Gabarito()
    if opcao == "7":
        Consultar_Pontuacao()
    if opcao == "8":
        Resultado_Final()
    if opcao == "9":
        Consultar_Dados()
        return None
    if opcao == "10": 
        return None
    Menu_Principal()
    

Menu_Principal()