from operator import itemgetter

def calcolaMOE(posizione):
    MOE = {1: 1, 2: 0.1, 3: 0.05}
    if posizione not in MOE:
        return 0
    return MOE[posizione]

def leggiRisultati(filename):
    risultati = {}
    with open(filename, 'r') as file:
        for line in file:
            parti = line.strip().split()
            (nazione, MOE) = (parti[-2], calcolaMOE(int(parti[-1])))

            if nazione not in risultati:
                risultati[nazione] = MOE
            else:
                risultati[nazione] += MOE

    return risultati

def main():
    risultati = leggiRisultati('nazioni.txt')
    classifica = sorted(risultati.items(), key = itemgetter(1), reverse = True)
    for (nazione, MOE) in classifica:
        print(f'{nazione} {MOE:6.2f}')


main()