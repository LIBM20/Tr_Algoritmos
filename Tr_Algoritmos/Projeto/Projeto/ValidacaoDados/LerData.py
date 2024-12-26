def LerData(msg, min=None, max=None):
    from datetime import datetime
    while True:
        data_texto = input(msg)
        try:
            data = datetime.strptime(data_texto, '%Y-%m-%d')
        except ValueError:
            print("\033[0:91mData inválida. Formato AAAA-MM-DD.\033[0m")
            continue
        c=0
        if min == None:
            c = 1
        elif data >= min:
            c = 1
        if max == None:
            c = c + 1
        elif data <= max:
            c = c + 1
        if c != 2:
            print("\033[0:91mData fora do intervalo %s e %s\033[0m"
                  % (min.strftime ("%Y-%m-%d"),
                     max.strftime ("%Y-%m-%d")))
        else:
            break
    return data

def LerData2(msg, min=None, max=None):
    from datetime import datetime
    while True:
        data_texto = input(msg)
        if data_texto == '':
            return None
        try:
            data = datetime.strptime(data_texto, '%Y-%m-%d')
        except ValueError:
            print("\033[0:91mData inválida. Formato AAAA-MM-DD.\033[0m")
            continue
        c=0
        if min == None:
            c = 1
        elif data >= min:
            c = 1
        if max == None:
            c = c + 1
        elif data <= max:
            c = c + 1
        if c != 2:
            print("\033[0:91mData fora do intervalo %s e %s\033[0m"
                  % (min.strftime ("%Y-%m-%d"),
                     max.strftime ("%Y-%m-%d")))
        else:
            break
    return data

# from datetime import datetime
# data_min = datetime.strptime("2019-01-01", '%Y-%m-%d')
# data_max = datetime.strptime("2019-12-31", '%Y-%m-%d')
# data_fundacao = LerData("Data fundação?", data_min, data_max)
#
# agora = datetime.now()
# print (agora)
# print ("Data: ", agora.strftime ("%Y-%m-%d"))
# print ("Hora: ", agora.strftime ("%X"))

# from datetime import datetime
# data_min = datetime.strptime("2019-01-01", '%Y-%m-%d')
# data_max = datetime.strptime("2019-12-31", '%Y-%m-%d')
# data_fundacao = LerData("Data fundação?", data_min, data_max)
#
# agora = datetime.now()
# print (agora)
# print ("Data: ", agora.strftime ("%Y-%m-%d"))
# print ("Hora: ", agora.strftime ("%X"))
