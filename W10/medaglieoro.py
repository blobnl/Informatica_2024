
def MOE(posizione):
    # lookup tabel
    valore = {1:1, 2:0.1, 3:0.05}
    if posizione in valore:
        return valore[posizione]
    else:
        return 0

def leggiMedagliere(filename):
    elenco = {}
    with open(filename, 'r') as file:
        for line in file:
            parti = line.strip().split()
            (nazione, posizione) = (parti[2], int(parti[3]))
            medRel = MOE(posizione)
            if nazione in elenco:
                elenco[nazione] += medRel
            else:
                elenco[nazione] = medRel

    return elenco


def main():
    elenco = leggiMedagliere('nazioni.txt')
    for (nazione, medaglie) in elenco.items():
        print(f'{nazione=} {medaglie=}')
main()