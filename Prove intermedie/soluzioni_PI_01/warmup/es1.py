'''
## Testo esercizio 1

### Controllo della temperatura

Scrivere un programma Python che legga una temperatura, espressa come numero decimale (`float`), e stampi un messaggio in base al valore letto:

- `Freddo` se la temperatura è inferiore a 15.
- `Mite` se la temperatura è compresa tra 15 e 25, estremi inclusi.
- `Caldo` se la temperatura è superiore a 25.

Il programma deve stampare esclusivamente uno dei tre messaggi indicati, rispettando maiuscole e minuscole.

**Esempio di esecuzione**

Input: 22.5

Output: Mite

**Altri esempi**

Input: 15

Output: Mite

Input: 27

Output: Caldo
'''

temperatura = float(input("Inserire temperatura: "))

if temperatura < 15:
    print("Freddo")
elif temperatura <= 25:
    print("Mite")
else:
    print("Caldo")
