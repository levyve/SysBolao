def Listar_Calendario(jogos):
    '''mostra todas as partidas realizadas e as proximas!'''
    print("\n==========================================") 
    print("          LISTA DE CALENDÁRIOS           ")
    print("==========================================")
    for jogo in jogos:
        gols1 = jogo["gols1"] if jogo["gols1"] != -1 else ""
        gols2 = jogo["gols2"] if jogo["gols2"] != -1 else ""
        print(f"ID: {jogo['ID']} - Fase: {jogo['fase']} - Grupo: {jogo['grupo']} ")
        print(f"\n  {jogo['time1']} {gols1} X {gols2} {jogo['time2']}\n")
        