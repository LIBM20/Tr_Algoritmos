def ListarPorNome(dados, nome_procurar):
    # {'ID': '1', 'Nome': '111', 'EMail': '111', 'Telemóvel': '111', 'Departamento': '111', 'Data Nascimento': '111', 'Titulo': '11'}
    print("{0:8s}{1:<30s}{2:<20s}{3:10s}".format("ID","Nome","Email","Telemóvel"))
    for pessoa in dados['Pessoas']:
        if pessoa['Nome'].find(nome_procurar) >= 0:
            # print(pessoa)
            print("{0:8s}{1:<30s}{2:<20s}{3:10s}".
                  format(str(pessoa["ID"]), pessoa["Nome"],
                         pessoa["EMail"], str(pessoa["Telemóvel"])))
