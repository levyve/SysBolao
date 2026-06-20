def Consulta(dados_copa):
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
    
    opcao = int(input("\nDigite a opção desejada: "))
    if opcao == "1":
        ListarCalendario
    if opcao == "2":
        ListarFase
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