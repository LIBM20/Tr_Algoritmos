from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from GestaoPessoas.PesquisaPorID import *
from GestaoReunioes.PesquisaPorID import *
from GestaoReunioes.Pessoas.PesquisaPessoas import *
def Eliminar(dados):
    print ("\033[1:4:36mEliminar Pessoa da Reunião\033[0m")

    reuniao = input("ID da Reunião ?")
    pos = PesquisaPorID(dados, reuniao)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        pessoa = LerNumero2("Id da Pessoa ? ", 1700000, 1709999)
        pos1 = PesquisaPessoas(dados, pos, pessoa)
        if pos1 == -1:
            print("\033[0:91mNão encontrado\033[0m")
        else:
            print(dados['Reunioes'][pos]['Pessoas'][pos1])
            op = LerNumero("1-Eliminar? 2-Cancelar a Eliminação", 1, 2, "inteiro")
            if op == 1:
                del (dados['Reunioes'][pos]['Pessoas'][pos1])
                print("\033[0:92mRemovido com sucesso\033[0m")