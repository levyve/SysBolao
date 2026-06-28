import json
import random

def Criar_Arquivo_Apostador(apostador: str):
    """Cria um arquivo de palpites de um apostador.
    
    :param apostador: nome do apostador
    :type apostador: str
    """


    with open('Archives/json/estrutura_jogos.json', 'r', encoding='utf-8') as arq:
        jogos = json.load(arq)

    with open(f'Archives/json/palpites_{apostador}.json', 'w', encoding='utf-8') as arq:
        json.dump(jogos, arq, indent=4, ensure_ascii=False)


def Atualizar_Arquivo_Palpites(jogos: list, apostador: str):
    """Atualiza um arquivo de palpites de um apostador.

    :param jogos: lista contendo todos os jogos, com ou sem palpites, do apostdor.
    :type jogos: list

    :param apostador: nome do apostador
    :type apostador: str
    """

    with open(f'Archives/json/palpites_{apostador}.json', 'w', encoding='utf-8') as arq:
            json.dump(jogos, arq, indent=4, ensure_ascii=False)


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

    Atualizar_Arquivo_Palpites(jogos, apostador)


def Validar_Jogador(nome: str):
    """Valida se um apostador já foi cadastrado
    
    :param nome: nome do apostador.
    :type nome: str

    :return: True se já estiver cadastrado, ou False caso não esteja.
    :rtype: bool
    """
    
    with open('Archives/txt/apostadores.txt', 'r', encoding='utf-8') as arq:
        if nome.lower() in [linha.strip().lower() for linha in arq]:
            return True
        
        else:
            return False


def Cadastrar_Apostador(nome: str):
    """Cadastra um novo apostador

    :param nome: nome do apostador que será cadastrado
    :type nome: str
    """
    with open('Archives/txt/apostadores.txt', 'a+', encoding='utf-8') as arq: ## a+ é leitura e escrita sem apagar, nao substitui o texto, adiciona
        if(Validar_Jogador(nome)):
            print("Erro: Apostador já cadastrado!")
            return None
        
        arq.write('\n'+nome )

    Criar_Arquivo_Apostador(nome)


def Carregar_Palpites(apostador: str) -> list:
    """Carrega os palpites do arquivo de um apostador.

    :param apostador: nome do apostador.
    :type apostador: str

    :return: uma lista de todos os jogos, com ou sem palpites, do arquivo.
    :rtype: list
    """    

    with open(f'Archives/json/palpites_{apostador}.json', 'r', encoding='utf-8') as arq:
        jogos = json.load(arq)
    return jogos


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
