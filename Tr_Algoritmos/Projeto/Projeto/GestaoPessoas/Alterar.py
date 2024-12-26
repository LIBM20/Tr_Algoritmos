from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerNome import *
from ValidacaoDados.LerEmail import *
from ValidacaoDados.LerData import *
from ValidacaoDados.LerDeLista import *
from ValidacaoDados.LerTelemovel import *
from GestaoPessoas.PesquisaPorID import *
from datetime import datetime
def Alterar(dados):
    id = input("ID a alterar ?")
    pos = PesquisaPorID(dados, id)
    if pos == -1:
        print("\033[0:91mNão encontrado\033[0m")
    else:
        id=dados['Pessoas'][pos]['ID']
        nome=dados['Pessoas'][pos]['Nome']
        eMail=dados['Pessoas'][pos]['EMail']
        telemovel=dados['Pessoas'][pos]['Telemóvel']
        data_nascimento=dados['Pessoas'][pos]['Data Nascimento']
        departamento=dados['Pessoas'][pos]['Departamento']
        titulo=dados['Pessoas'][pos]['Titulo']

        id2 = LerNumero2("ID (%s)?" % str(id), 170000, 1709999)
        nome2 = LerNome2("Nome (%s)?" % nome)
        eMail2 = LerEMail2("E-Mail (%s) ?" % eMail)
        telemovel2 = LerTelemovel2("Telemóvel (%s)?" % str(telemovel))
        departamento2 = LerNumero2("Departamento (%s) ('1-Design de Software "
                                 "2-Programação 3-Ciência de Dados 4-Recursos Humanos 5-Departamento Legal')?" % departamento, 1, 5)
        data_nascimento2 = LerData2("Data Nascimento (%s)?" % data_nascimento, None, datetime.now())
        titulo2 = LerDeLista2("Título (%s)?" % titulo, ['Designer', 'Programador', 'Testador', 'GRH', 'Advogado'])

        print('\033[0:92mCampos alterados\033[0m')
        if id2 != None:
            print("ID.............:", id2)
            dados['Pessoas'][pos]['ID']=str(id2)
        if nome2 != None:
            print("Nome...........:", nome2)
            dados['Pessoas'][pos]['Nome']=nome2
        if eMail2 != None:
            print("EMail..........:", eMail2)
            dados['Pessoas'][pos]['EMail']=eMail2
        if telemovel2 != None:
            print("Telemóvel......:", telemovel2)
            dados['Pessoas'][pos]['Telemóvel']=str(telemovel2)
        if departamento2 != None:
            print("Departamento...:", departamento2)
            dados['Pessoas'][pos]['Departamento']=departamento2
        if data_nascimento2 != None:
            print("Data Nascimento:", data_nascimento2)
            dados['Pessoas'][pos]['Data Nascimento']=str(data_nascimento2)
        if titulo2 != None:
            print("Título.........:", titulo2)
            dados['Pessoas'][pos]['Titulo']=titulo2