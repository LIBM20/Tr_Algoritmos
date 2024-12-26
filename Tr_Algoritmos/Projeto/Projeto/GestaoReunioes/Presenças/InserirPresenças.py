from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from GestaoPessoas.PesquisaPorID import *
from ValidacaoDados.LerAssunto import *
from ValidacaoDados.LerDeLista import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoPorID import *

def Inserir(dados):
    print("\033[1:4:36mInserir Presenças\033[0m")
    reunioes = LerNumero("ID da Reunião ? ", 1, 9999999)
    pos = PesquisaReuniaoPorID(dados, reunioes)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        id = LerNumero("ID da Pessoa ? ", 170000, 1709999)
        posPessoas = PesquisaPorID(dados, id)
        if posPessoas ==-1:
            print("\033[0:91mPessoa não encontrada\033[0m")
        else:
            pessoa = dados['Pessoas'][posPessoas]['Nome']
            dados['Reunioes'][pos]['Presenças'].append({'Pessoa': pessoa})