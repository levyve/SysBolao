import json
import string

def Criar_Arquivo_Padrao(jogos: list):
    """Cria um arquivo JSON contendo todos os 72 jogos para 1º fase, servindo como "estrutua base".
    
    :param jogos: uma lista contendo todos os jogos, sem qualquer palpite.
    :type jogos: list
    """

    with open('dados/base/estrutura_jogos.json', 'w', encoding='utf-8') as arq:
        json.dump(jogos, arq, indent=4, ensure_ascii=False)


def Carregar_Selecoes() -> dict:
    """Carrega as seleções que iram participar e as separa em seus respectivos grupos.
    """

    grupos = {}
    
    with open('dados/base/selecoes.txt', 'r', encoding='utf-8') as arq:
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
