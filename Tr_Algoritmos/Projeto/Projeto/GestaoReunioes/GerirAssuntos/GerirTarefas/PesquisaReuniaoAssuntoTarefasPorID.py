def PesquisaReuniaoAssuntoTarefasPorID(dados, index_reuniao, index_assunto,  ID):
    index = 0
    for task in dados['Reunioes'][index_reuniao]['Assuntos'][index_assunto]['Tarefas']:
        if str(task['ID']) == str(ID):
            return index
        index += 1
    return -1