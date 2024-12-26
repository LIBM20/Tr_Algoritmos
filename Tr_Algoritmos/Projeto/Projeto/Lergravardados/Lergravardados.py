import json

def GravarJSON(filename_in , dados):
    f = open(filename_in , 'w', encoding='utf8')
    print(dados)
    json.dump(dados , f, ensure_ascii=False , indent = 4) # to file
    f.close()
        # -------------
def LerJoson(filename_in):
    try:
        f = open(filename_in , encoding="utf8")
    except:
        return {"Pessoas":[],'Assuntos': [], 'Reunioes': []}
    dados = json.load(f)

    return dados
