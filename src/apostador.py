import json
from src.submenu import Sub_Menu_Interativo, Exibir_Tutorial_B

def Atualizar_Arquivo_Palpites(jogos: list, apostador: str):
    """Atualiza/Cria um arquivo de palpites pera um apostador

    :param jogos: uma lista de jogos contendo cada partida.
    :type jogos: list

    :param apostador: nome do apostador
    :type apostador: str
    """

    with open(f'Archives/json/palpites_{apostador}.json', 'w', encoding='utf-8') as arq:
        json.dump(jogos, arq, indent=4, ensure_ascii=False)


def Atualizar_Palpites(apostador: str, jogos: list, id: str, gols1: str, gols2: str):
    """Atualiza o palpite de um dados apostador em um jogo específico.

    :param apostador: nome do apostador.
    :type apostador: str
    
    :param jogos: lista contendo todos os jogos, com ou sem palpites, do apostdor.
    :type jogos: list
    
    :param id: ID do jogo que o apostador deseja alterar.
    :type id: str
    
    :param gols1: número de gols da primeira seleção.
    :type gols1: str
    
    :param gols2: número de gols da segunda seleção.
    :type gols2: str
    """
    
    for jogo in jogos:
        if(jogo['id'] == int(id)):
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

def Cadastrar_Apostador(jogos: list):
    """Cadastra um novo apostador

    :param nomearquivo: nome do arquivo que conterá os apostadores
    :type nomearquivo: str

    :param jogos: uma lista de jogos contendo cada partida.
    :type jogos: list
    """

    nome = input("Insira o nome do novo apostador: ")
    with open('Archives/txt/apostadores.txt', 'a+', encoding='utf-8') as arq: ## a+ é leitura e escrita sem apagar, nao substitui o texto, adiciona
        if(Validar_Jogador(nome)):
            print("Erro: Apostador já cadastrado!")
            return None
        
        arq.write('\n'+nome )

    Atualizar_Arquivo_Palpites(jogos, nome)


def Carregar_Palpites(apostador: str) -> list:
    """Carrega os palpites do arquivo de um apostador.

    :param apostador: nome do apostador.
    :type apostador: str

    :return: uma lista de todos os jogos, com ou sem palpites, do arquivo.
    :rtype: list
    """    

    with open(f'Archives/json/palpites_{apostador}', 'r', encoding='utf-8') as arq:
        jogos = json.load(arq)
    return jogos



def Cadastrar_Palpites(modo: str):
    """Verifica qual modo de cadastro de palpites o apostador escolheu.
    
    :param modo: modo de cadastro de palpites escolhido pelo apostador: 'a' --> cadastro interativo; 'b' --> cadastro em lote.
    :type modo: str

    :return False: retorna False se ocorreu algum erro durante o cadastro de palpites.
    :rtype: bool

    :return None: retorna None para informar ao sistema para parar sua execução.
    :rtype None:
    """
    
    if (modo.lower() != 'a' and modo.lower() != 'b'):
        print("ERRO: jogador não selecionou uma opção válida!")
        return False
    

    apostador = input("Nome do apostador: ")
    if (modo.lower() == 'a'):

        if(Validar_Jogador(apostador)):
            Sub_Menu_Interativo(apostador)
            
        else:
            print("Erro! Apostador não cadastrado no sistema.")
            return False
    else:
       Exibir_Tutorial_B(apostador)
       return None
