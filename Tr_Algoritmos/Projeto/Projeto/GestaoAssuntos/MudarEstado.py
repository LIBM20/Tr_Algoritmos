from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerAssunto import *
from GestaoAssuntos.PesquisaAssuntoPorID import *

def MudarEstado(dados):
    print("\033[1:4:36mMudar Estado do Assunto\033[0m")
    id = input("ID do Assunto a alterar ?")
    pos = PesquisaAssuntoPorID(dados, id)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        estado2 = LerAssunto2("Estado do Assunto ? ")
        print('\033[0:92mCampos alterados\033[0m')
        if estado2 != None:
            print("Estado............: ", estado2)
            dados['Assuntos'][pos]['Estado'] = estado2
            