def DepartamentosContar (dados):
    d = []
    q = []
    for i in range(len(dados['Pessoas'])):
            pessoa = dados['Pessoas'][i]
            dep = pessoa['Departamento']
            if dep in d:
                p = d.index(dep)
                q[p] = q[p] + 1
            else:
                d.append(dep)
                q.append(1)
    print("{0:20s}{1:10s}".
          format("Departamento","Quantidade"))
    for i in range(len(d)):
        print("{0:20s}{1:0d}"
              .format(str(d[i]),q[i]))

    fn = 'DepartamentosContar.HTML'
    f=open(fn,"wt")
    print("<img height='80px' src='https://politecnicoguarda.pt/wp-content/uploads/2021/11/ESTG.svg'><center><hr><h1>Departamentos</h1>", file=f)
    print("{0:20s}{1:10s}".
              format("<table><tr><th>Departamento</th>","<th>Quantidade</th></tr>"),file=f)
    for i in range(len(d)):
        print("<tr><td>{0:20s}</td><td>{1:5d}</td></tr>"
            .format(str(d[i]),q[i]), file=f)
    print("</table>", file=f)
    print("<style>table,th,td{border:2px solid black;border-collapse:collapse; padding:15px 40px; text-align:center;} h1{text-decoration:underline} table{margin:5%}</style>", file=f)
    f.close()
    import os
    os.system(fn)


