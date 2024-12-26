import GestaoReunioes.GerirAssuntos.GerirNotas.MenuGestaoReunioesNotas
import GestaoReunioes.GerirAssuntos.GerirTarefas.MenuGestaoReunioesTarefas
import GestaoReunioes.GerirAssuntos.Inserir
import GestaoReunioes.GerirAssuntos.Eliminar
from Lergravardados.Lergravardados import *

filename_in = 'dados.json'
dados = LerJoson(filename_in)
print(dados)

def Menu():
    while True:
        print ("\033[1:4:36mGestão Assunto\033[0m")
        print("1 - Inserir")
        print("2 - Eliminar")
        print("3 - Gerir Notas")
        print("4 - Gerir Tarefas")
        print("0 - Voltar")
        op = input("Opção?")
        if op == '0':
            break
        elif op=='1':
            GestaoReunioes.GerirAssuntos.Inserir.Inserir(dados)
            GravarJSON(filename_in, dados)
        elif op =='2':
            GestaoReunioes.GerirAssuntos.Eliminar.Eliminar(dados)
            GravarJSON(filename_in, dados)
        elif op =='3':
            GestaoReunioes.GerirAssuntos.GerirNotas.MenuGestaoReunioesNotas.Menu()
        elif op =='4':
            GestaoReunioes.GerirAssuntos.GerirTarefas.MenuGestaoReunioesTarefas.Menu()
        else:
            print("\033[0:91mCaracter inválido!\033[0m")
            print("Insira o número da opção que pretende abrir.")

