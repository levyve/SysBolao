from src.partidas import GerarPrimeiraFase, CarregarSelecoes
from src.apostador import CadastrarApostador
def ConsultarDados():
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
        ListarCalendario()
    if opcao == "2":
        ListarFase()
    if opcao == "3":
        ListarGrupo()
    if opcao == "4":
        BuscaID()
    if opcao == "5":
        Palpites()
    if opcao == "6":
        PalpitesPendentes()
    if opcao == "7":
        GabaritoOficial()
    if opcao == "8":
        ResultadosPendentes()
    if opcao == "9":
        MenuPrincipal()

def MenuPrincipal():
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
            GerarPrimeiraFase(CarregarSelecoes('Archives/selecoes.tx'))
            input('Selecoes carregadas, Primeira Fase gerada. Pressione enter para continuar \n')
        except:
            input('Erro ao Carregar as selecoes e gerar Fase, Pressione enter para continuar')
    if opcao == "2":
       CadastrarApostador()
    if opcao == "3":
        RegistrarPalpites()
    if opcao == "4":
        CompletarPalpites()
    if opcao == "5":
        GerarFase()
    if opcao == "6":
        CadastrarGabarito()
    if opcao == "7":
        ConsultarPontuacao()
    if opcao == "8":
        ResultadoFinal()
    if opcao == "9":
        ConsultarDados()
        return None
    if opcao == "10": 
        return None
    MenuPrincipal()
    

MenuPrincipal()