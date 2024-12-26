def LerNumero(msg, min, max, tipo="inteiro"):
    if tipo not in ["inteiro", "real"]:
        tipo = "real"
    while True:
        try:
            if tipo=="inteiro":
                n = int(input(msg))
            else:
                n = float(input(msg))
        except ValueError:
            print ("\033[0:91mNão digitou um número %s!\033[0m" % tipo)
            continue
        if n >= min and n <= max:
            break
        else:
             if tipo=="inteiro":
                print ("\033[0:91mO valor deve estar entre %d e %d\033[0m" % (min, max))
             else:
                print ("\033[0:91mO valor deve estar entre %f e %f\033[0m" % (min, max))
    return n

def LerNumero2(msg, min, max, tipo="inteiro"):
    if tipo not in ["inteiro", "real"]:
        tipo = "real"
    while True:
        try:
            s = input(msg)
            if s == '':
                return None
            if tipo=="inteiro":
                n = int(s)
            else:
                n = float(s)
        except ValueError:
            print ("\033[0:91mNão digitou um número %s!\033[0m" % tipo)
            continue
        if n >= min and n <= max:
            break
        else:
             if tipo=="inteiro":
                print ("\033[0:91mO valor deve estar entre %d e %d\033[0m" % (min, max))
             else:
                print ("\033[0:91mO valor deve estar entre %f e %f\033[0m" % (min, max))
    return n
