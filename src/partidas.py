import string #pra função de pegar os ascii
import json

def CarregarSelecoes(nomearquivo: str) -> dict:
    """Carrega as seleções que iram participar e as separa em seus respectivos grupos.

    :param nomearquivo: nome do arquivo .txt que contem as 48 seleções.
    :type nomearquivo: string

    :return: um dicionário contendo os grupos e a seleções de cada grupo.
    :rtype: dict
    """

    grupos = {}
    
    with open(nomearquivo, 'r', encoding='utf-8') as arq:
        selecoes = [linha.strip() for linha in arq] ##lê e separa, é um laço FOR normal
    
    # ve se tem 48 linha
    if len(selecoes) != 48:
        print("Número de linhas é diferente de 48, carregamento cancelado")
        return None
        
    #linha vazias
    if "" in selecoes:
        print("Linha vazia, carregamento cancelado")
        return None

    #se tem repetição
    if len(selecoes) != len(set(selecoes)): ##o set transforma em conjunto, entao se algo tiver repetido, ele vira 1 coisa só e o len ve se ainda sao 4 itens.
        print("Existem seleções repetidas, carregamento cancelado")
        return None

   
    letras = list(string.ascii_uppercase)[:12]  # Pega as letras de A-L
    for i in range(12):
        letra = letras[i]
        # pra fatiar
        inicio = i * 4
        fim = inicio + 4
        #formato {'A': [time',time2 ...], 'B': ...} fatia de 4 em 4
        grupos[letra] = selecoes[inicio:fim] 
        
    return grupos


def GerarPrimeiraFase(grupos: list) -> list:
    """Gera os todos os jogos da primeira fase

    :param grupos: lista contendo os grupos com todas as seleções participantes;
    :type grupos: list

    :return: uma lista de dicionários de cada partida da fase
    :rtype: lsit
    """
    
    jogos = []
    id = 0;
    for grupo in grupos:
        for i in range(len(grupos[grupo]) - 1):
            for j in range((i + 1), len(grupos[grupo])):
                id += 1
                partida = {
                    "id": id,
                    "fase": 1,
                    "grupo": grupo,
                    "selecao1": grupos[grupo][i],
                    "selecao2": grupos[grupo][j],
                    "gols1": -1,
                    "gols2": -1,
                }

                jogos.append(partida)
 
    return jogos