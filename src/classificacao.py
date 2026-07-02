from functools import cmp_to_key
from src.gabarito import Carregar_Gabarito
from src.apostador import Carregar_Palpites


PONTOS_EXATO = 10
PONTOS_PARCIAL = 7
PONTOS_RESULTADO = 5
PONTOS_ERRO = 0
PONTOS_SEM_PALPITE = 0

MAPA_CATEGORIAS = {
    "exato": "exatos",
    "parcial": "parciais",
    "resultado": "resultados",
    "erro": "erros",
    "sem_palpite": "sem_palpite",
}

def Obter_Resultado(gols1: int, gols2: int) -> int:
    """Obtém o resultado de uma partida com base na quantidade de gols de cada seleção.

    :param gols1: gols da primeira seleção.
    :type gols1: int

    :param gols2: gols da segunda seleção.
    :type gols2: int

    :return: 1 se a primeira seleção venceu, -1 se a segunda venceu, 0 se houve empate.
    :rtype: int
    """

    if gols1 > gols2:
        return 1
    elif gols2 > gols1:
        return -1
    else:
        return 0


def Classificar_Palpite(palpite: dict, jogo_gabarito: dict) -> tuple:
    """Classifica um palpite específico com base no resultado oficial do gabarito.

    :param palpite: dicionário contendo o palpite do apostador para a partida.
    :type palpite: dict

    :param jogo_gabarito: dicionário contendo o resultado oficial da partida.
    :type jogo_gabarito: dict

    :return: uma tupla (categoria, pontos), em que categoria é "exato", "parcial", "resultado" ou "erro".
    :rtype: tuple
    """

    palpite_gols1, palpite_gols2 = palpite['gols1'], palpite['gols2']
    gabarito_gols1, gabarito_gols2 = jogo_gabarito['gols1'], jogo_gabarito['gols2']

    if palpite_gols1 == -1 or palpite_gols2 == -1:
        return ("sem_palpite", PONTOS_SEM_PALPITE)

    if palpite_gols1 == gabarito_gols1 and palpite_gols2 == gabarito_gols2:
        return ("exato", PONTOS_EXATO)

    resultado_palpite = Obter_Resultado(palpite_gols1, palpite_gols2)
    resultado_gabarito = Obter_Resultado(gabarito_gols1, gabarito_gols2)

    if resultado_palpite != resultado_gabarito:
        return ("erro", PONTOS_ERRO)

    acertou_gols1 = (palpite_gols1 == gabarito_gols1)
    acertou_gols2 = (palpite_gols2 == gabarito_gols2)

    if acertou_gols1 or acertou_gols2:
        return ("parcial", PONTOS_PARCIAL)

    return ("resultado", PONTOS_RESULTADO)


def Calcular_Pontuacao_Apostador(apostador: str, jogos_gabarito: list) -> dict:
    """Calcula a pontuação total e as estatísticas de um apostador com base no gabarito oficial.

    :param apostador: nome do apostador.
    :type apostador: str

    :param jogos_gabarito: lista contendo todos os jogos do gabarito oficial.
    :type jogos_gabarito: list

    :return: dicionário com o nome do apostador e suas estatísticas (pontos, exatos, parciais, resultados, erros).
    :rtype: dict
    """

    estatisticas = {
        "apostador": apostador,
        "pontos": 0,
        "exatos": 0,
        "parciais": 0,
        "resultados": 0,
        "erros": 0,
        "sem_palpite": 0,
    }

    try:
        palpites = Carregar_Palpites(apostador)
    except FileNotFoundError:
        palpites = None

    for jogo_gabarito in jogos_gabarito:
        if jogo_gabarito['gols1'] == -1 or jogo_gabarito['gols2'] == -1:
            continue

        palpite = None
        if palpites is not None:
            palpite = next((p for p in palpites if p['id'] == jogo_gabarito['id']), None)

        if palpite is None:
            categoria, pontos = "sem_palpite", PONTOS_SEM_PALPITE
        elif palpite['gols1'] == -1 or palpite['gols2'] == -1:
            categoria, pontos = "sem_palpite", PONTOS_SEM_PALPITE    
        else:
            categoria, pontos = Classificar_Palpite(palpite, jogo_gabarito)

        estatisticas["pontos"] += pontos
        estatisticas[MAPA_CATEGORIAS[categoria]] += 1

    return estatisticas


def _Comparador_Classificacao(apostador1: dict, apostador2: dict) -> int:
    """Compara dois apostadores segundo os critérios de desempate:
    1. Pontos;
    2. Placares exatos;
    3. Placares parciais;
    4. Resultados corretos;
    5. Menor número de erros;
    6. Ordem alfabética do nome.

    :param apostador1: estatísticas do primeiro apostador.
    :type apostador1: dict

    :param apostador2: estatísticas do segundo apostador.
    :type apostador2: dict

    :return: número negativo se apostador1 deve vir antes de apostador2, positivo caso contrário, 0 se empatarem.
    :rtype: int
    """

    if apostador1["pontos"] != apostador2["pontos"]:
        return apostador2["pontos"] - apostador1["pontos"]

    if apostador1["exatos"] != apostador2["exatos"]:
        return apostador2["exatos"] - apostador1["exatos"]

    if apostador1["parciais"] != apostador2["parciais"]:
        return apostador2["parciais"] - apostador1["parciais"]

    if apostador1["resultados"] != apostador2["resultados"]:
        return apostador2["resultados"] - apostador1["resultados"]

    if apostador1["erros"] != apostador2["erros"]:
        return apostador1["erros"] - apostador2["erros"]

    nome1, nome2 = apostador1["apostador"].lower(), apostador2["apostador"].lower()
    if nome1 != nome2:
        return -1 if nome1 < nome2 else 1

    return 0


def Gerar_Classificacao_Final() -> list:
    """Gera a classificação final do bolão, calculando e ordenando a pontuação de todos os apostadores.

    :return: lista de dicionários com as estatísticas de cada apostador, ordenada da melhor para a pior colocação.
    :rtype: list
    """

    with open('Archives/txt/apostadores.txt', 'r', encoding='utf-8') as arq:
        apostadores = [linha.strip() for linha in arq if linha.strip() != ""] #Pequeno laço for reduzido, nada de surpreendente. Se a linha nao for vazia, pra cada linha.strip() ele taca em apostadores
    jogos_gabarito = Carregar_Gabarito()

    classificacao = [Calcular_Pontuacao_Apostador(apostador, jogos_gabarito) for apostador in apostadores]
    classificacao = sorted(classificacao, key=cmp_to_key(_Comparador_Classificacao))

    return classificacao


def Exibir_Classificacao_Final(classificacao: list):
    """Exibe a classificação final do bolão formatada em uma tabela.

    :param classificacao: lista de dicionários com as estatísticas de cada apostador, já ordenada.
    :type classificacao: list
    """

    print("\n******** Resultado Final do Bolão ********")
    print(f"{'Posição':<10}{'Apostador':<15}{'Pontos':<8}{'Exatos':<8}{'Parciais':<10}{'Resultados':<12}{'Erros':<8}")

    for posicao, apostador in enumerate(classificacao, start=1):
        print(f"{str(posicao) + 'º':<10}{apostador['apostador']:<15}{apostador['pontos']:<8}{apostador['exatos']:<8}{apostador['parciais']:<10}{apostador['resultados']:<12}{apostador['erros']:<8}")


def Salvar_Classificacao_Final(classificacao: list):
    """Salva a classificação final do bolão em um arquivo de texto.

    :param classificacao: lista de dicionários com as estatísticas de cada apostador, já ordenada.
    :type classificacao: list
    """

    with open('Archives/txt/resultado_bolao.txt', 'w', encoding='utf-8') as arq:
        arq.write("******** Resultado Final do Bolão ********\n")
        arq.write(f"{'Posição':<10}{'Apostador':<15}{'Pontos':<8}{'Exatos':<8}{'Parciais':<10}{'Resultados':<12}{'Erros':<8}\n")

        for posicao, apostador in enumerate(classificacao, start=1):
            arq.write(f"{str(posicao) + 'º':<10}{apostador['apostador']:<15}{apostador['pontos']:<8}{apostador['exatos']:<8}{apostador['parciais']:<10}{apostador['resultados']:<12}{apostador['erros']:<8}\n")

    print("\nResultado salvo com sucesso, Consulte no arquivo 'resultado_bolao.txt' na pasta arquivos/txt")


def Resultado_Final_Bolao():
    """Calcula, exibe e, opcionalmente, salva a classificação final do bolão.
    """

    try:
        open('Archives/json/gabarito.json', 'r', encoding='utf-8')
    except FileNotFoundError:
        print("ERRO: o arquivo JSON do gabarito oficial ainda não foi criado!\nPara criar o arquivo do gabarito oficial, vá em 'Cadastrar Gabarito Oficial', no menu principal.")
        return

    classificacao = Gerar_Classificacao_Final()
    Exibir_Classificacao_Final(classificacao)

    resposta = input("\nDeseja salvar o resultado em arquivo? (s/n): ").strip().lower()
    if resposta == 's':
        Salvar_Classificacao_Final(classificacao)