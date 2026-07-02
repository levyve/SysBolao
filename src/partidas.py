from classificacao_selecoes import (
    Calcular_Pontuacoes_Grupo,
    Classificar_Grupo,
    Classificar_Selecoes,
    Obter_Vencedor,
    Obter_Perdedor
)

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

    return jogos


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


def Obter_ID_Maximo(jogos: list) -> int:
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
    id_atual = Obter_ID_Maximo(jogos) + 1
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

    else:
        print("ERRO: Já foram geradas todas as fases possíveis!")
        return None

    return novos_jogos