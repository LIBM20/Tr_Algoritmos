from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerAssunto import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoPorID import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoAssuntoPorID import *

def Inserir(dados):
    val=1
    print("\033[1:4:36mInserir Tarefa em Assuntos de Reuniao\033[0m")
    while True:
        reunioes = LerNumero2("ID da Reunião ? ", 1, 9999999)
        if reunioes == None:
            return
        pos = PesquisaReuniaoPorID(dados, reunioes)
        if pos != -1:
            break
    while True:
        assuntos = LerNumero2("ID do Assunto ? ", 1, 9999999)
        if assuntos == None:
            return
        pos1 = PesquisaReuniaoAssuntoPorID(dados,pos, assuntos)
        if pos1 != -1:
            break
    id = LerNumero2("ID ?", 1, 9999999)
    for tarefas in dados['Reunioes'][pos]['Assuntos'][pos1]['Tarefas']:
        if str(tarefas['ID']) == str(id):
            val = 0
            print("\033[0:91mEste id já está a ser ocupado\033[0m")
    if val == 1:
        tarefa = LerAssunto("Tarefa ? ")
        dados['Reunioes'][pos]['Assuntos'][pos1]['Tarefas'].append({'ID': id,'Tarefas': tarefa,'Pessoas(ID)':[]})