from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerAssunto import *
from ValidacaoDados.LerData import *
from GestaoReunioes.PesquisaPorID import *
from ValidacaoDados.LerDeLista import *

def Alterar(dados):
    print("\033[1:4:36mAlterar Dados Reunioes\033[0m")
    id = input("ID a alterar ?")
    pos = PesquisaPorID(dados, id)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        id2 = LerNumero2("ID ?", 1, 9999999)
        if str(id) != str(id2):
            for reuniao in dados['Reuniões']:
                if str(reuniao['ID']) == str(id) and str(id) != str(id2):
                    print("\033[0:91mEste id já está a ser ocupado\033[0m")
        local2 = LerAssunto2("Local?")
        data2 = LerData2("Data ?")

        print('\033[0:92mCampos alterados\033[0m')
        if id2 != None:
            print("ID.............:", id2)
            dados['Reunioes'][pos]['ID']=str(id2)
        if local2 != None:
            print("Local...........:", local2)
            dados['Reunioes'][pos]['Local']=local2
        if data2 != None:
            print("Data..........:", data2)
            dados['Reunioes'][pos]['Data']=str(data2)




