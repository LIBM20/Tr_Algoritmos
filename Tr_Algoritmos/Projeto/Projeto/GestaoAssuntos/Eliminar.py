from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from GestaoAssuntos.PesquisaAssuntoPorID import *
def Eliminar(dados):
    print ("\033[1:4:36mEliminar Assuntos\033[0m")

    id = input("ID a alterar ?")
    pos = PesquisaAssuntoPorID(dados, id)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        print(dados['Assuntos'][pos])
        op = LerNumero2("1-Eliminar 2-Cancelar a Eliminação",
                       1,2,"inteiro")
        if op == 1:
           del(dados['Assuntos'][pos])
           print("\033[0:92mRemovido com sucesso\033[0m")
