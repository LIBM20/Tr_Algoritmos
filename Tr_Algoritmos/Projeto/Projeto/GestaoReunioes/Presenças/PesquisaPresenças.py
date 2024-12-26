def PesquisaPresenças(dados, index_reuniao, ID):
    index =0
    for presença in dados['Reunioes'][index_reuniao]['Presenças']:
        if str(presença['Pessoa'])==str(ID):
            return index
        index +=1
    return -1