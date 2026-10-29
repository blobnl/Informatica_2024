'''
Testo esercizio 2

### La sequenza crescente più lunga

Scrivere un programma che legga, uno per riga, una sequenza di 
numeri interi **non nulli**, terminata dal valore sentinella `0` 
(che non appartiene alla sequenza). Si garantisce che venga inserito 
almeno un numero prima della sentinella.

Determinare la **lunghezza della più lunga sottosequenza di 
elementi consecutivi strettamente crescenti**. Se un numero è
minore o uguale al precedente, la sottosequenza crescente corrente 
termina e ne inizia una nuova dal numero corrente. La lunghezza di una 
sottosequenza di un solo elemento è 1.

**Esempio di esecuzione**:

Input:
```text
3
5
8
2
4
7
9
6
0
```
Output atteso:
```text
Lunghezza massima: 4
```
La sottosequenza crescente più lunga è `2, 4, 7, 9`.
'''

finito = False
inseriti = 0

precedente = 0
numero = 0
lunghezza = 1
massimo = 0

while not finito:
    precedente = numero
    numero = int(input("Inserisci numero: "))
    inseriti += 1

    if numero == 0:
        finito = True
        continue

    # per poter procedere bisogna avere almeno due numeri inseriti
    if inseriti < 2:
        continue

    if numero > precedente:
        lunghezza += 1
    else:
        lunghezza = 1
    # massimo = max(massimo, lunghezza)
    if lunghezza > massimo:
        massimo = lunghezza

print("Lunghezza massima:", massimo)
