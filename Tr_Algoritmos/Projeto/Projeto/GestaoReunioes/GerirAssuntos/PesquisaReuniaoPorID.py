def PesquisaReuniaoPorID(dados, ID):
    for i in range(len(dados['Reunioes'])):
        x = dados['Reunioes'][i]
        if str(x['ID']) ==  str(ID):
            return i
    return -1

def PesquisaReuniaoPorID2(dados, ID):
    index = 0
    for meeting in dados['Reunioes']:
        if str(meeting['ID']) == str(ID):
            return index
        index += 1
    return -1