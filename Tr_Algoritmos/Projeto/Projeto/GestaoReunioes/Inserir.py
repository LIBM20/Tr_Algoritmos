from ValidacaoDados.LerAssunto import *
from ValidacaoDados.LerData import *
from ValidacaoDados.LerNumero import *

def Inserir(dados):
    val = 1
    print("\033[1:4:36mInserir Reunião\033[0m")
    id = LerNumero2("ID ? ", 1, 9999999)
    for reunioes in dados['Reunioes']:
        if str(reunioes['ID']) == str(id):
            val = 0
            print("\033[0:91mEste id já está a ser ocupado\033[0m")
    if val==1:
        local = LerAssunto("Local? ")
        data = LerData("Data (YYYY-MM-DD)? ")
        hora = input("Insira hora (HH:MM): ")
        dados['Reunioes'].append({'ID': id,
                                  'Local': local,
                                  'Data': data.strftime("%Y-%m-%d"),
                                  'Hora': hora,
                                  'Assuntos': [],
                                  'Pessoas': [],
                                  'Presenças':[]})
