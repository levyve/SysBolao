import json

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


def Carregar_Gabarito():
    with open('Archives/json/gabarito.json', 'r', encoding='utf-8') as arq:
        jogos_gabarito = json.load(arq)

    return jogos_gabarito
