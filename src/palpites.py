from armazenamento.manipulacao_arquivos_apostador import Atualizar_Arquivo_Palpites
from utilitários import (
    Validar_Apostador,
    Exibir_Jogo,
    Encontrar_Jogo
    ) 
from interface.menu_cadastro_palpites import SubMenu_Interativo
import random


def Atualizar_Palpites(apostador: str, jogos: list, jogo: dict, id: str, gols1: str, gols2: str):
    """Atualiza o palpite de um dados apostador em um jogo específico.

    :param apostador: nome do apostador.
    :type apostador: str
    
    :param jogos: lista contendo todos os jogos, com ou sem palpites, do apostdor.
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

    partida = {}
    if (jogo["fase"] == 1):
        
        partida = {
        "id": int(id),
        "fase": jogo['fase'],
        "grupo": jogo['grupo'],
        "selecao1": jogo['selecao1'],
        "selecao2": jogo['selecao2'],
        "gols1":int(gols1),
        "gols2": int(gols2),
        }

    else:
        
        partida = {
        "id": int(id),
        "fase": jogo['fase'],
        "grupo": jogo['grupo'],
        "selecao1": jogo['selecao1'],
        "selecao2": jogo['selecao2'],
        "gols1":int(gols1),
        "gols2": int(gols2),
        "vencedor_penaltis": None
        }

    jogos.insert(jogos.index(jogo), partida)
    jogos.pop(jogos.index(jogo))

    Atualizar_Arquivo_Palpites(jogos, apostador)


def Completar_Palpites_Aleatoriamente(apostador: str, jogos: list):
    
    qtd_preenchidos = 0
    qtd_gols = [0, 1, 2, 3, 4, 5, 6, 7]
    pesos = [60, 50, 40, 30, 25, 20, 15, 10]

    for jogo in jogos:
        if (jogo['gols1'] == -1 or jogo['gols2'] == -1):
            gols1 = random.choices(qtd_gols, weights=pesos, k=1)[0]
            gols2 = random.choices(qtd_gols, weights=pesos, k=1)[0]


            if (jogo['fase'] != 1):  # fases eliminatórias não permitem empate
                while (gols1 == gols2):
                    gols1 = random.choices(qtd_gols, weights=pesos, k=1)[0]
                    gols2 = random.choices(qtd_gols, weights=pesos, k=1)[0]


            Atualizar_Palpites(apostador, jogos, jogo, str(jogo['id']), gols1, gols2)
            qtd_preenchidos += 1

    print(f"\n{qtd_preenchidos} palpite(s) pendente(s) preenchido(s) aleatoriamente para {apostador}!")


def Exibir_Tutorial_Cadastro_Lote(apostador: str):
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


def Listar_Bolao_Completo_Apostador(jogos: list):
    
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


def Listar_Jogos_Pendentes_Apostador(jogos: list):

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


def Cadastrar_Placar(jogos: list, apostador: str):
        
    id_partida = input("Digite o ID do jogo: ")
    while (not id_partida.isdigit()):
        print("ERRO! O ID informado não é um ID válido.")
        id_partida = input("Por favor, digite um ID válido (Número): ")
    
    jogo = Encontrar_Jogo(jogos, id_partida)
    if (jogo == None):
        print("ERRO: Não há um jogo com o ID informado.")
        return False
    
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