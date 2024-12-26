def PesquisaAssuntoPorID(dados, ID):
    for i in range(len(dados['Assuntos'])):
        x = dados['Assuntos'][i]
        if str(x['ID']) ==  str(ID):
            return i
    return -1
