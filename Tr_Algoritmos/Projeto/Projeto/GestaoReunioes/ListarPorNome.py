def ListarPorNome(dados, assunto_procurar):
    print("{0:8s}{1:<50s}{2:<20s}".format("ID","Local","Data"))
    for x in dados['Reunioes']:
        if x['Local'].find(assunto_procurar) >= 0:
            # print(pessoa)
            print("{0:8s}{1:<50s}{2:<20s}".
                  format(str(x["ID"]), x["Local"],
                         str(x["Data"]),))
