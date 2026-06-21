def jogos_por_grupo(jogos, grupo_escolhido):
    '''função recebe os grupo escolhido no menu e demonstra os jogos e placares desse grupo
    jogos: arquivo contendo a lista de dicionarios com todos os dados sobre os jogos(id, placar, times, etc.)
    grupo_escolhido: variavel escolhida pelo usuario para acessar o grupo em jogos
    '''
    for jogo in jogos:
        if jogo['grupo'] == grupo_escolhido:
            print(f"      Grupo: {grupo_escolhido}    ")
            gols1 = jogo["gols1"] if jogo["gols1"] != -1 else ""
            gols2 = jogo["gols2"] if jogo["gols2"] != -1 else ""
            print(f"ID do jogo: {jogo[id]}\n")
            print(f"{jogo['selecao1']} {gols1} X {gols2} {jogo['selecao2']} \n ")
