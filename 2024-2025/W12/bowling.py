from operator import itemgetter

def leggiRisultati(filename):
    giocatori = []
    with open(filename, 'r') as file:
        for line in file:
            parti = line.strip().split(';')
            punti = [int(dato) for dato in parti[2:]]
            somma = sum(punti)
            num10 = punti.count(10)
            num0 = punti.count(0)

            giocatore = {
                'nome' : parti[1],
                'cognome' : parti[0],
                'punti' : somma,
                '10' : num10,
                '0' : num0
            } 

            giocatori.append(giocatore)

    return giocatori

def main():
    giocatori = leggiRisultati('bowling.txt')

    # stampa classifica
    giocatori.sort(key = itemgetter('punti'), 
                   reverse = True)

    for g in giocatori:
        print(f"{g['nome']:10} {g['cognome']:10} {g['punti']:4}")

    #stampa max 10
    giocatori.sort(key = itemgetter('10'), reverse = True)
    massimo = giocatori[0]
    if massimo['10'] > 0:
        print(f"{massimo['cognome']} {massimo['nome']} ha abbattuto tutti i birilli {massimo['10']} volta/e")

    # stampa max 0
    giocatori.sort(key = itemgetter('0'), reverse = True)
    massimo = giocatori[0]
    # massimo = max(giocatori, key = itemgetter('0))
    if massimo['0'] > 0:
        print(f"{massimo['cognome']} {massimo['nome']} ha mancato tutti i birilli {massimo['0']} volta/e")


main()