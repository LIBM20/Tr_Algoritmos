def ListarPorNome(dados, assunto_procurar):
    print("{0:8s}{1:33s}{2:<20s}{3:20s}{4:20s}{5:15s}".format("ID", "Assunto", "Data", "Data Limite", "Prioridade", "Estado"))
    for subject in dados['Assuntos']:
        if subject['Estado'].find(assunto_procurar) >= 0:
            print("{0:8s}{1:30s}{2:19s}{3:28s}{4:15s}{5:15s}".
                  format(str(subject["ID"]), str(subject["Assunto"]),
                         str(subject["Data"]), str(subject["Data Limite"]), str(subject["Prioridade"]), str(subject["Estado"])))