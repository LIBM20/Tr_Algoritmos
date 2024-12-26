import re

def ValidaAssunto(assunto):
    if re.search("^[A-Z][a-z 0-9@#?!]{5,80}$", assunto):  # No match
        return True
    return False

def LerAssunto(legenda):
    while True:
        nome = input(legenda)
        if ValidaAssunto(nome):
            return nome
        else:
            print("\033[0:91mAssunto inválido.\033[0m")

def LerAssunto2(legenda):
    while True:
        nome = input(legenda)
        if nome == '':
            return None
        if ValidaAssunto(nome):
            return nome
        else:
            print("\033[0:91mAssunto inválido.\033[0m")


