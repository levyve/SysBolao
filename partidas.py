import string #pra função de pegar os ascii

def CarregarSelecoes(nomearquivo):
    grupos = {}
    
    with open(nomearquivo, 'r', encoding='utf-8') as arq:
        selecoes = [linha.strip() for linha in arq] ##lê e separa, é um laço FOR normal
    
    # ve se tem 48 linha
    if len(selecoes) != 48:
        print("Número de linhas é diferente de 48, carregamento cancelado")
        return None
        
    #linha vazias
    if "" in selecoes:
        print("Linha vazia, carregamento cancelado")
        return None

    #se tem repetição
    if len(selecoes) != len(set(selecoes)):
        print("Existem seleções repetidas, carregamento cancelado")
        return None

   
    letras = list(string.ascii_uppercase)[:12]  # Pega as letras de A-L
    for i in range(12):
        letra = letras[i]
        # pra fatiar
        inicio = i * 4
        fim = inicio + 4
        #
        grupos[letra] = selecoes[inicio:fim] 
        
    print("Sucesso: Grupos estruturados com sucesso!")
    print (grupos)
    return grupos


CarregarSelecoes('selecoes.txt')
