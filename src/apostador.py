def CadastrarApostador(nomearquivo):
    with open(nomearquivo, 'a+', encoding='utf-8') as arq: ## a+ é leitura e escrita sem apagar, nao substitui o texto, adiciona
        nome = input("Insira o nome do novo apostador: ")
        arq.seek(0) # o a+ faz o arquivo iniciar no final, isso aqui faz ele voltar pro inicio
        if nome.lower() in [linha.strip().lower() for linha in arq]: #Verifica se o nome é repetido
            return print("Erro: Apostador já cadastrado!")
        arq.write('\n'+nome )
        


CadastrarApostador('Archives/apostadores.txt')