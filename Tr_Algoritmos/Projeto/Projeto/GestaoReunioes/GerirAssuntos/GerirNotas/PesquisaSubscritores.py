def PesquisaSubscritores(dados, index_reuniao, index_assunto, index_nota, ID):
    index =0
    for sub in dados['Reunioes'][index_reuniao]['Assuntos'][index_assunto]['Notas'][index_nota]['Subscritores']:
        if str(sub['ID do Subscritor'])==str(ID):
            return index
        index +=1
    return -1