'''
## Testo esercizio 1

### Analisi delle rilevazioni

Un sistema acquisisce N rilevazioni numeriche intere, nell'ordine
in cui vengono effettuate. Si garantisce che N sia almeno 4.
I valori possono essere ripetuti.

Scrivere un programma che legga N e poi le N rilevazioni,
memorizzandole in una lista. Terminata l'acquisizione,
il programma deve eseguire **due elaborazioni indipendenti**
sulla stessa lista.

**Parte 1 - Valori ripetuti**

Stampare, in una lista, tutti i valori che compaiono
**almeno due volte** nelle rilevazioni,
senza ripetizioni e ordinati dal minore al maggiore.
Se non esistono valori ripetuti, stampare una lista vuota.

**Parte 2 - Variazione massima**

Per ogni coppia di rilevazioni consecutive,
calcolare la **differenza in valore assoluto** fra i due valori.
Stampare il valore della differenza massima e, in una lista,
tutte le posizioni in cui questa si verifica.
La posizione è quella della **prima rilevazione della coppia**
ed è numerata a partire da 1.
Le posizioni devono essere in ordine crescente.

**Esempio di esecuzione**

Valori inseriti, nell'ordine: N = 6;
rilevazioni: 10, 20, 10, 5, 15, 20.

**Output atteso:**

Valori ripetuti: [10, 20]

Variazione massima: 10

Posizioni: [1, 2, 4]

Nell'esempio la differenza massima fra
due rilevazioni consecutive vale 10 e si verifica nelle coppie
che iniziano alle posizioni 1, 2 e 4.
'''

n = int(input("Numero di rilevazioni da inserire: "))

# inserimento valori in input
valori = []
for i in range(n):
    valore = int(input("Inserisci una rilevazione: "))
    valori.append(valore)

# Parte 1: valori che compaiono almeno due volte (--> valori distinti)
ripetuti = []
for valore in valori:
    if valori.count(valore) >= 2 and valore not in ripetuti:
        ripetuti.append(valore)

ripetuti.sort()
print("Valori ripetuti:", ripetuti)

# Parte 2: variazione assoluta massima e posizioni
massima_variazione = -1
posizioni = []

for i in range(n - 1):
    differenza = abs(valori[i + 1] - valori[i])
    if differenza > massima_variazione:
        massima_variazione = differenza
        posizioni = [i + 1]
    elif differenza == massima_variazione:
        posizioni.append(i + 1)
        
print("Variazione massima:", massima_variazione)
print("Posizioni:", posizioni)
