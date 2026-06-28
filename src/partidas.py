import random
import string #pra função de pegar os ascii
import json
import functools

def Criar_Arquivo_Padrao(jogos: list):
    """Cria um arquivo JSON contendo todos os 72 jogos para 1º fase, servindo como "estrutua base".
    
    :param jogos: uma lista contendo todos os jogos, sem qualquer palpite.
    :type jogos: list
    """

    with open('Archives/json/estrutura_jogos.json', 'w', encoding='utf-8') as arq:
        json.dump(jogos, arq, indent=4, ensure_ascii=False)




def Encontrar_Jogo(jogos: list, id: str) -> dict:
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


def Calcular_Pontuacoes_Grupo(jogos: list, grupo: str) -> dict:
    """Calcula os pontos, saldos, gols marcados e sofridos de cada seleção de um grupo.
    
    :param jogos: uma lista contendo todos os jogos, com todos os resultados
    :type jogos: list

    :param grupo: grupo (A, B, C, D...) cujas seleções terão seus pontos calculados
    :type grupo: str
    
    :return: um dicionário contendo as "pontuações" de cada seleção no formato 
        { "Brasil": {"pontos": 6, "gols_marcados": 4, "gols_sofridos": 1, "saldo": 3}, ... }
    
    :rtype: dict
    """

    jogos_grupo = [jogo for jogo in jogos if jogo["grupo"] == grupo and jogo["fase"] == 1]

    pontuacoes = {}
    for jogo in jogos_grupo:
        # Adiciona uma seleção no dicionário de pontuações com seus valores zerados
        for selecao in [jogo["selecao1"], jogo["selecao2"]]:
            if selecao not in pontuacoes:
                pontuacoes[selecao] = {"pontos": 0, "gols_marcados": 0, "gols_sofridos": 0, "saldo": 0}

        selecao1, selecao2 = jogo["selecao1"], jogo["selecao2"]
        gols1, gols2 = jogo["gols1"], jogo["gols2"]

        # Acumula gols
        pontuacoes[selecao1]["gols_marcados"] += gols1
        pontuacoes[selecao1]["gols_sofridos"] += gols2
        pontuacoes[selecao2]["gols_marcados"] += gols2
        pontuacoes[selecao2]["gols_sofridos"] += gols1

        # Distribui pontos
        if gols1 > gols2:
            pontuacoes[selecao1]["pontos"] += 3
        elif gols2 > gols1:
            pontuacoes[selecao2]["pontos"] += 3
        else:
            pontuacoes[selecao1]["pontos"] += 1
            pontuacoes[selecao2]["pontos"] += 1

    # Calcula saldo
    for selecao in pontuacoes:
        pontuacoes[selecao]["saldo"] = pontuacoes[selecao]["gols_marcados"] - pontuacoes[selecao]["gols_sofridos"]

    return pontuacoes


def Realizar_Confronto_Direto(selecao1: str, selecao2: str, jogos: list) -> int:
    """Busca o jogo da primeira fase entre duas seleções e analisa o confronto entre elas.
    :param selecao1: nome de uma seleção "x"
    :type selecao1: str
    
    :param selecao2: nome de uma seleçaõ "y"
    :type selecao2: str
    
    :param jogos: uma lista contendo todos os jogos
    :type jogos: list
    
    :return: 1 se a selecao1 venceu, -1 se selecao2 venceu, e 0 se empataram.
    :rtype: int
    """

    for jogo in jogos:
        if jogo["fase"] == 1 and {jogo["selecao1"], jogo["selecao2"]} == {selecao1, selecao2}:
        
            if jogo["gols1"] > jogo["gols2"]: 
                return 1
                
            elif jogo["gols2"] > jogo["gols1"]:
                return -1 
            
            else:
                return 0


def _Comparador_Criterios(selecao1: str, selecao2: str, pontuacoes: dict, jogos_grupo: None | list = None) -> int:
    """Realiza a comparação entre duas seleções pelos seguintes critérios:
    1. Pontos;
    2. Saldo de gols (Número de gols marcados - número de gols sofridos);
    3. Gols marcados;
    4. Confronto direto (se as seleções são de um mesmo grupo);
    5. Sorteio (Caso haja empate em todos os critérios anteriores);
       
    :param selecao1: nome de uma seleçaõ "x"
    :type selecao1: str

    :param selecao2: nome de uma seleçaõ "y"
    :type selecao2: str
    
    :param pontuacoes: um dicionário contendo as pontuações de cada seleção
    :type pontuacoes: dict
    
    :param jogos_grupo: parâmetro que indica se os jogos das seleções que estão sendo comparadas são em um mesmo grupo
    :type jogos_grupo: None (não são em um mesmo grupo) | list (são em um mesmo grupo)

    :return: um número inteiro (positivo ou negativo) diferente de zero.
    :rtype: int
    """

    # 1. Pontos
    if pontuacoes[selecao1]["pontos"] != pontuacoes[selecao2]["pontos"]:
        return pontuacoes[selecao1]["pontos"] - pontuacoes[selecao2]["pontos"]
    
    # 2. Saldo de Gols
    elif pontuacoes[selecao1]["saldo"] != pontuacoes[selecao2]["saldo"]:
        return pontuacoes[selecao1]["saldo"] - pontuacoes[selecao2]["saldo"]
    
    # 3. Gols Marcados
    elif pontuacoes[selecao1]["gols_marcados"] != pontuacoes[selecao2]["gols_marcados"]:
        return pontuacoes[selecao1]["gols_marcados"] - pontuacoes[selecao2]["gols_marcados"]
    
    # 4. Confronto Direto (Apenas em ambiente interno de um grupo)
    else:
        if jogos_grupo is not None:
            confronto = Realizar_Confronto_Direto(selecao1, selecao2, jogos_grupo)
            if confronto != 0:
                return confronto

    # 5. Sorteio
    return random.choice([-1, 1])


def Classificar_Grupo(jogos: list, grupo: str) -> list:
    """Classifica as seleções de um grupo específico, indo do 1º colocado ao 4º colocado.
    
    :param jogos: uma lista contendo todos os jogos, com todos os resultados
    :type jogos: list

    :param grupo: grupo (A, B, C, D...) cujas seleções terão seus pontos calculados
    :type grupo: str

    :return: uma lista com as seleções de um grupo ordenadas pela classificação (1º ao 4º).
    :rtype: list
    """
    
    pontuacoes = Calcular_Pontuacoes_Grupo(jogos, grupo)
    selecoes = list(pontuacoes.keys()) 
    jogos_grupo = [jogo for jogo in jogos if jogo["grupo"] == grupo and jogo["fase"] == 1]

    # Transforma o comparador em uma função de chave utilizável pelo sorted()
    def Comparar(selecao1, selecao2):
        return _Comparador_Criterios(selecao1, selecao2, pontuacoes, jogos_grupo)

    return sorted(selecoes, key=functools.cmp_to_key(Comparar), reverse=True)


def Classificar_Selecoes(pontuacoes: list) -> list:
    """Classifica todas as seleções de forma generalizada, sem levar em consideração um grupo específico.

    :param: pontuacoes: um dicionário contendo as pontuações de cada seleção
    :type pontuacoes: dict

    :return: uma lista contendo tuplas cujos elemento são, respectivamente, nome da seleção e suas pontuações
    :rtype: list
    """

    # "Transforma" a lista recebida em um dicionário de pontuacoes temporário para que se faça a comparação
    pontuacoes_temporarias = {selecao: pontuacao for selecao, pontuacao in pontuacoes}
    selecoes = list(pontuacoes_temporarias.keys())

    def comparar(selecao1, selecao2):
        return _Comparador_Criterios(selecao1, selecao2, pontuacoes_temporarias, jogos_grupo=None)

    classificacao_selecoes = sorted(selecoes, key=functools.cmp_to_key(comparar), reverse=True)
    return [(selecao, pontuacoes_temporarias[selecao]) for selecao in classificacao_selecoes]


def Obter_Vencedor(jogo: dict) -> str:
    """Obtém o vencedor de um jogo.

    :param jogo: uma lista contendo todos os jogos, com todos os resultados
    :type jogo: dict
    
    :return: o vencedor de um jogo
    :rtype: str
    """

    if jogo["gols1"] > jogo["gols2"]:
        return jogo["selecao1"]
    elif jogo["gols2"] > jogo["gols1"]:
        return jogo["selecao2"]
    else:
        return jogo["vencedor_penaltis"]

def Obter_Perdedor(jogo: dict) -> str:
    """Obtém o perdedor de um jogo.

    :param jogo: uma lista contendo todos os jogos, com todos os resultados
    :type jogo: dict
    
    :return: o perdedor de um jogo
    :rtype: str
    """
    
    if jogo["gols1"] < jogo["gols2"]:
        return jogo["selecao1"]
    elif jogo["gols2"] < jogo["gols1"]:
        return jogo["selecao2"]
    else:
        if jogo["vencedor_penaltis"] == jogo["selecao1"]:
            return jogo["selecao2"]
        else:
            return jogo["selecao1"]


def Gerar_Primeira_Fase(grupos: dict) -> list:
    """Gera os todos os jogos da primeira fase.

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


def Gerar_Classificados_Fase2(jogos: list) -> list:
    """Classifica as 32 melhores seleções que passam para os 16-avos de Final. 
    Isso é feito da seguinte forma:
    - Obtém os 12 primeiros, 12 segundos e os 8 melhores terceiros colocados.

    :param jogos: lista que contém todos os jogos (da Primeira Fase)
    :type: list

    :return: uma lista contendo os nomes das 32 seleções classificadas para os 16-avos de Final
    :rtype: list
    """
    
    grupos = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    primeiros, segundos, terceiros = [], [], []

    for grupo in grupos:
        pontuacoes = Calcular_Pontuacoes_Grupo(jogos, grupo)
        classificacao = Classificar_Grupo(jogos, grupo)


        # Proteção para garantir que o grupo foi devidamente preenchido
        if len(classificacao) == 4:
            primeiros.append((classificacao[0], pontuacoes[classificacao[0]]))
            segundos.append((classificacao[1], pontuacoes[classificacao[1]]))
            terceiros.append((classificacao[2], pontuacoes[classificacao[2]]))

    # "Filtra" somente os 8 melhores terceiros colocados dos 12 totais
    top8_terceiros = Classificar_Selecoes(terceiros)[:8]

    # Une todas as 32 seleções qualificadas e as classifica entre si
    todos_qualificados = primeiros + segundos + top8_terceiros
    classificacao_geral = Classificar_Selecoes(todos_qualificados)

    # Retorna apenas os nomes das 32 melhores seleções
    return [selecao for selecao, _ in classificacao_geral]


def Verificar_Fase_Completa(jogos: list) -> bool:
    """Verifica se todos os jogos estão preenchidos.
    Evita que haja alguma Fase, atual ou anterior, com algum jogo com -1 "gols".

    :param jogos: uma lista que contém todos os jogos.
    :type: list

    :return: False se houver algum jogo com -1 "gols", True se todos os jogos estão preenchidos 
    :rtype: bool
    """
    
    for jogo in jogos:
        if (jogo["gols1"] <= -1 or jogo["gols2"] <=-1):
            return False
    
    return True


def Obter_Fase_Atual(jogos: list) -> int:
    return max(jogo["fase"] for jogo in jogos)


def Obter_ID_Atual(jogos: list) -> int:
    return max(jogo["id"] for jogo in jogos)


def Gerar_Proxima_Fase(jogos: list) -> list:
    """Gera todos os novos jogos da próxima Fase.
    
    - Se a Fase atual for a 1º: Organiza a Fase 2 com de modo espelhado (1º vs 32º, 2º vs 31º...).
    - Se a Fase atual for a 2º e a 3º: Obtém os vencedores de cada rodada e os organiza de modo espelhado.
    - Se a Fase atual for a 4º: ... 
    - Se a Fase atual for a 5º: ...

    :param jogos: uma lista que contém todos os jogos.
    :type jogos: list

    :return: uma lista contendo os jogos da próxima fase.
    :rtype: list
    """


    if(not Verificar_Fase_Completa(jogos)):
        return None


    novos_jogos = []
    id_atual = Obter_ID_Atual(jogos) + 1
    fase_atual = Obter_Fase_Atual(jogos)

    # Transição da Fase de Grupos (1) para os Dezesseis-avos de Final (2)
    if fase_atual == 1:
        classificados = Gerar_Classificados_Fase2(jogos)

        # Cruzamento "espelhado"
        esquerda = 0
        direita = len(classificados) - 1

        while esquerda < direita:
            partida = {
                "id": id_atual,
                "fase": 2,
                "grupo": "None",
                "selecao1": classificados[esquerda],
                "selecao2": classificados[direita],
                "gols1": -1,
                "gols2": -1,
                "vencedor_penaltis": None
            }

            novos_jogos.append(partida)
            id_atual += 1
            esquerda += 1
            direita -= 1

    elif fase_atual in [2, 3, 4]:
        # Coleta e ordena os jogos da fase que acabou por ID para manter o chaveamento linear
        jogos_concluidos = [jogo for jogo in jogos if jogo["fase"] == fase_atual]
        jogos_concluidos = sorted(jogos_concluidos, key=lambda jogo: jogo["id"])


        esquerda = 0
        direita = len(jogos_concluidos) - 1
        while esquerda < direita:

            vencedor1 = Obter_Vencedor(jogos_concluidos[esquerda])
            vencedor2 = Obter_Vencedor(jogos_concluidos[direita])

            partida = {
                "id": id_atual,
                "fase": fase_atual + 1,
                "grupo": "None",
                "selecao1": vencedor1,
                "selecao2": vencedor2,
                "gols1": -1,
                "gols2": -1,
                "vencedor_penaltis": None
            }

            novos_jogos.append(partida)
            id_atual += 1
            esquerda += 1
            direita -= 1

    elif fase_atual == 5:

         # Coleta e ordena os jogos da fase que acabou por ID para manter o chaveamento linear
        jogos_concluidos = [jogo for jogo in jogos if jogo["fase"] == fase_atual]
        jogos_concluidos = sorted(jogos_concluidos, key=lambda jogo: jogo["id"])

        vencedor1 = Obter_Vencedor(jogos_concluidos[0])
        vencedor2 = Obter_Vencedor(jogos_concluidos[len(jogos_concluidos) - 1])

        perdedor1 = Obter_Perdedor(jogos_concluidos[0])
        perdedor2 = Obter_Perdedor(jogos_concluidos[len(jogos_concluidos) - 1])

        partida1 = {
            "id": 103,
            "fase": fase_atual + 1,
            "grupo": "None",
            "selecao1": perdedor1,
            "selecao2": perdedor2,
            "gols1": -1,
            "gols2": -1,
            "vencedor_penaltis": None
        }
        
        partida2 = {
            "id": 104,
            "fase": fase_atual + 1,
            "grupo": "None",
            "selecao1": vencedor1,
            "selecao2": vencedor2,
            "gols1": -1,
            "gols2": -1,
            "vencedor_penaltis": None
        }

        novos_jogos.append(partida1)
        novos_jogos.append(partida2)


    return novos_jogos


def Exibir_Jogo(jogo: dict):
    """Exibe um jogo específico em um formato padrão.

    :param jogo: um dicionário que representa um jogo específico a ser exibido.
    :type jogo: dict
    """

    fases = {
        1: "Primeira Fase",
        2: "16-avos de Final",
        3: "Oitavas de Final",
        4: "Quartas de Final",
        5: "Semifinal",
        6: "Final"}
    
    print(f"""
    ID: {jogo['id']}
    Fase: {fases[jogo['fase']]}
    Grupo: {jogo['grupo']}
    Partida: {jogo['selecao1']} x {jogo['selecao2']}""")
