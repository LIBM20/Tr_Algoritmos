from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerAssunto import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoPorID import *
def Inserir(dados):
    val = 1
    print("\033[1:4:36mInserir Assunto em reuniao\033[0m")
    reunioes = LerNumero("ID da Reunião ?", 1, 9999999)
    pos = PesquisaReuniaoPorID(dados, reunioes)
    if pos == -1:
        print("\033[0:91mReunião não encontrada\033[0m")
    else:
        id = LerNumero("ID ?", 1, 9999999)
        for reunioes in dados['Reunioes'][pos]['Assuntos']:
            if str(reunioes['ID']) == str(id):
                val = 0
                print("\033[0:91mEste id já está a ser ocupado\033[0m")
        if val == 1:
            assunto = LerAssunto("Assunto ?")
            dados['Reunioes'][pos]['Assuntos'].append({'ID': id,'Assunto':assunto,'Notas': [],'Tarefas': []})