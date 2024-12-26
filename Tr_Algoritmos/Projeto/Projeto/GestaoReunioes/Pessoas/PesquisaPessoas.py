def PesquisaPessoas(dados, index_reuniao, ID):
    index =0
    for pessoa in dados['Reunioes'][index_reuniao]['Pessoas']:
        if str(pessoa['ID da Pessoa'])==str(ID):
            return index
        index +=1
    return -1