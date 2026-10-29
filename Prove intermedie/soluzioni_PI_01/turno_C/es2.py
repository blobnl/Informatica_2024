'''
Testo esercizio 2

### L'occupazione massima del parcheggio

Un parcheggio ha `100` posti auto ed è inizialmente vuoto. Durante la giornata vengono registrati gli ingressi e le uscite. Il programma legge una sequenza di numeri interi, uno per riga, terminata dalla sentinella `0` (che non rappresenta un movimento):

- Un valore positivo indica quante automobili entrano.
- Un valore negativo indica quante automobili escono.

Si garantisce che ogni variazione prima della sentinella sia diversa da zero e che il numero di automobili presenti rimanga sempre compreso tra `0` e `100`, estremi inclusi. Si garantisce inoltre **almeno una variazione prima dello 0**.

Il programma deve stampare:

1. Il **massimo numero di automobili presenti contemporaneamente** nel corso della giornata.
2. Il **numero di volte in cui, dopo una variazione, il parcheggio raggiunge quel valore massimo**.

La situazione iniziale (parcheggio vuoto prima di ogni variazione) **non** conta come evento. Se lo stesso massimo viene raggiunto di nuovo dopo essere stato abbandonato, va contato nuovamente.

**Esempio di esecuzione**:

Input:
```text
10
-5
5
-5
5
0
```
Output atteso:
```text
Massimo auto presenti: 10
Numero di volte: 3
```
Le occupazioni dopo ogni variazione sono `10, 5, 10, 5, 10`.
'''

presenti = 0
massimo = 0
volte = 0

variazione = int(input("Inserire variazione: "))
while variazione != 0:
    presenti += variazione
    if presenti > massimo:
        # aggiorna massimo e resetta contatotre volte
        massimo = presenti
        volte = 1
    elif presenti == massimo:
        # incrementa il numero di volte in cui si è raggiunto il massimo
        volte += 1
    variazione = int(input("Inserire variazione: "))

print(f"Massimo auto presenti: {massimo}")
print(f"Numero di volte: {volte}")
