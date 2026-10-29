'''
Testo esercizio 1

### Le spese di una giornata

Un negozio registra gli importi degli acquisti di una giornata. Scrivere un programma che legga un intero positivo `N` e successivamente `N` importi, uno per riga, ciascuno espresso come numero `float` non negativo.

Il programma deve stampare:

1. L'**incasso totale** della giornata.
2. La **percentuale di acquisti** con importo strettamente superiore a 20 euro, rispetto ai `N` acquisti.

Usare esattamente le etichette indicate nell'output di esempio. Non è richiesta una particolare formattazione decimale.

**Esempio di esecuzione**:

Input:
```text
5
12
25
8
20
35
```
Output atteso:
```text
Incasso totale: 100.0
Percentuale sopra 20: 40.0
```
'''

n = int(input("NUmero importi: "))
totale = 0.0
sopra_20 = 0

for i in range(n):
    importo = float(input(f"Incasso giorno {i+1}: "))
    totale += importo
    if importo > 20:
        sopra_20 += 1

print(f"Incasso totale: {totale}")
print(f"Percentuale sopra 20: {sopra_20 * 100 / n:.2f}%")
