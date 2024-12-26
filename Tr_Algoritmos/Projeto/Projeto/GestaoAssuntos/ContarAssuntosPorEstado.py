def ContarAssuntosPorEstado(dados):
    d = []
    q = []
    for index_assunto in range(len(dados['Assuntos'])):
        assunto = dados['Assuntos'][index_assunto]
        state = assunto['Estado']
        if state in d:
            p = d.index(state)
            q[p] = q[p] + 1
        else:
            d.append(state)
            q.append(1)
    print("{0:20s}{1:15s}".
          format("Estado", "Quantidade"))

    for index_assunto in range(len(d)):
        print("{0:20s}{1:0d}"
              .format(str(d[index_assunto]), q[index_assunto]))

    fn = 'ContarAssuntoPorEstado.html'
    f = open(fn, "wt")
    print("<img height='80px' src='https://politecnicoguarda.pt/wp-content/uploads/2021/11/ESTG.svg'><center><hr><h1>Assuntos Por Estado</h1>", file=f)
    print("{0:20s}{1:15s}".format("<table><tr><th>Estado</th>", "<th>Quantidade</th></tr>"), file=f)
    for i in range(len(d)):
        print("<tr><td>{0:20s}</td><td>{1:5d}</td></tr>".format(str(d[i]), q[i]), file=f)
    print("</table>", file=f)
    print("<style>table,th,td{border:2px solid black;border-collapse:collapse; padding:15px 40px; text-align:center;} h1{text-decoration:underline} table{margin:5%}</style>", file=f)
    f.close()
    import os
    os.system(fn)
