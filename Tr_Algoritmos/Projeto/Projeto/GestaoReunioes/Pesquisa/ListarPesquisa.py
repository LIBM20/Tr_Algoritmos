def ListarAssunto(dados, assunto_procurar):
    print("{0:8s}{1:15s}{2:10s}{3:15s}".format("ID","Local","Data","Hora"))
    for assunto in dados['Reunioes']:
        if str(assunto['Assuntos']).find(assunto_procurar) >= 0:
            print("{0:0}{1:7s}{2:12s}{3:12s}{4:7s}".
                  format(assunto["ID"],(" ") ,str(assunto["Local"]),
                         str(assunto["Data"]), str(assunto["Hora"])))

def ListarData(dados, data_procurar):
    print("{0:8s}{1:15s}{2:10s}{3:15s}".format("ID","Local","Data","Hora"))
    for data in dados['Reunioes']:
        if data['Data'].find(data_procurar) >= 0:
            print("{0:0}{1:7s}{2:12s}{3:12s}{4:7s}".
                  format(data["ID"],(" ") ,str(data["Local"]),
                         str(data["Data"]), str(data["Hora"])))

def ListarNotas(dados, nota_procurar):
    print("{0:8s}{1:15s}{2:10s}{3:15s}".format("ID","Local","Data","Hora"))
    for i in dados['Reunioes']:
        for nota in dados['Reunioes'][i]['Assuntos']:
            if nota['Notas'].find(nota_procurar) >= 0:
                print("{0:0}{1:7s}{2:12s}{3:12s}{4:7s}".format(nota["ID"],(" ") ,str(nota["Local"]),str(nota["Data"]), str(nota["Hora"])))

def ListarPessoa(dados, pessoa_procurar):
    print("{0:8s}{1:15s}{2:10s}{3:15s}".format("ID","Local","Data","Hora"))
    for pessoa in dados['Reunioes']:
        if str(pessoa['Pessoas']).find(pessoa_procurar) >= 0:
            print("{0:0}{1:7s}{2:12s}{3:12s}{4:7s}".format(pessoa["ID"],(" ") ,str(pessoa["Local"]),str(pessoa["Data"]), str(pessoa["Hora"])))

def ListarTarefa(dados, tarefa_procurar):
    print("{0:8s}{1:15s}{2:10s}{3:15s}".format("ID","Local","Data","Hora"))
    for i in dados['Reunioes']:
        for tarefa in dados['Reunioes'][i]['Assuntos']:
            if tarefa['Tarefas'].find(tarefa_procurar) >= 0:
                print("{0:0}{1:7s}{2:12s}{3:12s}{4:7s}".format(tarefa["ID"],(" ") ,str(tarefa["Local"]),str(tarefa["Data"]), str(tarefa["Hora"])))

def ListarPresenca(dados, presenca_procurar):
    print("{0:8s}{1:15s}{2:10s}{3:15s}".format("ID","Local","Data","Hora"))
    for presenca in dados['Reunioes']:
        if str(presenca['Presenças']).find(presenca_procurar) >= 0:
            print("{0:0}{1:7s}{2:12s}{3:12s}{4:7s}".format(presenca["ID"],(" ") ,str(presenca["Local"]),str(presenca["Data"]), str(presenca["Hora"])))
