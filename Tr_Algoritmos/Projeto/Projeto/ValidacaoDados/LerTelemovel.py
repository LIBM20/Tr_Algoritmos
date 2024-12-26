import re

def ValidaTelemovel(email):
    if re.search("^(91|92|93|96|)[0-9]{7}$", email):  # No match
        return True
    return False

def LerTelemovel(legenda):
    while True:
        e = input(legenda)
        if ValidaTelemovel(e):
            return e
        else:
            print("\033[0:91m%s inválido\033[0m" % legenda)
    return e


def LerTelemovel2(legenda):
    while True:
        e = input(legenda)
        if e == '':
            return None
        if ValidaTelemovel(e):
            return e
        else:
            print("\033[0:91m%s inválido\033[0m" % legenda)
    return e
