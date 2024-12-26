def PesquisaPorID(dados, ID):
    for i in range(len(dados['Reunioes'])):
        r = dados['Reunioes'][i]
        if str(r['ID']) == str(ID):
            return i
    return -1
