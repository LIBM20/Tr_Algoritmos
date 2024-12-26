from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoPorID import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoAssuntoPorID import *
from GestaoReunioes.GerirAssuntos.GerirNotas.PesquisaReuniaoAssuntoNotasPorID import *

def Eliminar(dados):
    print ("\033[1:4:36mEliminar Nota do Assunto da Reunião\033[0m")

    reuniao = input("ID da Reunião? ")
    pos = PesquisaReuniaoPorID(dados, reuniao)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        assunto = input("ID do Assunto? ")
        pos1 = PesquisaReuniaoAssuntoPorID(dados,pos, assunto)
        if pos1 == -1:
            print("\033[0:91mNão encontrado\033[0m")
        else:
            nota = input("ID da Nota? ")    
            pos2 = PesquisaReuniaoAssuntoNotasPorID(dados,pos,pos1, nota)
            if pos2 == -1:
                print("\033[0:91mNão encontrado\033[0m")
            else:
                print(dados['Reunioes'][pos]['Assuntos'][pos1]['Notas'][pos2])
                op = LerNumero("1-Eliminar? 2-Cancelar a Eliminação",1,2,"inteiro")
                if op == 1:
                    del(dados['Reunioes'][pos]['Assuntos'][pos1]['Notas'][pos2])
                    print("\033[0:92mRemovido com sucesso\033[0m")