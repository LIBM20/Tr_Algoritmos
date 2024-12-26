import GestaoReunioes.ListarPorNome
from Lergravardados.Lergravardados import *
import GestaoReunioes.Inserir
import GestaoReunioes.ListarConvocatoria
import GestaoReunioes.ListarAta
import GestaoReunioes.Eliminar
import GestaoReunioes.Alterar
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerDeLista import *
import GestaoReunioes.PesquisaPorID
import GestaoReunioes.Presenças
import GestaoReunioes.Presenças.InserirPresenças
import GestaoReunioes.Presenças.EliminarPresenças
import GestaoReunioes.GerirAssuntos.MenuGestaoReunioesAssuntos

filename_in = 'dados.json'
dados = LerJoson(filename_in)

def Menu():
    while True:
        print ("\033[1:4:36mPessoas\033[0m")
        print("1 - Inserir")
        print("2 - Eliminar")
        print("0 - Voltar")
        op = (input("Opção?"))
        if op == '0':
            break
        elif op== '1':
            GestaoReunioes.Presenças.InserirPresenças.Inserir(dados)
            GravarJSON(filename_in, dados)
        elif op== '2':
            GestaoReunioes.Presenças.EliminarPresenças.Eliminar(dados)
            GravarJSON(filename_in, dados)
        else:
            print("\033[0:91mCaracter inválido!")
            print("Insira o número da opção que pretende abrir.")