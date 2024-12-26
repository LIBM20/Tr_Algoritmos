from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerAssunto import *
from ValidacaoDados.LerEmail import *
from GestaoAssuntos.PesquisaAssuntoPorID import *
from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerAssunto import *
from ValidacaoDados.LerData import *
from ValidacaoDados.LerDeLista import *
def Alterar(dados):
    id = input("ID a alterar ?")
    pos = PesquisaAssuntoPorID(dados, id)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        assunto2 = LerAssunto2("Assunto ?")
        data2= LerData("Data (YYYY-MM-DD)? ")
        datalimite2 = LerData("Data Limite (YYYY-MM-DD)? ")
        prioridade2 = LerNumero2("Prioridade (1-Muito Urgente, "
                                   "2-Urgente, "
                                   "3-Pouco Urgente) ?", 1, 3)
        estado2 = LerAssunto("Estado do Assunto (Concluido, Por Tratar, Adiado) ? ")
        print('\033[0:92mCampos alterados\033[0m')
        if id != None:
            print("ID.............:", id)
            dados['Assuntos'][pos]['ID']=str(id)
        if assunto2 != None:
            print("Assunto...........:", assunto2)
            dados['Assuntos'][pos]['Assunto']=assunto2
        if data2 != None:
            print("Data..........:", data2)
            dados['Assuntos'][pos]['Tarefas']=str(data2)
        if datalimite2 != None:
            print("Data Limite......:", datalimite2)
            dados['Assuntos'][pos]['Data Limite']=str(datalimite2)
        if prioridade2 != None:
            print("Prioridade......:", prioridade2)
            dados['Assuntos'][pos]['Prioridade'] = prioridade2
        if estado2 != None:
            print("Estado......:", estado2)
            dados['Assuntos'][pos]['Estado'] = estado2