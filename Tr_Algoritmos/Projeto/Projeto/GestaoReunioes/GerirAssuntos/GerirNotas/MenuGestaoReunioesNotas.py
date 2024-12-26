import GestaoReunioes.GerirAssuntos.GerirNotas.Inserir
import GestaoReunioes.GerirAssuntos.GerirNotas.Eliminar
#from GestaoReunioes.GerirAssuntos.GerirNotas.Inserir import *
import GestaoReunioes.GerirAssuntos.GerirNotas.InserirSubscritores
import GestaoReunioes.GerirAssuntos.GerirNotas.EliminarSubscritores
from Lergravardados.Lergravardados import *

filename_in = 'dados.json'
dados = LerJoson(filename_in)

def Menu():
    print ("\033[1:4:36mGerir Notas\033[0m")
    print("1 - Inserir")
    print("2 - Eliminar")
    print("3 - Inserir Subscritores(ID)")
    print("4 - Eliminar Subscritores(ID)")
    print("0 - Voltar")
    op = input("Opção?")
    if op== '1':
        GestaoReunioes.GerirAssuntos.GerirNotas.Inserir.Inserir(dados)
        GravarJSON(filename_in, dados)
    elif op == '2':
        GestaoReunioes.GerirAssuntos.GerirNotas.Eliminar.Eliminar(dados)
        GravarJSON(filename_in, dados)
    elif op == '3':
        GestaoReunioes.GerirAssuntos.GerirNotas.InserirSubscritores.Inserir(dados)
        GravarJSON(filename_in, dados)
    elif op == '4' :
        GestaoReunioes.GerirAssuntos.GerirNotas.EliminarSubscritores.Eliminar(dados)
        GravarJSON(filename_in, dados)
    elif op == '0' :
        pass
    else:
        print("\033[0:91mCaracter inválido!\033[0m")
        print("Insira o número da opção que pertende abrir.")