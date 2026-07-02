from functools import cmp_to_key
import random


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

    return sorted(selecoes, key=cmp_to_key(Comparar), reverse=True)


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

    classificacao_selecoes = sorted(selecoes, key=cmp_to_key(comparar), reverse=True)
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
