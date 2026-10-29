'''
Testo esercizio 1

### La stazione meteorologica

Una stazione meteorologica registra le temperature di `N` giornate. Scrivere un programma che legga un intero positivo `N` e, nelle successive `N` righe, una temperatura per giornata (numero `float`).

Il programma deve stampare:

1. La **media** delle temperature registrate.
2. Il **numero di giornate** con temperatura strettamente inferiore a zero.

Usare esattamente le etichette indicate nell'output di esempio. Non è richiesta una particolare formattazione decimale.

**Esempio di esecuzione**:

Input:
```text
5
4
-2
0
8
-5
```
Output atteso:
```text
Media: 1.0
Giornate sotto zero: 2
```
'''

n = int(input("Inserire numero di giornate: "))
somma = 0.0
sotto_zero = 0

for i in range(n):
    temperatura = float(input("Temperatura: "))

    somma += temperatura

    if temperatura < 0:
        sotto_zero += 1

print(f"Media: {somma / n}")
print(f"Giornate sotto zero: {sotto_zero}")
