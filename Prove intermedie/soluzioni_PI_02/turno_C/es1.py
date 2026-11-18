'''
## Testo esercizio 1

### Analisi dei tempi di percorrenza

Un servizio di trasporto registra, nell'ordine, i tempi di N viaggi,
espressi come numeri interi positivi. Si garantisce che N sia almeno 4.
Dopo aver letto i tempi, il programma legge anche un intero K compreso
tra 0 e N - 1 (estremi inclusi).

Scrivere un programma che memorizzi tutti i tempi in una lista
ed esegua **due elaborazioni indipendenti** sui dati acquisiti.

**Parte 1 - Rotazione della lista**

Costruire una nuova lista spostando **gli ultimi K tempi all'inizio**,
mantenendo invariato l'ordine relativo sia degli elementi spostati
sia degli elementi rimanenti.
Se K vale 0, la lista deve rimanere identica a quella originale.
Stampare la lista ruotata.

**Parte 2 - Tempi sopra la mediana**

Calcolare la **mediana** dei tempi originali:
ordinando i tempi in ordine crescente, la mediana è il valore centrale
se N è dispari, oppure la media aritmetica dei due valori centrali
se N è pari.

Stampare una lista con tutti i tempi strettamente superiori
alla mediana, **nell'ordine originale** ed **eventualmente ripetuti**.
Se nessun tempo supera la mediana, stampare una lista vuota.
La mediana non deve essere stampata.

**Esempio di esecuzione**

Valori inseriti, nell'ordine: N = 6;
tempi: 12, 8, 18, 8, 14, 10; K = 2.

**Output atteso:**

Lista ruotata: [14, 10, 12, 8, 18, 8]

Tempi sopra la mediana: [12, 18, 14]

Nell'esempio i tempi ordinati sono 8, 8, 10, 12, 14, 18
e la mediana è (10 + 12) / 2 = 11.
'''

n = int(input("Numero di tempi da inserire: "))

tempi = []
for i in range(n):
    tempo = int(input("Inserisci un tempo di percorrenza: "))
    tempi.append(tempo)

k = int(input("Di quante posizioni vuoi ruotare la lista? "))

# Parte 1: costruzione della lista ruotata
# somma di due sottosliste costruite con slicing
if k != 0:
    ruotata = tempi[n-k:] + tempi[:n-k]
else:
    ruotata = list(tempi)

'''
# soluzione alternativa con for

for i in range(n - k, n):
    ruotata.append(tempi[i])
for i in range(n - k):
    ruotata.append(tempi[i])
'''    

print("Lista ruotata:", ruotata)



# Parte 2: calcolo mediana
# nota: la lista originale deve essere mantnnuta come tale
ordinati = list(tempi)
ordinati.sort()

if n % 2 == 0:
    mediana = (ordinati[n // 2 - 1] + ordinati[n // 2]) / 2
else:
    mediana = ordinati[n // 2]

superiori = []
for valore in tempi:
    if valore > mediana:
        superiori.append(valore)
        
print("Tempi sopra la mediana:", superiori)
