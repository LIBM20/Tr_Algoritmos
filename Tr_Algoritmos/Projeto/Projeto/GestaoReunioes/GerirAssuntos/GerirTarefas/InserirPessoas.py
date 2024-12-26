from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from GestaoPessoas.PesquisaPorID import *
from ValidacaoDados.LerAssunto import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoPorID import *
from GestaoReunioes.GerirAssuntos.PesquisaReuniaoAssuntoPorID import *
from GestaoReunioes.GerirAssuntos.GerirTarefas.PesquisaReuniaoAssuntoTarefasPorID import *

def Inserir(dados):
    print("\033[1:4:36mInserir Pessoas(ID) em Tarefa\033[0m")
    reunioes = LerNumero("ID da Reunião ? ", 1, 9999999)
    pos = PesquisaReuniaoPorID(dados, reunioes)
    if pos == -1:
        print("\033[0.91mNão encontrado\033[0m")
    else:
        assuntos = LerNumero("ID do Assunto ? ", 1, 9999999)
        pos1 = PesquisaReuniaoAssuntoPorID(dados,pos,assuntos)
        if pos1 == -1:
            print("\033[0:91mNão encontrado\033[0m")
        else:
            nota = LerNumero("ID da Tarefa ? ", 1, 9999999)
            pos2 = PesquisaReuniaoAssuntoTarefasPorID(dados,pos,pos1, nota)
            if pos2 == -1:
                print("\033[0:91mNão encontrado\033[0m")
            else:
                id = LerNumero("ID da Pessoa ? ",170000, 1709999)
                posPes = PesquisaPorID(dados,id)
                if posPes == -1:
                    print("\033[0:91mNão encontrado\033[0m")
                else:
                    pessoa = dados['Pessoas'][posPes]['Nome']
                    dados['Reunioes'][pos]['Assuntos'][pos1]['Tarefas'][pos2]['Pessoas(ID)'].append({'ID da Pessoa': id,'Pessoa': pessoa})
                    print("\033[0:92mAdicionada com sucesso\033[0m")