import json

def Cadastrar_Apostador(jogos: list, nomearquivo: str = "Archives/txt/apostadores.txt"):
    """Cadastro um novo apostador

    :param nomearquivo: nome do arquivo que conterá os apostadores
    :type nomearquivo: str

    :param jogos: uma lista de jogos contendo cada partida.
    :type jogos: list
    """

    with open(nomearquivo, 'a+', encoding='utf-8') as arq: ## a+ é leitura e escrita sem apagar, nao substitui o texto, adiciona
        nome = input("Insira o nome do novo apostador: ")
        arq.seek(0) # o a+ faz o arquivo iniciar no final, isso aqui faz ele voltar pro inicio
        if nome.lower() in [linha.strip().lower() for linha in arq]: #Verifica se o nome é repetido
            return print("Erro: Apostador já cadastrado!")
        arq.write('\n'+nome ) #/n é quebra de linha
        Criar_Arquivo_Palpite(jogos, nome)
    i = input("Aperte enter para continuar")



def Criar_Arquivo_Palpite(jogos: list, apostador: str):
    """Cria um arquivo de palpites pera um apostador

    :param jogos: uma lista de jogos contendo cada partida.
    :type jogos: list

    :param apostador: nome do apostador
    :type apostador: str
    """

    with open(f"Archives/json/palpite_{apostador}.json", "w", encoding="utf-8") as arq:
        json.dump(jogos, arq, indent=4, ensure_ascii=False)