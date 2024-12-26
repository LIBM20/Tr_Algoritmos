
def ListarPorDepartamentos(dados, departamento):
    print("{0:8s}{1:<30s}{2:<20s}{3:10s}".format("ID","Nome","Email","Telemóvel"))
    for pessoa in dados['Pessoas']:
        if pessoa['Departamento'] == departamento:
            # print(pessoa)
            print("{0:8s}{1:<30s}{2:<20s}{3:10s}".
                  format(pessoa["ID"], pessoa["Nome"],
                         pessoa["EMail"], pessoa["Telemóvel"]))
