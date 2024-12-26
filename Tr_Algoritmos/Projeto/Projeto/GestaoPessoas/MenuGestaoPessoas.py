from Lergravardados.Lergravardados import *
import GestaoPessoas.ListarPorNome
import GestaoPessoas.Inserir
import GestaoPessoas.Alterar
import GestaoPessoas.Eliminar
import GestaoPessoas.ListarPorDepartamentos
import GestaoPessoas.DepartamentosContarAgrupar

filename_in = 'dados.json'
dados = LerJoson(filename_in)

def Menu():
    while True:
        print ("\033[1:4:36mGestão Pessoas\033[0m")
        print("1 - Inserir")
        print("2 - Alterar")
        print("3 - Eliminar")
        print("4 - Pesquisa por nome")
        print("5 - Pesquisa por departamento")
        print("6 - Departamentos")
        print("0 - Voltar")
        op = (input("Opção?"))
        if op == '0':
            break
        elif op == '2':
            GestaoPessoas.Alterar.Alterar(dados)
            GravarJSON(filename_in, dados)
        elif op == '3':
            GestaoPessoas.Eliminar.Eliminar(dados)
            GravarJSON(filename_in, dados)
        elif op == '4':
            nome_procurar =  input("Nome (enter para ver todos)?")
            GestaoPessoas.ListarPorNome.ListarPorNome(dados, nome_procurar)
        elif op == '5':
            departamento = input("Qual o Departamento?")
            GestaoPessoas.ListarPorDepartamentos.ListarPorDepartamentos(dados, departamento)
        elif op == '6':
            GestaoPessoas.DepartamentosContarAgrupar.DepartamentosContar(dados)
        elif op == '1':
            GestaoPessoas.Inserir.Inserir(dados)
            GravarJSON(filename_in, dados)
        else:
            print("\033[0:91mCaracter inválido!\033:0m")
            print("Insira o número da opção que pertende abrir.")
