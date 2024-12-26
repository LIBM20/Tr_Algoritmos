from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerNome import *
from ValidacaoDados.LerEmail import *
from ValidacaoDados.LerData import *
from ValidacaoDados.LerDeLista import *
from ValidacaoDados.LerTelemovel import *
from datetime import datetime
def Inserir(dados):
    val = 1
    print("\033[1:4:36mInserir pessoa\033[0m")
    id = LerNumero("ID ?", 1700000, 1709999)
    for pessoa in dados['Pessoas']:
        if str(pessoa['ID']) == str(id):
            val = 0
            print("\033[0:91mEste id já está a ser utilizado\033[0m")
    if val==1:
        nome = LerNome("Nome ? ")
        eMail = LerEMail("E-Mail ? ")
        telemovel = LerTelemovel("Telemóvel ?  ")
        departamento = LerNumero("Departamento ('1-Design de Software 2-Programação 3-Ciência de Dados 4-Recursos Humanos 5-Departamento Legal')? ", 1, 5)
        data_nascimento = LerData("Data Nascimento ? ", None, datetime.now())
        titulo = LerDeLista("Título ?", ['Designer', 'Programador', 'Testador', 'GRH', 'Advogado'])
        dados['Pessoas'].append({'ID': id,'Nome': nome,
                                 'EMail':eMail,
                                 'Telemóvel': telemovel,
                                 'Departamento': departamento,
                                 'Data Nascimento': "%s" % data_nascimento,
                                'Titulo':titulo })






