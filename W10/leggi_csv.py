#import csv

from csv import reader, writer

with open("studenti.txt", 'r') as file:
    csvReader = reader(file, delimiter = ';')
    prodotti = []
    for record in csvReader:
        prodotti.append(record)
        print
        
with open("nuovo_elenco.csv", 'w', encoding = 'utf-8') as file:
    csvWriter = writer(file, delimiter = ';')
    csvWriter.writerow(["Categoria", "Incasso"])
    csvWriter.writerows(prodotti)
    for prodotto in prodotti:
        csvWriter.writerow(prodotto)

