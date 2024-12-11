import operator

def leggiRisultati(fileName):

    giocatori = []

    with open(fileName, "r") as file:
        for line in file:
            parts = line.strip().split(";")
            points = [int(point) for point in parts[2:]]
            somma = sum(points)
            ctr10 = points.count(10)
            ctr0 = points.count(0)

            giocatori.append({"nome": parts[0], 'cognome' : parts[1],
                              "punti": somma,
                              "10": ctr10,
                              "0": ctr0})

    return giocatori


def main():
    giocatori = leggiRisultati("bowling.txt")
    giocatori.sort(key = operator.itemgetter("punti"), reverse = True)

    for giocatore in giocatori:
        print(f"{giocatore['nome']:10} {giocatore['cognome']:10} {giocatore['punti']:4}")

    giocatori.sort(key = operator.itemgetter("10"), reverse = True)
    if giocatori[0]["10"] > 0:
        print(f"{giocatori[0]['nome']} {giocatori[0]['cognome']} ha abbattuto tutti i birilli {giocatori[0]['10']} volta/e")

    giocatori.sort(key = operator.itemgetter("0"), reverse = True)
    if giocatori[0]["0"] > 0:
        print(f"{giocatori[0]['nome']} {giocatori[0]['cognome']} ha mancato tutti i birilli {giocatori[0]['0']} volta/e")


main()
