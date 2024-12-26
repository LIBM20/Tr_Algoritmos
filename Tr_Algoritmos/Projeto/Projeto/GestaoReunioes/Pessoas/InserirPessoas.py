from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from GestaoPessoas.PesquisaPorID import *
from ValidacaoDados.LerAssunto import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoPorID import *

def Inserir(dados):
    print("\033[1:4:36mInserir Pessoas\033[0m")
    reunioes = LerNumero("ID da Reunião ? ", 1, 9999999)
    pos = PesquisaReuniaoPorID(dados, reunioes)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        id = LerNumero("ID da Pessoa? ", 170000, 1709999)
        posPessoas = PesquisaPorID(dados, id)
        if posPessoas ==-1:
            op = LerDeLista("Deseja adicionar uma pessoa não pertencente?", ["s", "n"])
            if op == 's':
                pessoa = dados['Pessoas'][posPessoas]['Nome']
                dados['Reunioes'].append({'Id da Pessoa': id, 'Pessoas': pessoa})
        else:
            pessoa = dados['Pessoas'][posPessoas]['Nome']
            dados['Reunioes'][pos]['Pessoas'].append({'ID da Pessoa': id,'Pessoa': pessoa})