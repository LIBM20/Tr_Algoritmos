def PesquisaReuniaoAssuntoNotasPorID(dados, index_reuniao, index_assunto,  ID):
    index =0
    for note in dados['Reunioes'][index_reuniao]['Assuntos'][index_assunto]['Notas']:
        if str(note['ID'])==str(ID):
            return index
        index +=1
    return -1