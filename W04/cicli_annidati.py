'''
un ciclo può contenere al suo interno un ciclo...

Esempio: utile per gestinoe tabelle (righe e colonne)

PROBLEMA: dati XMAX valori (e.g., da 1 a 6)
e NMAX esponenti (e.g. 1...4)
Stampare una tabella con:
- riga di intestazione x^1  x^2 etc...
- per ogni valore intero, la riga corrispondente alle sue potenze

NOTA: la tabella deve essere ordinata...
(usare combinazione di f-string e named parameters opzionali di print)

ALGORITMO?
per ogni valore di esponente
    stampa x^esponente sulla stessa riga
    
per ogni x in [1, XMAX]
    per ogni n in [1, NMAX]
        stampa x ^ n sulla stessa riga (e in tabella)
    vai a capo

'''
XMAX = 6
NMAX = 4

# stampa intestazione
for n in range(1, NMAX + 1):
    valore = f"x^{n}"
    print(f"{valore:^15}", end = '')
    
print()

# stampa tabella
for x in range(1, XMAX + 1):
    for n in range(1, NMAX + 1):
        print(f"{x**n:^15}", end = '')
    print()
