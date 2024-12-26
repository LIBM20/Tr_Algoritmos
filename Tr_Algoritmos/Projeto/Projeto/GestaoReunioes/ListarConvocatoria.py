import GestaoAssuntos.PesquisaAssuntoPorID
import GestaoPessoas.PesquisaPorID

def ListarConvocatoria(dados, id_reuniao):
    print("Listar Convocatoria",id_reuniao)
    reuniao = dados['Reunioes'][id_reuniao]
    id = reuniao['ID']
    local = reuniao['Local']
    data = reuniao['Data']
    meses = {"11":"novembro","12":"dezembro","01":"janeiro","02":"fevereiro","03":"marco", "04":"abril", "05":"maio", "06":"junho", "07":"julho", "08":"agosto", "09":"setembro", "10":"outubro"}
    hora = reuniao['Hora']
    dia = reuniao['Data'][8:]
    mes = meses[reuniao['Data'][5:7]]
    ano = reuniao['Data'][0:4]
    assuntos = reuniao['Assuntos']
    pessoas = reuniao['Pessoas']
    fn = 'Convocatoria_%s.HTML' % data
    f=open(fn,"wt")
    print("<br>", file=f)
    print("<br>", file=f)
    print("<center><img height='80px' src='https://politecnicoguarda.pt/wp-content/uploads/2021/11/ESTG.svg'></center>", file=f)
    print("<br>", file=f)
    print("<center><h1>Convocatória</h1></center>", file=f)
    s =  """ Convocam-se todas as pessoas listadas em anexo, para uma reunião a realizar em %s,
    <br>pelas %s do dia %s de %s de %s, com a seguinte Ordem de Trabalhos:
    """ %(local, hora, dia, mes, ano)
    print("<center><p>%s</p></center>" % s, file=f)
    print("<center><ol></center>", file=f)
    for a in assuntos:
        assunto = a["Assunto"]
        print("<center><li>%s</li></center>" %assunto, file=f)
    print("</ol>", file=f)
    print("<br>", file=f)
    print("<center><p>Guarda, %s de %s de %s</p></center>" %(dia, mes, ano), file=f)
    print("<br>", file=f)
    print("<center><h2>Lista de Convocados</h2></center>", file=f)
    print("<center><table></center>", file=f)
    for a in pessoas:
        id = a["ID da Pessoa"]
        r = GestaoPessoas.PesquisaPorID.PesquisaPorID(dados, id)
        a = dados["Pessoas"][r]
        print("<tr><td>%s</td><td></td></tr>" % (a["Nome"]), file=f)
    print("</table>", file=f)
    print("<style>td{border-bottom:1px solid black;width:100px}</style>", file=f)
    print("<style>table{width:300px}</style>", file=f)
    
    f.close()
    import os
    os.system(fn)
