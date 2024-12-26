def LerDeLista(legenda, lista):
    while True:
        escolha = input(legenda.replace('?','') + ' (' + ', '.join(lista) + ')?')
        if escolha in lista:
            return escolha
        else:
            print("\033[0:91mO valor tem de ser um da lista:", lista)
            print("\033[m")


def LerDeLista2(legenda, lista):
    while True:
        escolha = input(legenda.replace('?','') + ' (' + ', '.join(lista) + ')?')
        if escolha == '':
            return None
        if escolha in lista:
            return escolha
        else:
            print("\033[0:91mO valor tem de ser um da lista:", lista)

