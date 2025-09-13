'''
usare list comprehension per crare da una lista di giorni della settimana
- lista lunghezze stringa giorni
- lista nomi invertiti
- list giorni con lettera accentata
- list tuple di giorni con lunghezza uguale
'''


def main():
  giorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
  
  #- lista lunghezze stringa giorni
  lunghezze = []
  for giorno in giorni:
    lunghezza = len(giorno)
    lunghezze.append(lunghezza)

  print(lunghezze)

  # [f(elemento) for elemento in contenitore]
  lunghezza = [len(giorno) for giorno in giorni]
  print(lunghezza)

  #- lista nomi invertiti
  invertiti = [giorno[::-1] for giorno in giorni]
  print(invertiti)
  #- list giorni con lettera accentata
  accentati = []
  for giorno in giorni:
    if 'ì' in giorno:
      accentati.append(giorno)

  print(accentati)
  # [operazione(elemento) for elemento in contenitore if condizione(elemento)]
  accentati = [giorno for giorno in giorni if 'ì' in giorno]
  print(accentati)
  #- list tuple di giorni con lunghezza uguale
  uguali = []
  for i in range(len(giorni)):
    for j in range(i+1, len(giorni)):
      if len(giorni[i]) == len(giorni[j]):
        uguali.append( (giorni[i], giorni[j]) )

  print(uguali)
  '''
  [operazione(el1, el2, ...)
  for el1 in contenitore 1
  for el2 in contenitore 2...
  etc..
  if condizione(el1, el2,...)
  ]
  '''
  uguali = [
    (giorni[i], giorni[j]) for i in range(len(giorni)) for j in range(i+1, len(giorni))
    if len(giorni[i]) == len(giorni[j])  ]
  print(uguali)


main()
