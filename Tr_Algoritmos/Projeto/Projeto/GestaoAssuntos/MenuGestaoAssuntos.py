import GestaoAssuntos.ListarPorNome
from Lergravardados.Lergravardados import *
import GestaoAssuntos.Inserir
import GestaoAssuntos.Alterar
import GestaoAssuntos.Eliminar
import GestaoAssuntos.MudarEstado
import GestaoAssuntos.ContarAssuntosPorEstado

filename_in = 'dados.json'
dados = LerJoson(filename_in)
print(dados)

def Menu():
    while True:
        print ("\033[1:4:36mGestão Assuntos\033[0m")
        print("1 - Inserir")
        print("2 - Alterar")
        print("3 - Eliminar")
        print("4 - Mudar Estado")
        print("5 - Lista Concluídos")
        print("6 - Lista Por tratar")
        print("7 - Lista Adiados")
        print("8 - Listagem de Assuntos por Estado")
        print("0 - Voltar")
        op = (input("Opção?"))
        if op== '0':
            break
        elif op== '1':
            GestaoAssuntos.Inserir.Inserir(dados)
            GravarJSON(filename_in, dados)
        elif op == '2':
            print("\033[1:4:36mAlterar Assunto\033[0m")
            GestaoAssuntos.Alterar.Alterar(dados)
            GravarJSON(filename_in, dados)            
        elif op== '3':
            GestaoAssuntos.Eliminar.Eliminar(dados)
            GravarJSON(filename_in, dados)           
        elif op== '4':
            GestaoAssuntos.MudarEstado.MudarEstado(dados)
            GravarJSON(filename_in, dados)
        elif op== '5':
            print("\033[1:4:36mLista Assuntos Concluídos\033[0m")
            GestaoAssuntos.ListarPorNome.ListarPorNome(dados, "Concluido")
        elif op== '6':
            print("\033[1:4:36mLista Assuntos Por Tratar\033[0m")
            GestaoAssuntos.ListarPorNome.ListarPorNome(dados, "Por tratar")           
        elif op== '7':
            print("\033[1:4:36mLista Assuntos Adiados\033[0m")
            GestaoAssuntos.ListarPorNome.ListarPorNome(dados, "Adiado")
        elif op== '8':
            print("\033[1:4:36mTabela de Assuntos por Estado\033[0m")
            GestaoAssuntos.ContarAssuntosPorEstado.ContarAssuntosPorEstado(dados)
        else:
            print("\033[0:91mCaracter inválido!")
            print("Insira o número da opção que pretende abrir.")

