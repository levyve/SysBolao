import string #pra função de pegar os ascii
import json

def Criar_Arquivo_Padrao(jogos: list):
    """Cria um arquivo JSON contendo todos os 72 jogos para 1º fase, servindo como "estrutua base".
    
    :param jogos: uma lista contendo todos os jogos, sem qualquer palpite.
    :type jogos: list
    """

    with open('Archives/json/estrutura_jogos.json', 'w', encoding='utf-8') as arq:
        json.dump(jogos, arq, indent=4, ensure_ascii=False)

def Gerar_Primeira_Fase(grupos: dict) -> list:
    """Gera os todos os jogos da primeira fase

    :param grupos: lista contendo os grupos com todas as seleções participantes;
    :type grupos: list
    """
    
    jogos = []
    id = 0
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

    Criar_Arquivo_Padrao(jogos)

def Carregar_Selecoes(nomearquivo: str) -> dict:
    """Carrega as seleções que iram participar e as separa em seus respectivos grupos.

    :param nomearquivo: nome do arquivo .txt que contem as 48 seleções.
    :type nomearquivo: string
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
    
    Gerar_Primeira_Fase(grupos)

def Encontrar_Jogo(jogos: list, id: str):
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
def Exibir_Jogo(jogo: dict):
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
