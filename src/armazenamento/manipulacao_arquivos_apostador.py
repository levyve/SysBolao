import json
from src.palpites import Validar_Jogador

def Carregar_Palpites(apostador: str) -> list:
    """Carrega os palpites do arquivo de um apostador.

    :param apostador: nome do apostador.
    :type apostador: str

    :return: uma lista de todos os jogos, com ou sem palpites, do arquivo.
    :rtype: list
    """    

    with open(f'dados/apostadores/palpites_{apostador.lower()}.json', 'r', encoding='utf-8') as arq:
        jogos = json.load(arq)
    return jogos


def Criar_Arquivo_Apostador(apostador: str):
    """Cria um arquivo de palpites de um apostador.
    
    :param apostador: nome do apostador
    :type apostador: str
    """

    with open('dados/base/estrutura_jogos.json', 'r', encoding='utf-8') as arq:
        jogos = json.load(arq)

    with open(f'dados/apostadores/palpites_{apostador.lower()}.json', 'w', encoding='utf-8') as arq:
        json.dump(jogos, arq, indent=4, ensure_ascii=False)


def Atualizar_Arquivo_Palpites(jogos: list, apostador: str):
    """Atualiza um arquivo de palpites de um apostador.

    :param jogos: lista contendo todos os jogos, com ou sem palpites, do apostdor.
    :type jogos: list

    :param apostador: nome do apostador
    :type apostador: str
    """

    with open(f'dados/apostadores/palpites_{apostador.lower()}.json', 'w', encoding='utf-8') as arq:
            json.dump(jogos, arq, indent=4, ensure_ascii=False)


def Cadastrar_Apostador(nome: str):
    """Cadastra um novo apostador

    :param nome: nome do apostador que será cadastrado
    :type nome: str
    """

    with open('dados/apostadores/apostadores.txt', 'a+', encoding='utf-8') as arq: ## a+ é leitura e escrita sem apagar, nao substitui o texto, adiciona
        if(Validar_Jogador(nome)):
            print("Erro: Apostador já cadastrado!")
            return None
        
        arq.write('\n'+nome )

    Criar_Arquivo_Apostador(nome)

