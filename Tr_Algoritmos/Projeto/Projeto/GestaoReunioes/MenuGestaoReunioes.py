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
import GestaoReunioes.Pessoas.MenuPessoas
import GestaoReunioes.Presenças.MenuPresenças
import GestaoReunioes.Pesquisa.MenuPesquisa
import GestaoReunioes.Pesquisa
import GestaoReunioes.GerirAssuntos.MenuGestaoReunioesAssuntos

filename_in = 'dados.json'
dados = LerJoson(filename_in)

def Menu():
    while True:
        print ("\033[1:4:36mGestão Reuniões\033[0m")
        print("1 - Inserir")
        print("2 - Alterar")
        print("3 - Eliminar")
        print("4 - Listar convocatória")
        print("5 - Listar ata")
        print("6 - Gerir Assuntos")
        print("7 - Pesquisar por local")
        print("8 - Pessoas(IDs)")
        print("9 - Presenças")
        print("10 - Pesquisa")
        print("0 - Voltar")
        op = (input("Opção?"))
        if op == '0':
            break
        elif op== '1':
            print("Inserir pessoa")
            GestaoReunioes.Inserir.Inserir(dados)
            GravarJSON(filename_in, dados)
        elif op== '2':
            GestaoReunioes.Alterar.Alterar(dados)
            GravarJSON(filename_in, dados)
        elif op== '3':
            GestaoReunioes.Eliminar.Eliminar(dados)
            GravarJSON(filename_in, dados)
        elif op == '4':
            id = LerNumero2("Id da Reuniao?", 1, 9999)
            r = GestaoReunioes.PesquisaPorID.PesquisaPorID(dados, id)
            if r == -1:
                print("\033[0:91mReunião com Id %d não existe"%id)
                print("\033[0m")
            else:
                reuniao = dados["Reunioes"][r]
                id = reuniao['ID']
                local = reuniao['Local']
                data = reuniao['Data']
                hora = reuniao['Hora']
                print ("ID.....:", id)
                print ("Local..:", local)
                print ("Data...:", data)
                print("Hora...:", hora)

                op = LerDeLista("Confirmas?", ["s","n"])
                if op == "s":
                    GestaoReunioes.ListarConvocatoria.ListarConvocatoria(dados, r)

        elif op== '5':
            id = LerNumero("Id da Reuniao?", 1, 9999)
            r = GestaoReunioes.PesquisaPorID.PesquisaPorID(dados, id)
            if r == -1:
                print("\033[0:91mReunião com Id %d não existe"%id)
                print("\033[0m")
            else:
                reuniao = dados["Reunioes"][r]
                id = reuniao['ID']
                local = reuniao['Local']
                data = reuniao['Data']
                print ("ID.....:", id)
                print ("Local..:", local)
                print ("Data...:", data)

                op = LerDeLista("Confirmas?", ["s","n"])
                if op == "s":
                    GestaoReunioes.ListarAta.ListarAta(dados, r)
        elif op == '6':
            GestaoReunioes.GerirAssuntos.MenuGestaoReunioesAssuntos.Menu()
        elif op == '7':
            local = input("Local a procurar (enter para ver todos)!")
            GestaoReunioes.ListarPorNome.ListarPorNome(dados, local)
        elif op == '8':
            GestaoReunioes.Pessoas.MenuPessoas.Menu()
        elif op == '9':
            GestaoReunioes.Presenças.MenuPresenças.Menu()
        elif op=='10':
            GestaoReunioes.Pesquisa.MenuPesquisa.Menu()
        else:
            print("\033[0:91mCaracter inválido!\033:0m")
            print("Insira o número da opção que pertende abrir.")