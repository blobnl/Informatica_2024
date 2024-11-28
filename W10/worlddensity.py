'''
Leggere due file che contengono dati sulle nazioni del mondo:
worldpop.txt e worldarea.txt  
Creare un file world_pop_density.txt che contenga i nomi delle nazioni e
la relativa densità di popolazione, dove i nomi delle nazioni siano allineati
a sinistra e i numeri siano allineati a destra

NOTA: i file di input contengono per ogni riga <stato> <dato> separati da spazio
ma attenzione che i nomi delle nazioni possono contenere spazi
e.g.
San Marino <dato>
Città del Vaticano <dato>

-> come posso separare in maniera corretta i due campi?

1. leggi i file input in due liste
2. scorri le liste per indice
  per ogni indice salva nel file in uscita i dati di densità

'''

AREA_FILE = 'worldarea.txt'
POPULATION_FILE = 'worldpop.txt'
DENSITY_FILE = 'worlddensity.txt'

def leggiFile(filename):
  elenco = []
  with open(filename, 'r') as file:
    for line in file:
      parti = line.strip().rsplit(' ', 1)
      elenco.append((parti[0], parti[1]))

  return elenco

def main():

  aree = leggiFile(AREA_FILE)
  popolazione = leggiFile(POPULATION_FILE)

  with open(DENSITY_FILE, 'w') as file:
    for i in range(len(aree)):
      (nazione, area) = aree[i]
      pop = popolazione[i][1]

      densita = float(pop)/float(area)
      file.write(f'{nazione:20} {densita:.2f}\n')

main()
