from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from GestaoReunioes.PesquisaPorID import *
def Eliminar(dados):
    print ("\033[1:4:36mEliminar Reniões\033[0m")

    id = input("ID a eliminar ?")
    pos = PesquisaPorID(dados, id)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        print(dados['Reunioes'][pos])
        op = LerNumero2("1-Eliminar? 2-Cancelar a Eliminação",
                       1,2,"inteiro")
        if op == 1:
            del(dados['Reunioes'][pos])
            print("\033[0:92mRemovido com sucesso\033[0m")
