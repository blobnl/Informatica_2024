'''
leggere un file csv in ingresso che contiene un DB di film
Salvare in output in formato csv i film presentati tra il 1990 e il 1999 (inclusi)
scrivendo in uscita solo i dati relativi ai campi
"Name","Year","Actors"

filtrati = []
per ogni riga del file
  se l'ann è compreso tra 1990 e 1999
    aggiungi a filtrati

salva eleco dati filtrati nel file di uscita

'''

from csv import reader, writer


def main():
  IN_FILE = 'movies.csv'
  OUT_FILE = 'filtered.csv'


  # lettura e filtraggio dati
  filtrati = []
  with open(IN_FILE, 'r', encoding = 'utf-8') as file:
    csvReader = reader(file)
    next(csvReader)
    for film in csvReader:
      filtrati = [[film[0], film[1], film[4]]
                  for film in csvReader 
                  if int(film[1]) >= 1990 and int(film[1]) <= 1999]
      '''
      anno = int(film[1])
      if anno >= 1990 and anno <= 1999:
        filtrati.append([film[0], film[1], film[2].strip()])
      '''

  # salvataggio dei dati
  # il file va apeto specificando nwewline = '' altrimenti su windows aggiunge uno \n
  # dopo ogni riga stampata
  with open(OUT_FILE, 'w', encoding = 'utf-8', newline='') as file:
    csvWriter = writer(file)
    csvWriter.writerows(filtrati)


main()
