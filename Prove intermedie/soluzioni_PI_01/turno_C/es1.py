'''
Testo esercizio 1

### Le consegne in ritardo

Un corriere effettua `N` consegne. Per ogni consegna si registra lo **scostamento in minuti** rispetto all'orario previsto: un valore negativo indica un anticipo, un valore positivo un ritardo, e zero una consegna puntuale.

Scrivere un programma che legga un intero positivo `N` e successivamente `N` scostamenti interi, uno per riga.

Il programma deve stampare:

1. La **somma dei soli minuti di ritardo** (ignorando gli anticipi).
2. La **percentuale di consegne in ritardo** rispetto alle `N` consegne.

Usare esattamente le etichette indicate nell'output di esempio. Non è richiesta una particolare formattazione decimale.

**Esempio di esecuzione**:

Input:
```text
5
-3
8
0
5
-2
```
Output atteso:
```text
Minuti totali di ritardo: 13
Percentuale in ritardo: 40.0
```
'''

n = int(input("Numero consegne: "))
ritardi = 0
minuti = 0

for i in range(n):
    scostamento = int(input(f"Consegna {i+1}: "))
    if scostamento > 0:
        ritardi += 1
        minuti += scostamento

print(f"Minuti totali di ritardo: {minuti}", minuti)
print(f"Percentuale in ritardo: {ritardi/n * 100: .2f}%")
