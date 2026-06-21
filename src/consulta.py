def Listar_Calendario(jogos):
    '''mostra todas as partidas realizadas e as proximas!'''
    print("\n==========================================") 
    print("          LISTA DE CALENDÁRIOS           ")
    print("==========================================")
    for jogo in jogos:
        gols1 = jogo["gols1"] if jogo["gols1"] != -1 else ""
        gols2 = jogo["gols2"] if jogo["gols2"] != -1 else ""
        print(f"ID: {jogo['ID']} - Fase: {jogo['fase']} - Grupo: {jogo['grupo']} ")
        print(f"\n  {jogo['selecao1']} {gols1} X {gols2} {jogo['selecao2']}\n")

def jogos_por_fase(jogos):
    '''função  o dicionario de jogos
    jogos: arquivo contendo a lista de dicionarios com todos os dados sobre os jogos(id, placar, times, etc.)
    fase_escolhida: variavel escolhida pelo usuario para acessar o grupo em jogos
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
    fase_escolhida = int(input("digite o numero da fase que você pretende checar: "))
    fase_escolhida = fases[fase_escolhida - 1]
    print(f"           Fase: {fase_escolhida}    ")
    print("------------------------------------------")
    fase_gerada = False
    for jogo in jogos:
        if jogo['fase'] == fase_escolhida:
            fase_gerada = True
            gols1 = jogo["gols1"] if jogo["gols1"] != -1 else ""
            gols2 = jogo["gols2"] if jogo["gols2"] != -1 else ""
            if jogo['grupo'] != "não":
                print(f"Grupo: {jogo['grupo']}\n ID do jogo: {jogo['id']}\n")
            else:
                print(f"ID do jogo: {jogo['id']}\n")
            print(f"{jogo['selecao1']} {gols1} X {gols2} {jogo['selecao2']} \n ")
    if not fase_gerada:
        print(f"O(s) jogo(s) da(s) {fase_escolhida} ") 

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
    id_escolhido = input("digite o numero do id do jogo que você pretende checar: ")
    id_gerado = False
    for jogo in jogos:
        if jogo['id'] == id_escolhido:
            id_gerado = True
            gols1 = jogo["gols1"] if jogo["gols1"] != -1 else ""
            gols2 = jogo["gols2"] if jogo["gols2"] != -1 else ""            
            print(f"ID: {jogo['id']}")
            print(f"{jogo['selecao1']} {gols1} X {gols2} {jogo['selecao2']}")
            break
    if not id_gerado:
        print(f"a partida de ID: {id_escolhido} ainda não ocorreu")
        #depois possivelmente botar um limite de IDs, tipo a partidade de ID: 1337 não está ocorrerá, os ID(s) variam de 1 a x             