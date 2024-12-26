from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from GestaoPessoas.PesquisaPorID import *
from ValidacaoDados.LerAssunto import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoPorID import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoAssuntoPorID import *
from GestaoReunioes.GerirAssuntos.GerirNotas.PesquisaReuniaoAssuntoNotasPorID import *

def Inserir(dados):
    print("\033[1:4:36mInserir Subscritores\033[0m")
    reunioes = LerNumero("ID da Reunião ? ", 1, 9999999)
    pos = PesquisaReuniaoPorID(dados, reunioes)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        assuntos = LerNumero("ID do Assunto ? ", 1, 9999999)
        pos1 = PesquisaReuniaoAssuntoPorID(dados,pos,assuntos)
        if pos1 == -1:
            print("\033[0:91mNão encontrado\033[0m")
        else:
            nota = LerNumero("ID da Nota ? ", 1, 9999999)
            pos2 = PesquisaReuniaoAssuntoNotasPorID(dados,pos,pos1, nota)
            if pos2 == -1:
                print("\033[0:91mNão encontrado\033[0m")
            else:
                id = LerNumero("ID do Subscritor ? ",170000, 1709999)
                posSub = PesquisaPorID(dados,id)
                if posSub == -1:
                    print("\033[0:91mNão encontrado\033[0m")
                else:
                    sub = dados['Pessoas'][posSub]['Nome']
                    dados['Reunioes'][pos]['Assuntos'][pos1]['Notas'][pos2]['Subscritores'].append({'ID do Subscritor': id,'Subscritor': sub})