def CadastrarApostador(nomearquivo):
    with open(nomearquivo, 'a', encoding='utf-8') as arq:
        nome = input("Insira o nome do novo apostador: ")
        arq.write(nome + '\n')

CadastrarApostador('Archives/apostadores.txt')