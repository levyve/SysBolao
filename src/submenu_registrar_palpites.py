from src.apostador import (
    Carregar_Palpites, 
    Atualizar_Palpites, 
    Validar_Jogador
    )
from src.partidas import ( 
    Encontrar_Jogo,
    Exibir_Jogo
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

            print("""
            =========================================
                     LISTA DE TODOS OS JOGOS      
            =========================================
            """)

            for jogo in jogos:
                Exibir_Jogo(jogo)

                print(f"""
    Seu palpite:
    {jogo['selecao1']} {jogo['gols1']} x {jogo['gols2']} {jogo['selecao2']}""")
                print("""
    -----------------------------------------""")

        elif (int(opcao) == 2):
            
            print("""
            ========================================
                       JOGOS SEM PALPITES      
            ========================================
            """)
            
            for jogo in jogos:
                if (jogo['gols1'] <= -1 or jogo['gols2'] <= -1):
                    Exibir_Jogo(jogo)

                    print(f"""
    Palpite:
    {jogo['selecao1']} {jogo['gols1']} x {jogo['gols2']} {jogo['selecao2']}""")  
                    print("""
    -----------------------------------------""")

        elif (int(opcao) == 3):
            
            id_partida = input("Digite o ID do jogo: ")
            while (not id_partida.isdigit()):
                print("ERRO! O ID informado não é um ID válido.")
                id_partida = input("Por favor, digite um ID válido (Número): ")
            
            jogo = Encontrar_Jogo(jogos, id_partida)
            if (jogo == None):
                print("ERRO: Não há um jogo com o ID informado.")
                continue
            
            print("Jogo encontrado:")

            Exibir_Jogo(jogo)

            print(f"""
    Palpite atual:
    {jogo['selecao1']} {jogo['gols1']} x {jogo['gols2']} {jogo['selecao2']}
            """)
            
            novo_gols1 = input(f"Digite o número de gols de {jogo['selecao1']}: ")
            while (not novo_gols1.isdigit()):
                print("\nERRO! O número de gols informado não é um número.")
                id_partida = input(f"Por favor, digite uma quantidade de gols válida para {jogo['selecao1']}: ")
            
            novo_gols2 = input(f"Digite o número de gols de {jogo['selecao2']}: ")
            while (not novo_gols2.isdigit()):
                print("\nERRO! O número de gols informado não é um número.")
                id_partida = input(f"Por favor, digite uma quantidade de gols válida para {jogo['selecao2']}: ")

            Atualizar_Palpites(apostador, jogos, id_partida, novo_gols1, novo_gols2)

            print("\nPalpite cadastrado com sucesso!")
            print(f"\n{jogo['selecao1']} {novo_gols1} x {novo_gols2} {jogo['selecao2']}")

        elif (int(opcao) == 4):
            break


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
        + Encontre o seu arquivo JSON, ele estará no caminho "Archives/json/" com o nome "palpites_{apostador}.json". 
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
                "gols2": -1, ----> Gols da segunda seleção - Este é o campo que você deve modificar
                "vencedor_penaltis": None (Este campo só aparece na fases 2 em diante)
            }

        + Insira ou modifique diretamente no arquivo seus palpites sobre os jogos. 
        + Essa inserção deve ser feita nos locais ao lado dos "gols1" e "gols2" (onde está -1).
           * Caso haja EMPATE nessa partida E esteja inserindo o resultado de uma partida da 2º Fase (16-avos de Final) ou em diante, você deve inserir no campo "vencedor_penaltis" o NOME DA SELEÇÃO VENCEDORA dentre a "selecao1" e "selecao2" da mesma forma como está escrita.
           * Caso não escreva o nome corretamente, ou deixe o campo em nenhum valor (None), o sistema não irá gerar a próxima fase, ou mesmo não será capaz de calcular a pontuações dos jogadores corretamente.
        + Números negativos serão considerados como palpites pendentes.
        + Respeite a estrutura original do JSON 
        (NÃO ALETERE nomes de campos, vírgulas ou chaves).
            
        --> Verifique se os resultados foram colocados corretamente antes de finalizar.

        ----------------------------------------------------------------------------------------------------------
        ATENÇÃO: qualquer erro de formatação (vírgula faltando, chave não fechada, etc.) 
        pode impedir que o arquivo seja lido corretamente quando o programa for reaberto, resultando em falha.
        ----------------------------------------------------------------------------------------------------------
        """)

     print(f"""
        ----> Passo 5: Salve o arquivo
        + Salve as alterações no MESMO LOCAL e com o MESMO NOME (palpites_{apostador}.json) 
        em que o arquivo estava originalmente (no caminho "Archives/json/").

        ----> Passo 6: Inicie o programa novamente
        + Inicie o programa novamente. 
        + Se tudo tiver sido feito da forma correta, 
        ele identificará automaticamente o arquivo modificado e carregará os palpites atualizados.
        """) 
     
     print("^ LEIA O TUTORIAL ACIMA PARA SABER COMO FAZER UM CADASTRO EM LOTE ^\n")


def Cadastrar_Palpites(modo: str):
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

        if(Validar_Jogador(apostador)):
            SubMenu_Interativo(apostador)
            
        else:
            print("Erro! Apostador não cadastrado no sistema.")
            return False
    else:
       Exibir_Tutorial_B(apostador)
       return None