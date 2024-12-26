import GestaoReunioes.GerirAssuntos.GerirTarefas.Inserir
import GestaoReunioes.GerirAssuntos.GerirTarefas.Eliminar
import GestaoReunioes.GerirAssuntos.GerirTarefas.InserirPessoas
import GestaoReunioes.GerirAssuntos.GerirTarefas.EliminarPessoas
#from GestaoReunioes.GerirAssuntos.GerirTarefas.Inserir import *
from Lergravardados.Lergravardados import *

filename_in = 'dados.json'
dados = LerJoson(filename_in)

def Menu():
    print ("\033[1:4:36mGerir Tarefas\033[0m")
    print("1 - Inserir")
    print("2 - Eliminar")
    print("3 - Inserir Pessoas(ID)")
    print("4 - Eliminar Pessoas(ID)")
    print("0 - Voltar")
    op = input("Opção?")
    if op == '1':
        GestaoReunioes.GerirAssuntos.GerirTarefas.Inserir.Inserir(dados)
        GravarJSON(filename_in, dados)
    elif op == '2':
        GestaoReunioes.GerirAssuntos.GerirTarefas.Eliminar.Eliminar(dados)
        GravarJSON(filename_in, dados)
    elif op == '3':
        GestaoReunioes.GerirAssuntos.GerirTarefas.InserirPessoas.Inserir(dados)
    elif op == '4':
        GestaoReunioes.GerirAssuntos.GerirTarefas.EliminarPessoas.Eliminar(dados)
    elif op == '0':
        pass
    else:
        print("\033[0:91mCaracter inválido!\033[0m")
        print("Insira o número da opção que pretende abrir.")
