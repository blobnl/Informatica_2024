import csv
from operator import itemgetter

def main():
    elenco = []
    with open('14BHDPI_2024.csv', 'r') as file:
        csvReader = csv.DictReader(file)
        for studente in csvReader:
            elenco.append(studente)

    elenco.sort(key = itemgetter('NOME', 'MATRICOLA'))
    for studente in elenco:
        print(studente)

main()