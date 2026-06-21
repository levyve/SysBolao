import json

def AtualizarArquivoPalpites(jogos: list, apostador: str):
    """Atualiza/Cria um arquivo de palpites pera um apostador

    :param jogos: uma lista de jogos contendo cada partida.
    :type jogos: list

    :param apostador: nome do apostador
    :type apostador: str
    """

    with open(f'Archives/palpites_{apostador}.json', 'w', encoding='utf-8') as arq:
        json.dump(jogos, arq, indent=4, ensure_ascii=False)


def AtualizarPalpites(apostador: str, jogos: list, id: str, gols1: str, gols2: str):
    """Atualiza o palpite de um dados apostador em um jogo específico.

    :param apostador: nome do apostador.
    :type apostador: str
    
    :param jogos: lista contendo todos os jogos, com ou sem palpites, do apostdor.
    :type jogos: list
    
    :param id: ID do jogo que o apostador deseja alterar.
    :type id: str
    
    :param gols1: número de gols da primeira seleção.
    :type gols1: str
    
    :param gols2: número de gols da segunda seleção.
    :type gols2: str
    """
    
    for jogo in jogos:
        if(jogo['id'] == int(id)):
            partida = {
            "id": int(id),
            "fase": 1,
            "grupo": jogo['grupo'],
            "selecao1": jogo['selecao1'],
            "selecao2": jogo['selecao2'],
            "gols1":int(gols1),
            "gols2": int(gols2),
            }

            jogos.insert(jogos.index(jogo), partida)
            jogos.pop(jogos.index(jogo))
    
    AtualizarArquivoPalpites(jogos, apostador)


def ValidarJogador(nome: str):
    """Valida se um apostador já foi cadastrado
    
    :param nome: nome do apostador.
    :type nome: str

    :return: True se já estiver cadastrado, ou False caso não esteja.
    :rtype: bool
    """
    
    with open('Archives/apostadores.txt', 'r', encoding='utf-8') as arq:
        if nome.lower() in [linha.strip().lower() for linha in arq]:
            return True
        
        else:
            return False

def CadastrarApostador(jogos: list):
    """Cadastra um novo apostador

    :param nomearquivo: nome do arquivo que conterá os apostadores
    :type nomearquivo: str

    :param jogos: uma lista de jogos contendo cada partida.
    :type jogos: list
    """

    nome = input("Insira o nome do novo apostador: ")
    with open('Archives/apostadores.txt', 'a+', encoding='utf-8') as arq: ## a+ é leitura e escrita sem apagar, nao substitui o texto, adiciona
        if(ValidarJogador(nome)):
            print("Erro: Apostador já cadastrado!")
            return None
        
        arq.write('\n'+nome )

    AtualizarArquivoPalpites(jogos, nome)


def CarregarPalpites(nome_arquivo: str) -> list:
    """Carrega os palpites do arquivo de um apostador.

    :param nome_arquivo: nome do arquivo do apostador.
    :type nome_arquivo: str

    :return: uma lista de todos os jogos, com ou sem palpites, do arquivo.
    :rtype: list
    """    

    with open(nome_arquivo, 'r', encoding='utf-8') as arq:
        jogos = json.load(arq)
    return jogos


def ExibirJogo(jogo: dict):
    """Exibe um jogo específico em um formato padrão.

    :param jogo: um dicionário que representa um jogo específico a ser exibido.
    :type jogo: dict
    """

    fases = {
        1: "Primeira Fase",
        2: "Segunda Fase",
        3: "Oitavas de Final",
        4: "Quartas de Final",
        5: "Semifinal",
        6: "Final"}
    
    print(f"""
    ID: {jogo['id']}
    Fase: {fases[jogo['fase']]}
    Grupo: {jogo['grupo']}
    Partida: {jogo['selecao1']} x {jogo['selecao2']}""")


def EncontrarJogo(jogos: list, id: str):
    """Encontra um jogo específico pelo seu ID em uma lista de jogos.
    
    :param jogos: uma lista contendo todos os jogos, com ou sem palpites.
    :type: list

    :param id: o ID do jogo que se deseja encontrar.
    :type id: str

    :return jogo: um dicionário que representa o jogo referente ao ID informado.
    :rtype jogo: dict

    :return None: retorna None caso o jogo com o ID informado não exista. 
    :rtype None: None
    """
    
    for jogo in jogos:
        if (jogo['id'] == int(id)):
            return jogo
        
    print("ERRO! O ID informado não existe!")
    return None


def Exibir_Tutorial_B(apostador: str):
     """Exibe um tutorial sobre como fazer o cadastro ou alteração de palpite(s) em Lote.

     :param apostador: nome do apostador que deseja alterar ou cadastrar palpite(s)
     :type apostador: str
     """
     print(f"""
        ===========================================
            COMO USAR O CADASTRO EM LOTE
        ===========================================

        Com essa opção, você pode editar seus palpites diretamente no SEU arquivo de dados, 
        sem precisar preenchê-los um a um pela interface do programa.

        O sistema, automaticamente, já parou a execução. 
        Isso evita conflitos de acesso ao arquivo e garante que suas alterações não sejam perdidas ou corrompidas.
        Quando terminar, inicie o programa novamente.

        -------------------------------------PASSO A PASSO-------------------------------------

        ----> Passo 1: Localize o arquivo JSON
        + Encontre o seu arquivo JSON, ele estará na pasta "Archives" com o nome "palpites_{apostador}.json". 
        + Este é arquivo que contém os dados de todos os jogos, com ou sem seus palpites. 
        + DECORE, ou ANOTE O CAMINHO, pois você precisará devolver o arquivo alterado EXATAMENTE nesse mesmo lugar depois de editá-lo.

        ----> Passo 2: Abra o arquivo em um editor de texto
        + Use um editor de texto simples (como Bloco de Notas, Notepad++, VS Code, etc.) para abrir o arquivo e altera o arquivo. 
        + EVITE usar editores que possam alterar a formatação do JSON (como o Word).
        """)
     
     print("""
        ----> Passo 3: Edite os resultados dos jogos
        + A estrutura de cada partida/jogo será como a seguinte:
            {
                "id": 37, ----> ID do jogo
                "fase": 1, ----> Fase
                "grupo": "G", ----> Grupo
                "selecao1": "Brasil", ----> Primeira Seleção
                "selecao2": "Uruguai", ----> Segunda Seleção
                "gols1": -1, ----> Gols da primeira seleção - Este é o campo que você deve modificar
                "gols2": -1 ----> Gols da segunda seleção - Este é o campo que você deve modificar
            }

        + Insira ou modifique diretamente no arquivo seus palpites sobre os jogos. 
        + Essa inserção deve ser feita nos locais ao lado dos "gols1" e "gols2" (onde está -1).
        + Números negativos serão considerados com palpites pendentes.
        + Respeite a estrutura original do JSON 
        (NÃO ALETERE nomes de campos, vírgulas ou chaves, apenas os valores dos palpites em "gols1" e "gols2").
            
        --> Verifique se os resultados foram colocados corretamente antes de finalizar.

        ----------------------------------------------------------------------------------------------------------
        ATENÇÃO: qualquer erro de formatação (vírgula faltando, chave não fechada, etc.) 
        pode impedir que o arquivo seja lido corretamente quando o programa for reaberto, resultando em falha.
        ----------------------------------------------------------------------------------------------------------
        """)

     print(f"""
        ----> Passo 5: Salve o arquivo
        + Salve as alterações no MESMO LOCAL e com o MESMO NOME (palpites_{apostador}.json) 
        em que o arquivo estava originalmente (na pasta "Archives").

        ----> Passo 6: Inicie o programa novamente
        + Inicie o programa novamente. 
        + Se tudo tiver sido feito da forma correta, 
        ele identificará automaticamente o arquivo modificado e carregará os palpites atualizados.
        """) 
     
     print("^ LEIA O TUTORIAL ACIMA PARA SABER COMO FAZER UM CADASTRO EM LOTE ^\n")

def SubMenuInterativo(apostador: str):
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
        
        
        jogos = CarregarPalpites(nome_arquivo=f'Archives/palpites_{apostador}.json')
        if (int(opcao) == 1):

            print("""
            =========================================
                     LISTA DE TODOS OS JOGOS      
            =========================================
            """)

            for jogo in jogos:
                ExibirJogo(jogo)

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
                    ExibirJogo(jogo)

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
            
            jogo = EncontrarJogo(jogos, id_partida)
            if (jogo == None):
                continue
            
            print("""
    Jogo encontrado:""")

            ExibirJogo(jogo)

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

            AtualizarPalpites(apostador, jogos, id_partida, novo_gols1, novo_gols2)

            print("\nPalpite cadastrado com sucesso!")
            print(f"\n{jogo['selecao1']} {novo_gols1} x {novo_gols2} {jogo['selecao2']}")

        elif (int(opcao) == 4):
            break


def CadastrarPalpites(modo: str):
    """Verifica qual modo de cadastro de palpites o apostador escolheu.
    
    :param modo: modo de cadastro de palpites escolhido pelo apostador: 'a' --> cadastro interativo; 'b' --> cadastro em lote.
    :type modo: str

    :return False: retorna False se ocorreu algum erro durante o cadastro de palpites.
    :rtype: bool

    :return None: retorna None para informar ao sistema para parar sua execução.
    :rtype None:
    """
    
    if (modo.lower() != 'a' and modo.lower() != 'b'):
        print("ERRO: jogador não selecionou uma opção válida!")
        return False
    

    apostador = input("Nome do apostador: ")
    if (modo.lower() == 'a'):

        if(ValidarJogador(apostador)):
            SubMenuInterativo(apostador)
            
        else:
            print("Erro! Apostador não cadastrado no sistema.")
            return False
    else:
       Exibir_Tutorial_B(apostador)
       return None
    
CadastrarPalpites('b')