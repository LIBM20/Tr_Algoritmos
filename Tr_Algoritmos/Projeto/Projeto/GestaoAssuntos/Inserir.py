from ValidacaoDados import *
from ValidacaoDados.LerNumero import *
from ValidacaoDados.LerAssunto import *
from ValidacaoDados.LerEmail import *
from ValidacaoDados.LerData import *
from ValidacaoDados.LerDeLista import *
from ValidacaoDados.LerTelemovel import *
from datetime import datetime

def Inserir(dados):
    val = 1
    print("\033[1:4:36mInserir assunto\033[0m")
    id = LerNumero2("ID ? ", 1, 9999999)
    for assunto in dados['Assuntos']:
        if str(assunto['ID']) == str(id):
            val = 0
            print("\033[0:91mEste id já está a ser ocupado\033[0m")
    if val==1:
        assunto = LerAssunto("Assunto ? ")
        data = LerData("Data ? ")
        data_limite = LerData("Data limite? ", data)
        prioridade = LerNumero2("Prioridade (1-Muito Urgente, 2-Urgente, 3-Pouco Urgente) ? ", 1, 3)
        estado = LerAssunto("Estado do Assunto (Concluido, Por Tratar, Adiado) ? ")
        dados['Assuntos'].append({'ID': id,
                                  'Assunto': assunto,
                                  'Data': data.strftime ("%Y-%m-%d"),
                                  'Data Limite': data_limite.strftime ("%Y-%m-%d"),
                                  'Prioridade': prioridade,
                                  'Estado': estado})