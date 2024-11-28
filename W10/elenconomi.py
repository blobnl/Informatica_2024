import csv

def main():
    elenco = []
    with open('14BHDPI_2024.csv', 'r') as file:
        cvsReader = csv.reader(file)
        next(cvsReader)
        elenco = [studente[2] for studente in cvsReader]

    elenco.sort()
    print(elenco)

main()