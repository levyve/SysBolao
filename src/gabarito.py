import json
from partidas import Encontrar_Jogo, Exibir_Jogo

def Criar_Arquivo_Gabarito():
    """Cria um arquivo que conterá o gabarito oficial dos jogos.
    """
    
    with open('Archives/json/estrutura_jogos.json', 'r', encoding='utf-8') as arq:
        jogos = json.load(arq)

    with open('Archives/json/gabarito.json', 'w', encoding='utf-8') as arq:
        json.dump(jogos, arq, indent=4, ensure_ascii=False)


def Atualizar_Arquivo_Gabarito(jogos: list):
    """Atualiza um arquivo do gabarito oficial.

    :param jogos: lista contendo todos os jogos do gabarito oficial.
    :type jogos: list
    """

    with open(f'Archives/json/gabarito.json', 'w', encoding='utf-8') as arq:
            json.dump(jogos, arq, indent=4, ensure_ascii=False)


def Atualizar_Partida_Gabarito(jogos: list, id: str, jogo: dict, gols1: str, gols2: str):
    """Atualiza o resultado de um jogo específico no gabarito oficial.
    
    :param jogos: lista contendo todos os jogos do gabarito oficial.
    :type jogos: list
    
    :param jogo: dicionário que representa o jogo.
    :type jogo: dict
    
    :param id: ID do jogo que o apostador deseja alterar.
    :type id: str
    
    :param gols1: número de gols da primeira seleção.
    :type gols1: str
    
    :param gols2: número de gols da segunda seleção.
    :type gols2: str
    """

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

    Atualizar_Arquivo_Gabarito(jogos)


def Carregar_Gabarito():
    with open('Archives/json/gabarito.json', 'r', encoding='utf-8') as arq:
        jogos_gabarito = json.load(arq)

    return jogos_gabarito


def Exibir_Tutorial_Cadastro_Lote():
    """Exibe um tutorial sobre como fazer o cadastro ou alteração de palpite(s) em Lote.
    """
     
    print(f"""
        ===========================================
               COMO USAR O CADASTRO EM LOTE
        ===========================================

        Com essa opção, você pode editar o gabarito oficial que contém os dados de cada partida, 
        sem precisar preenchê-los um a um pela interface do programa.

        O sistema, automaticamente, já parou a execução. 
        Isso evita conflitos de acesso ao arquivo e garante que suas alterações não sejam perdidas ou corrompidas.
        Quando terminar, inicie o programa novamente.

        -------------------------------------PASSO A PASSO-------------------------------------

        ----> Passo 1: Localize o arquivo JSON
        + Encontre o arquivo JSON do gabarito, ele estará no caminho "Archives/json/" com o nome "gabarito.json". 
        + Este é arquivo que contém os dados oficiais de todos os jogos. 
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
                "vencedor_penaltis": None (Este campo só aparece na fases 2 em diante)
            }

        + Insira ou modifique diretamente no arquivo seus palpites sobre os jogos. 
        + Essa inserção deve ser feita nos locais ao lado dos "gols1" e "gols2" (onde está -1).
           * Caso haja empate nessa partida E esteja inserindo o resultado de uma partida da 2º Fase (16-avos de Final) ou em diante, você deve inserir no campo "vencedor_penaltis" o NOME DA SELEÇÃO VENCEDORA dentre a "selecao1" e "selecao2" da mesma forma como está escrita.
           * Caso não escreva o nome corretamente, ou deixe o campo em nenhum valor (None), o sistema não irá gerar a próxima fase, ou mesmo não será capaz de calcular a pontuações dos jogadores corretamente.
        + Números negativos serão considerados como resultados pendentes.
        + Respeite a estrutura original do JSON 
        (NÃO ALETERE nomes de campos, vírgulas ou chaves).
            
        --> Verifique se os resultados foram colocados CORRETAMENTE antes de finalizar.

        ----------------------------------------------------------------------------------------------------------
        ATENÇÃO: qualquer erro de formatação (vírgula faltando, chave não fechada, etc.) 
        pode impedir que o arquivo seja lido corretamente quando o programa for reaberto, resultando em falha.
        ----------------------------------------------------------------------------------------------------------
        """)

    print(f"""
        ----> Passo 5: Salve o arquivo
        + Salve as alterações no MESMO LOCAL e com o MESMO NOME (gabarito.json) 
        em que o arquivo estava originalmente (no caminho "Archives/json/").

        ----> Passo 6: Inicie o programa novamente
        + Inicie o programa novamente. 
        + Se tudo tiver sido feito da forma correta, 
        ele identificará automaticamente o arquivo modificado e carregará os palpites atualizados.
        """) 
     
    print("^ LEIA O TUTORIAL ACIMA PARA SABER COMO FAZER UM CADASTRO EM LOTE ^\n")
    

def Cadastrar_Gabarito():
    try:
        open('Archives/json/gabarito.json', 'r', encoding='utf-8')
        
    except FileNotFoundError:
        Criar_Arquivo_Gabarito()

    while (True):
        print(f"""
        ******** Cadastrar Gabarito ********
        1. Cadastro Interativo
        2. Cadastro em Lote
        3. Voltar ao menu principal
        """)

        opcao =  input("Digite a opção desejada: ")

        if opcao not in ["1", "2", "3"]:
            print("ERRO: a opção selecionada não existe.")
            continue


        jogos_gabarito = Carregar_Gabarito()
        if (opcao == "1"):
            id_partida = input("Digite o ID do jogo: ")

            while (not id_partida.isdigit()):
                print("ERRO: O ID informado não é um ID válido.")
                id_partida = input("Por favor, digite um ID válido (Número): ")

            jogo = Encontrar_Jogo(jogos_gabarito, id_partida)
            if (jogo == None):
                print("ERRO: Não há um jogo com o ID informado.")
                continue
                
            print("Jogo encontrado:")
            Exibir_Jogo(jogo)
            print(f"""
    Resultado:
    {jogo['selecao1']} {jogo['gols1']} x {jogo['gols2']} {jogo['selecao2']}""")     
            print("""
    -----------------------------------------""")
            
            novo_gols1 = input(f"Digite o número de gols de {jogo['selecao1']}: ")
            while (not novo_gols1.isdigit()):
                print("\nERRO! O número de gols informado não é um número.")
                id_partida = input(f"Por favor, digite uma quantidade de gols válida para {jogo['selecao1']}: ")
            
            novo_gols2 = input(f"Digite o número de gols de {jogo['selecao2']}: ")
            while (not novo_gols2.isdigit()):
                print("\nERRO! O número de gols informado não é um número.")
                id_partida = input(f"Por favor, digite uma quantidade de gols válida para {jogo['selecao2']}: ")


            Atualizar_Partida_Gabarito(jogos_gabarito, id_partida, jogo, novo_gols1, novo_gols2)

            print("\nResultado cadastrado com sucesso!")
            print(f"\n{jogo['selecao1']} {novo_gols1} x {novo_gols2} {jogo['selecao2']}")


        elif (opcao == "2"):
            Exibir_Tutorial_Cadastro_Lote()
            break

        else:
            break


def Visualizar_Gabarito_Oficial():
    existe_gabarito = True
    try:
        open('Archives/json/gabarito.json', 'r', encoding='utf-8')
    except FileNotFoundError:
        print("ERRO: o arquivo JSON do gabarito oficial ainda não foi criado!\nPara criar o arquivo do gabarito oficial, vá em 'Cadastrar Gabarito Ofical', no meu principal.")
        
        existe_gabarito = False

    if (existe_gabarito):

        jogos_gabarito = Carregar_Gabarito()

        print("""
        =======================================
               GABARITO OFICIAL COMPLETO      
        =======================================
        """)

        for jogo in jogos_gabarito:
            Exibir_Jogo(jogo)
            print(f"""
    Resultado:
    {jogo['selecao1']} {jogo['gols1']} x {jogo['gols2']} {jogo['selecao2']}""")     
            print("""
    -----------------------------------------""")
            

def Visualizar_Resultados_Pendentes():

    existe_gabarito = True
    try:
        open('Archives/json/gabarito.json', 'r', encoding='utf-8')
    except FileNotFoundError:
        print("ERRO: o arquivo JSON do gabarito oficial ainda não foi criado!\nPara criar o arquivo do gabarito oficial, vá em 'Cadastrar Gabarito Ofical', no meu principal.")
        
        existe_gabarito = False

    if (existe_gabarito):
        
        jogos_gabarito = Carregar_Gabarito()

        print("""
        ============================================
          RESULTADOS PENDENTES NO GABARITO OFICIAL       
        ============================================
        """)

        for jogo in jogos_gabarito:
            if (jogo["gols1"] <= -1 or jogo["gols2"] <= -1):
                Exibir_Jogo(jogo)
                print(f"""
    Resultado (Pendente):
    {jogo['selecao1']} {jogo['gols1']} x {jogo['gols2']} {jogo['selecao2']}""")     
                print("""
    -----------------------------------------""")
            
