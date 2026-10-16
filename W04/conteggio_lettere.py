'''
Uso di cicli per conteggio di elementi che soddisfano una (o più) condizione

ESEMPIO: data una stringa inserita da tastiera,
contare il numero di vocali e consonanti
(indipendentemente da maiuscolo/minuscolo)

ALGORTIMO: 

inserisci stringa
stranga = stringa in minuscolo
vocali = 0, consonanti = 0
per ogni lettera di stringa:
    se lettera è alfabetica
        se lettera in "aeiou" -> incrementa vocali
        altrimenti incerementa consonsnati
        
stampa valori troavti

'''

stringa = input("Inserisci stringa: ")
stringa = stringa.lower()

idx = 0
vocali = 0
consonanti = 0

while idx < len(stringa):
    carattere = stringa[idx]
    if carattere.isalpha():
        if carattere in "aeiou":
            vocali += 1
        else:
            consonanti += 1
    idx += 1

print(f"IL numero di vocali è {vocali}, quello di consonanti è {consonanti}")
