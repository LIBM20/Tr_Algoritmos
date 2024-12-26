from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoPorID import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoAssuntoPorID import *
def Eliminar(dados):
    print ("\033[1:4:36mEliminar Assunto da Reunião\033[0m")

    reuniao = input("ID da Reunião ?")
    pos = PesquisaReuniaoPorID(dados, reuniao)
    assunto = input("ID do Assunto ?")
    pos2 = PesquisaReuniaoAssuntoPorID(dados, pos, assunto)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        print(dados['Reunioes'][pos]['Assuntos'][pos2])
        op = LerNumero("1-Eliminar? 2-Cancelar a Eliminação",
                       1,2,"inteiro")
        if op == 1:
            del(dados['Reunioes'][pos]['Assuntos'][pos2])
            print("\033[0:92mRemovido com sucesso\033[0m")