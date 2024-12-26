import GestaoPessoas.MenuGestaoPessoas
# from GestaoAssuntos.MenuGestaoAssuntos import *
import GestaoAssuntos.MenuGestaoAssuntos
import GestaoReunioes.MenuGestaoReunioes

# from GestaoReunioes.MenuGestaoReunioes import *
while True:
    print("\033[1:4:36mGestão Reuniões\033[0m")
    print("1 - Pessoas")
    print("2 - Reuniões")
    print("3 - Assunto")
    print("0 - Terminar")
    op = (input("Opção?"))
    if op == '0':
        break
    elif op == '1':
        GestaoPessoas.MenuGestaoPessoas.Menu()
    elif op == '2':
        GestaoReunioes.MenuGestaoReunioes.Menu()
    elif op == '3':
        GestaoAssuntos.MenuGestaoAssuntos.Menu()
    else:
        print("\033[0:91mCaracter inválido!\033:0m")
        print("Insira o número da opção que pertende abrir.")

