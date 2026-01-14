'''
generare indice analitico a partire da file ingresso
pagina: keyword
stampare inordine alfabetico di keyword le pagine in cui compare

ALGORITMO
elenco = {}
per ogni triga del file in ingresso
    estrai pagina, parola
    se parola in elenco, aggiungi pagina al set parole
    altrimenti aggiungi parola con {pagina} come valore

stampa elenco
per ogni chiave di elenco in ordine alfabetico:
    crea lista ordinata di pagine
    stampa chiave e elenco pagine

'''
def leggiIndiceAnalitico(filename):
    elenco = {}
    with open(filename, 'r') as file:
        for line in file:
            parti = line.strip().split(':')
            (parola, pagina) = (parti[1], int(parti[0]))
            if parola in elenco:
                elenco[parola].add(pagina)
            else:
                elenco[parola] = {pagina}

    return elenco

def main():
    #leggi elenco
    elenco = leggiIndiceAnalitico('indexdata.txt')
    #stanpa elenco
    for parola in sorted(elenco):
        pagine = sorted(elenco[parola])
        pagineStr = [str(pagina) for pagina in pagine]
        print(f'{parola}: {", ".join(pagineStr)}')

main()
