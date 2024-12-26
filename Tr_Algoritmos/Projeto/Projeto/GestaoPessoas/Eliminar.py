from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from GestaoPessoas.PesquisaPorID import *

def Eliminar(dados):
    print("\033[1:4:36mEliminar Dados\033[0m")

    id = input("ID a alterar? ")
    pos = PesquisaPorID(dados, id)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        print(dados['Pessoas'][pos])
        op = LerNumero2("1-Eliminar? 2-Cancelar a Eliminação",
                       1, 2, "inteiro")
        if op == 1:
            del(dados['Pessoas'][pos])
            print("\033[0:92mRemovido com sucesso\033[0m")
