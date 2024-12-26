from Lergravardados.Lergravardados import *
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerDeLista import *
import GestaoReunioes.Pesquisa.ListarPesquisa
#import GestaoReunioes.Pesquisa.ListarPesquisa.ListarData
filename_in = 'dados.json'
dados = LerJoson(filename_in)
#print(dados)
import GestaoReunioes.GerirAssuntos.MenuGestaoReunioesAssuntos
def Menu():
    while True:
        print ("\033[1:4:36mPesquisa Por\033[0m")
        print("1 - Assunto")
        print("2 - Data")
        print("3 - Nota")
        print("4 - Pessoa")
        print("5 - Tarefa")
        print("6 - Presenças")
        print("0 - Voltar")
        op = (input("Opção?"))
        if op == '0':
            break
        elif op== '1':
            print("\033[1:4:36mPesquisa por Assunto\033[0m")
            assunto_procurar = input("Assunto (enter para ver todos)?")
            GestaoReunioes.Pesquisa.ListarPesquisa.ListarAssunto(dados,assunto_procurar)
            GravarJSON(filename_in, dados)
        elif op== '2':
            print("\033[1:4:36mPesquisa por Data\033[0m")
            data_procurar = input("Data (enter para ver todos)?")
            GestaoReunioes.Pesquisa.ListarPesquisa.ListarData(dados,data_procurar)
            GravarJSON(filename_in, dados)
        elif op== '3':
            print("\033[1:4:36mPesquisa por Nota\033[0m")
            nota_procurar = input("Nota (enter para ver todos)?")
            GestaoReunioes.Pesquisa.ListarPesquisa.ListarData(dados, nota_procurar)
            GravarJSON(filename_in, dados)
        elif op == '4':
            print("\033[1:4:36mPesquisa por Pessoa\033[0m")
            pessoa_procurar = input("Pessoa (enter para ver todos)?")
            GestaoReunioes.Pesquisa.ListarPesquisa.ListarPessoa(dados, pessoa_procurar)
            GravarJSON(filename_in, dados)
        elif op == '5':
            print("\033[1:4:36mPesquisa por Tarefa\033[0m")
            tarefa_procurar = input("Tarefa (enter para ver todos)?")
            GestaoReunioes.Pesquisa.ListarPesquisa.ListarTarefa(dados, tarefa_procurar)
            GravarJSON(filename_in, dados)
        elif op == '6':
            print("\033[1:4:36mPesquisa por Presenças\033[0m")
            presenca_procurar = input("Presença (enter para ver todos)?")
            GestaoReunioes.Pesquisa.ListarPesquisa.ListarPresenca(dados, presenca_procurar)
            GravarJSON(filename_in, dados)