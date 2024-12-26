from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerNome import *
from GestaoPessoas.PesquisaPorID import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoPorID import *
from GestaoReunioes.Presenças.PesquisaPresenças import *
def Eliminar(dados):
    print ("\033[1:4:36mEliminar Presença da Reunião\033[0m")

    reuniao = input("ID da Reunião ?")
    pos = PesquisaReuniaoPorID(dados, reuniao)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        pessoa = LerNome("Pessoa (nome)? ")
        pos1 = PesquisaPresenças(dados, pos, pessoa)
        if pos1 == -1:
            print("\033[0:91mNão encontrado\033[0m")
        else:
            print(dados['Reunioes'][pos]['Presenças'])
            op = LerNumero("1-Eliminar? 2-Cancelar a Eliminação", 1, 2, "inteiro")
            if op == 1:
                del (dados['Reunioes'][pos]['Presenças'][pos1])
                print("\033[0:92mRemovido com sucesso\033[0m")