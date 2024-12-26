import GestaoAssuntos.PesquisaAssuntoPorID
import GestaoPessoas.PesquisaPorID

def ListarAta(dados, id_reuniao):
    print("Listar Ata",id_reuniao)
    reuniao = dados['Reunioes'][id_reuniao]
    id = reuniao['ID']
    local = reuniao['Local']
    data = reuniao['Data']
    meses = {"11":"novembro","12":"dezembro", "01":"janeiro","02":"fevereiro", "03":"março","04":"abril", "05":"maio","06":"junho", "07":"julho","08":"agosto", "09":"setembro","10":"outubro"}
    hora = reuniao['Hora']
    dia = reuniao['Data'][8:]
    mes = meses[reuniao['Data'][5:7]]
    ano = reuniao['Data'][0:4]
    assuntos = reuniao['Assuntos']
    pessoas = reuniao['Pessoas']

    fn = 'Convocatoria_%s.HTML' % data
    f=open(fn,"wt")
    print("<center><img height='100px' src='https://politecnicoguarda.pt/wp-content/uploads/2021/11/ESTG.svg'></center>", file=f)
    print("<center><h1>Ata</h1></center>", file=f)
    s =  """Às %s, do dia %s de %s de %s, na %s de
     reunião ....  
    """ % (hora, dia, mes, ano, local)
    print("<center><p>%s</p></center>" % s, file=f)

    for a in assuntos:
        id    = a["ID"]
        assunto = a["Assunto"]
        notas = a["Notas"]
        tarefas = a["Tarefas"]
        r = GestaoAssuntos.PesquisaAssuntoPorID.PesquisaAssuntoPorID(dados, id)
        a = dados["Assuntos"][r]

        print("<center><h2>%d - %s</h2></center>" % (id, assunto), file=f)

        print("<center><h3>Notas</h3></center>", file=f)
        for n in notas:
            id = n ["ID"]
            nota = n ["Notas"]
            subscritores = n['Subscritores']
            print("<center><p>%s (%d)</p></center>" %(nota, id), file=f)
            if len(subscritores)>0:
                print("<ol>",file=f)
                for x in subscritores:
                    y = GestaoPessoas.PesquisaPorID.\
                        PesquisaPorID(dados, x)
                    y = dados["Pessoas"][y]
                    print("<center><li> (%s)</li></center>" % (x), file=f)
                print("<center></ol></center>",file=f)

        print("<center><h3>Tarefas</h3></center>", file=f)

        for t in tarefas:
            id = t ["ID"]
            tarefa = t ["Tarefas"]
            pessoas = t ["Pessoas(ID)"]
            print("<center><p>%s (%d) </p></center>" %(tarefa, id), file=f)
            if len(pessoas)>0:
                print("<center><ol></center>",file=f)
                for x in pessoas:
                    y = GestaoPessoas.PesquisaPorID.\
                        PesquisaPorID(dados, x)
                    y = dados["Pessoas"][y]
                    print("<center><li> (%s)</li></center>" % (x), file=f)
                print("</ol>",file=f)

    print("<br>", file=f)
    print("<center><p>Guarda, %s de %s de %s</p></center>" %(dia, mes, ano), file=f)
    print("<br><br>", file=f)
    
    print("<style>table,th,td{border:1px solid blue;border-collapse:collapse;width:400px}</style>", file=f)


    f.close()
    import os
    os.system(fn)

