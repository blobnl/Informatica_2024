'''
## Testo esercizio 1

### Analisi dei punteggi

Un sistema registra, nell'ordine in cui vengono ottenuti,
N punteggi interi compresi tra 0 e 100. Si garantisce che N sia almeno 4.

Scrivere un programma che legga N e poi gli N punteggi,
memorizzandoli in una lista. Terminata l'acquisizione,
il programma deve eseguire **due elaborazioni indipendenti**,
entrambe sui punteggi originali.

**Parte 1 - Punteggi sopra la media**

Calcolare la media aritmetica dei punteggi e stampare,
in una lista, tutti i **valori distinti** strettamente superiori alla media,
ordinati dal maggiore al minore.
Se non ci sono valori sopra la media, stampare una lista vuota.

**Parte 2 - Picchi locali massimi**

Un punteggio è un *picco locale* quando è strettamente maggiore
sia del punteggio immediatamente precedente sia di quello
immediatamente successivo.
Il primo e l'ultimo elemento non possono essere picchi locali.

Determinare il valore massimo fra tutti i picchi locali e stampare,
in una lista, le **posizioni di tutti i picchi** aventi tale valore massimo,
in ordine crescente. Le posizioni sono numerate a partire da 1.
Se non esistono picchi locali, stampare una lista vuota.

**Esempio di esecuzione**

Valori inseriti, nell'ordine:
N = 8; punteggi: 10, 30, 20, 40, 15, 40, 5, 30.

**Output atteso:**

Punteggi sopra la media: [40, 30]

Posizioni dei picchi massimi: [4, 6]

Nell'esempio i picchi locali si trovano alle posizioni 2, 4 e 6,
con valori 30, 40 e 40. I picchi di valore massimo sono quindi quelli in posizione 4 e 6.
'''

n = int(input("Numero punteggi da inserire: "))

punteggi = []
somma = 0

# inserimento valori input
for i in range(n):
    valore = int(input("Inserisci un punteggio: "))
    punteggi.append(valore)
    somma += valore

# Parte 1: valori distinti strettamente sopra la media
media = somma / n
selezionati = []

# inserire solo valori distinti
for valore in punteggi:
    if valore > media and valore not in selezionati:
        selezionati.append(valore)

selezionati.sort(reverse = True)
print("Punteggi sopra la media:", selezionati)

# Parte 2: picchi locali di valore massimo
massimo_picco = -1
posizioni = []

for i in range(1, n - 1):
    # ricerca picco (posizioni, non valori...)
    # strettamente maggiore sia del punteggio immediatamente precedente
    # sia di quello immediatamente successivo
    if punteggi[i] > punteggi[i - 1] and punteggi[i] > punteggi[i + 1]:
        if punteggi[i] > massimo_picco:
            massimo_picco = punteggi[i]
            posizioni = [i + 1]
        elif punteggi[i] == massimo_picco:
            posizioni.append(i + 1)
            
print("Posizioni dei picchi massimi:", posizioni)
