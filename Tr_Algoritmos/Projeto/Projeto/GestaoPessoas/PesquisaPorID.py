def PesquisaPorID(dados, ID):
    for i in range(len(dados['Pessoas'])):
        pessoa = dados['Pessoas'][i]
        if str(pessoa['ID']) == str(ID):
            return i
    return -1