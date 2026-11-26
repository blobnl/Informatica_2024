'''
leggere db dei film in movies.csv
filtrare i film tra il 1990 e il 1999
salvare in filtered.csv solo i film rimanenti e solo i campi 
titolo, anno, attori CON intestazione
'''
import csv

filtrati = []
with open("movies.csv", 'r', encoding = 'utf-8') as file:
    csvReader = csv.reader(file)
    next(csvReader)
    for record in csvReader:
        anno = int(record[1])
        if anno >= 1990 and anno <= 1999:
            filtrati.append(
                [record[0], anno, record[2]]
            )
        

with open("filtrati.csv", 'w', encoding = 'utf-8') as file:
    csvWriter = csv.writer(file)
    csvWriter.writerow(["Name", "Year", "Director"])
    csvWriter.writerows(filtrati)
    