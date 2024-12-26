import re

def ValidaEMail(email):
    if re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):  # No match
        return True
    return False

def ValidaEMail2(email):
    if re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):  # No match
        return True
    return False

def LerEMail(legenda):
    while True:
        e = input(legenda)
        if ValidaEMail(e):
            return e
        else:
            print("\033[0:91m%s inválido\033[0m" % legenda)
    return e

def LerEMail2(legenda):
    while True:
        e = input(legenda)
        if e == '':
            return None
        if ValidaEMail(e):
            return e
        else:
            print("\033[0:91m%s inválido\033[0m" % legenda)
    return e
