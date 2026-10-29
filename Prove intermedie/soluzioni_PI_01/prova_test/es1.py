'''
Testo esercizio 1

### Il biglietto del museo

Un museo applica le seguenti tariffe, in euro:

- Età inferiore a 12 anni: 5 euro.
- Età da 12 a 64 anni (estremi inclusi): 12 euro.
- Età da 65 anni in poi: 7 euro.

La domenica ciascun biglietto costa 2 euro in meno rispetto alla tariffa ordinaria.

Scrivere un programma che legga **due valori, uno per riga**: l'età del visitatore (un intero non negativo) e il giorno della settimana (una stringa in minuscolo, senza accenti, ad esempio `lunedi` oppure `domenica`). Il programma deve stampare **solo il prezzo finale del biglietto**, come numero intero.

**Esempio di esecuzione** (le righe dell'input sono inserite nell'ordine indicato):

Input:
```text
70
domenica
```
Output atteso:
```text
5
```
'''

eta = int(input("Età visitatore: "))

# lower() per evitare problemi con maiuscole e minuscole
giorno = input("Giorno di visita: ").lower()

if eta < 12:
    prezzo = 5
elif eta < 65:
    prezzo = 12
else:
    prezzo = 7
if giorno == "domenica":
    prezzo -= 2

# il testo chiedeva di stampare SOLO il prezzo del biglietto....
print(prezzo)
