def Validar_Apostador(nome: str):
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
            return 
        

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


def Existe_Gabarito():
    
    try:
        open('dados/resultados/gabarito.json', 'r', encoding='utf-8')
        return True
    except FileNotFoundError:
        return False
