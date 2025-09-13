import csv
from operator import itemgetter

def leggiNomi(filename):
    nomi = {}
    with open(filename, 'r') as file:
        csvReader = csv.reader(file)
        next(csvReader)
        for studente in csvReader:
            nome = studente[2]

            if nome in nomi:
                nomi[nome] = nomi[nome] + 1
            else:
                nomi[nome] = 1

    return nomi


def main():
    DA_STAMPARE = 20
    elenco = leggiNomi('14BHDPI_2024.csv')
    elencoOrdinato = sorted(elenco.items(), key = itemgetter(1), reverse = True)

    for i in range(DA_STAMPARE):
        (nome, occorenze) = elencoOrdinato[i]
        print(f'{nome:20} {occorenze}')
    

main()