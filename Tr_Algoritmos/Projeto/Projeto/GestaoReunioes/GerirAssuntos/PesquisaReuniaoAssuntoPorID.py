def PesquisaReuniaoAssuntoPorID(dados, index_reuniao, ID):
    index = 0
    for subject in dados['Reunioes'][index_reuniao]['Assuntos']:
        if str(subject['ID']) == str(ID):
            return index
        index += 1
    return -1