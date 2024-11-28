'''
leggere un file csv in ingresso che contiene un DB difilm
Salvare in output in formato csv i film presentati tra il 1990 e il 1999 (inclusi)
scrivendo in uscita solo i dati relativi ai campi
"Name","Year","Actors"

'''

from csv import reader, writer


def main():
  IN_FILE = 'movies.csv'
  OUT_FILE = 'filtered.csv'
  with open(IN_FILE, encoding = 'utf-8') as file:
    csvReader = reader(file)
    out = [[row[0], row[1]] for row in csvReader if row[1] >= '1990' and row[1] <= '1999']

  print(out)


main()
