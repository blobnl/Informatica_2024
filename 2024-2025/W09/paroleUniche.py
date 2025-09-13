'''
Leggere da file un elenco di parole
e stampare in output l'elenco delle parole uniche (indipendentemente da maisucole/minuscole)
in ordine alfabetico

Algoritmo:
----------
1. creare lista parole uniche
elenco = []
per ogni riga del file
  dividi la riga in parti
  per ogni parte
    ripulisci la parola e trasformala in minuscolo
    se la parola non è in elenco, aggiungila
2. ordinare lista
3. stampare

'''

def leggiFile(filename):
  elenco = []
  with open(filename, 'r', encoding = 'utf-8') as file:
    for line in file:
      parti = line.strip().split()
      for parola in parti:
        parola = parola.strip(',.;:?!').lower()
        if parola not in elenco:
          elenco.append(parola)

  return elenco

def main():
  INPUT_FILE = "sample.txt"
  elenco = leggiFile(INPUT_FILE)
  elenco.sort()

  for parola in elenco:
    print(parola)

main()
