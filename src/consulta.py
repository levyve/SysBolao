import json
#importado para consultar gabarito e palpites
def Listar_Calendario(jogos):
    '''mostra todas as partidas realizadas e as proximas!'''

    print("\n==========================================") 
    print("          LISTA DE CALENDÁRIOS           ")
    print("==========================================")
    for jogo in jogos:
        gols1 = jogo["gols1"] if jogo["gols1"] != -1 else ""
        gols2 = jogo["gols2"] if jogo["gols2"] != -1 else ""
        if jogo['grupo'] != "None":
            print(f"ID: {jogo['id']} - Fase: {jogo['fase']} - Grupo: {jogo['grupo']} ")
        else:
            print(f"ID: {jogo['id']} - Fase: {jogo['fase']} ")    
        print(f"\n  {jogo['selecao1']} {gols1} X {gols2} {jogo['selecao2']}\n")

def jogos_por_fase(jogos):
    '''função  o dicionario de jogos
    jogos: arquivo contendo a lista de dicionarios com todos os dados sobre os jogos(id, placar, times, etc.)
    numero_fase: variavel escolhida pelo usuario para acessar o grupo em jogos
    fases: converte numero em string
    '''

    fases = ["Fase de grupos", "16-avos de final", "Oitavas de final", "Quartas de final", "Semifinais", "Disputa de 3º lugar", "final" ]
    print("        FASES:")
    print("----------------------")
    print("1 -  Fase de grupos")
    print("2 -  16-avos de final")
    print("3 -  Oitavas de final")
    print("4 -  Quartas de final")
    print("5 -  Semifinais")
    print("6 -  Disputa de 3º lugar")
    print("7 -  final")
    numero_fase = int(input("digite o numero da fase que você pretende checar: "))
    numero_fase = fases[numero_fase - 1]
    print(f"           Fase: {numero_fase}    ")
    print("------------------------------------------")
    fase_gerada = False
    for jogo in jogos:
        if jogo['fase'] == numero_fase:
            fase_gerada = True
            gols1 = jogo["gols1"] if jogo["gols1"] != -1 else ""
            gols2 = jogo["gols2"] if jogo["gols2"] != -1 else ""
            if jogo['grupo'] != "None":
                print(f"Grupo: {jogo['grupo']}\n ID do jogo: {jogo['id']}\n")
            else:
                print(f"ID do jogo: {jogo['id']}\n")
            print(f"{jogo['selecao1']} {gols1} X {gols2} {jogo['selecao2']} \n ")
    if not fase_gerada:
        print(f"Nenhum jogo encontrado para {numero_fase}") 

def jogos_por_grupo(jogos):
    '''função recebe os grupo escolhido no menu e demonstra os jogos e placares desse grupo
    jogos: arquivo contendo a lista de dicionarios com todos os dados sobre os jogos(id, placar, times, etc.)
    grupo_escolhido: variavel escolhida pelo usuario para acessar o grupo em jogos
    '''
    grupo_escolhido = input("digite o grupo que você pretende checar: ").upper()
    print(f"           Grupo: {grupo_escolhido}    ")
    print("--------------------------------")
    for jogo in jogos:
        if jogo['grupo'] == grupo_escolhido:
            gols1 = jogo["gols1"] if jogo["gols1"] != -1 else ""
            gols2 = jogo["gols2"] if jogo["gols2"] != -1 else ""
            print(f"ID do jogo: {jogo['id']}\n")
            print(f"{jogo['selecao1']} {gols1} X {gols2} {jogo['selecao2']} \n ")
def jogos_por_id(jogos):
    ''' função que demonstra o jogo de um id especifico
    '''

    id_escolhido = input("digite o numero do id do jogo que você pretende checar: ")
    id_gerado = False
    for jogo in jogos:
        if jogo['id'] == int(id_escolhido):
            id_gerado = True
            gols1 = jogo["gols1"] if jogo["gols1"] != -1 else ""
            gols2 = jogo["gols2"] if jogo["gols2"] != -1 else ""            
            print(f"ID: {jogo['id']}")
            print(f"{jogo['selecao1']} {gols1} X {gols2} {jogo['selecao2']}")
            break
    if not id_gerado:
        print(f"a partida de ID: {id_escolhido} ainda não ocorreu")
        #depois possivelmente botar um limite de IDs, tipo a partidade de ID: 1337 não está ocorrerá, os ID(s) variam de 1 a x

def consulta_palpite():
    '''permite usuario consultar seus palpites
    '''    
    nome = input("para ver seus paplpites insira o nome cadastrado no bolão:  ")
    cadastro = False
    with open("Archives/txt/apostadores.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome_original = linha.strip()
            if nome == nome_original:
                cadastro = True
                break
    if not cadastro:
        print("usuário não cadastrado") 
        return
    nome_arquivo_json = f"Archives/json/palpites_{nome_original}.json"
    with open(nome_arquivo_json, "r", encoding="utf-8") as arquivo_json:
         palpites = json.load(arquivo_json)
    print(f"\n Palpites de {nome}:")
    for palpite in palpites:
        gols1 = palpite["gols1"] if palpite["gols1"] != -1 else ""
        gols2 = palpite["gols2"] if palpite["gols2"] != -1 else ""
        print(f"{palpite['selecao1']} {gols1} X {gols2} {palpite['selecao2']}")

def consulta_palpite_pendentes():
    '''permite usuario checar palpites que ainda faltam serem preenchidos
    '''  

    nome = input("para ver seus palpites não realizados insira o nome cadastrado no bolão:  ")
    cadastro = False
    with open("Archives/txt/apostadores.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome_original = linha.strip()
            if nome == nome_original:
                cadastro = True
                break
    if not cadastro:
        print("usuário não cadastrado!") 
        return
    nome_arquivo_json = f"Archives/json/palpites_{nome_original}.json"
    with open(nome_arquivo_json, "r", encoding="utf-8") as arquivo_json:
         palpites = json.load(arquivo_json)
    print(f"\n Palpites pendentes de {nome}:")
    palpites_faltam = False 
    for palpite in palpites:
        gols1 = palpite["gols1"] if palpite["gols1"] != -1 else ""
        gols2 = palpite["gols2"] if palpite["gols2"] != -1 else ""
        if gols1 == "" or gols2 == "":
            print(f"ID: {palpite['id']}")
            print(f"{palpite['selecao1']} {gols1} X {gols2} {palpite['selecao2']}")
            palpites_faltam = True
    if not palpites_faltam:
        print("Todos os palpites estão preenchidos.")

def Visualizar_Gabarito_Oficial(jogos):
    '''função mostra o gabarito oficial, os jogos que já ocorreram'''

    print("\n==========================================") 
    print("          GABARITO OFICIAL!           ")
    print("==========================================")
    for jogo in jogos:
        gols1 = jogo["gols1"] if jogo["gols1"] != -1 else ""
        gols2 = jogo["gols2"] if jogo["gols2"] != -1 else ""
        if gols1 != "" and gols2 != "":
            if jogo['grupo'] != "None":
                print(f"ID: {jogo['id']} - Fase: {jogo['fase']} - Grupo: {jogo['grupo']} ")
            else:
                print(f"ID: {jogo['id']} - Fase: {jogo['fase']} ")    
            print(f"\n  {jogo['selecao1']} {gols1} X {gols2} {jogo['selecao2']}\n")

def Visualizar_Resultados_Pendentes(jogos):            
    '''função demonstra os jogos pendentes'''

    print("\n==========================================") 
    print("          RESULTADOS PENDENTES!           ")
    print("==========================================")
    gabarito_faltam = False
    for jogo in jogos:
        gols1 = jogo["gols1"] if jogo["gols1"] != -1 else ""
        gols2 = jogo["gols2"] if jogo["gols2"] != -1 else ""
        if gols1 == "" and gols2 == "":
            gabarito_faltam = True
            if jogo['grupo'] != "None":
                print(f"ID: {jogo['id']} - Fase: {jogo['fase']} - Grupo: {jogo['grupo']} ")
            else:
                print(f"ID: {jogo['id']} - Fase: {jogo['fase']} ")    
            print(f"\n  {jogo['selecao1']} {gols1} X {gols2} {jogo['selecao2']}\n")
    if not gabarito_faltam:
        print("       Gabarito está completo")
        print("\nPara ver os resultado dos jogos olhe o gabarito oficial")
