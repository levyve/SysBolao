import string #pra função de pegar os ascii

def CarregarSelecoes(nomearquivo):
    selecoes = []
    grupos = {}
    with open (nomearquivo, 'r', encoding='utf-8') as arq:
        for linha in arq:
            if linha == '':
                print("Linha vazia, carregamento cancelado")
                return None
            if len(arq.readlines()) != 48:
                print("Número de linhas é diferente de 48, carregamento cancelado")
            selecao = linha.split(',')
            selecoes.append(selecao)
        letras = list(string.ascii_uppercase)[:12]  #Pega as letras de A-L
        for i in range(12):
            letra = letras[i]
            # pra fatiar
            inicio = i * 4
            fim = inicio + 4
            #
            grupos[letra] = selecoes[inicio:fim]
            
        print("Sucesso: Grupos estruturados com sucesso!")
        return grupos