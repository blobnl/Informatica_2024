'''
Vogliamo contare il numero di parole uniche (distinte tra loro) in un documento di testo
Es. il testo di “Mary had a little lamb” contiene 57 parole uniche
Il nostro compito è scrivere un programma che legga un documento di testo da
un file e determina il numero di parole uniche presenti nel documento

ALGORITMO:

0. parole = insieme vuoto
1. estrai tutte le parole dal file
  1.1 per ogni riga del file
    - estrai tutti i blocchi separati da spazi
    - ripulisci ogni blocco da caratteri di interpunzione, e inseriscili in ?
    parole
2. stampa dimensione di parole

'''


def estraiParole(filename):
  paroleUniche = set()
  with open(filename, 'r') as file:
    for riga in file:
      riga = riga.strip()
      parole = riga.split()
      for parola in parole:
        parola = parola.strip(',.:;!?"')
        paroleUniche.add(parola.lower())
        
  return paroleUniche
      

def main():
  parole = estraiParole("nurseryrhyme.txt")
  print(f'Parole uniche: {len(parole)}')
  print(sorted(parole))

main()
