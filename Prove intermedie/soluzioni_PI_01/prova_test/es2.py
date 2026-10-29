'''
Testo esercizio 2

### I divisori di un numero

Scrivere un programma che legga un numero intero positivo `N` e stampi **tutti i suoi divisori positivi in ordine crescente**, uno per riga. Un intero positivo `d` è divisore di `N` se `N % d == 0`.

**Esempio di esecuzione**:

Input:
```text
12
```
Output atteso:
```text
1
2
3
4
6
12
```
'''

n = int(input("inserire numero: "))

for d in range(1, n + 1):
    if n % d == 0:
        print(d)
