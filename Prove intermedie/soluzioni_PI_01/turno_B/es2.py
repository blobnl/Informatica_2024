'''
Testo esercizio 2

### I cambi di direzione dell'ascensore

Un ascensore parte dal piano `0`. Il programma legge, uno per riga, i piani delle fermate successive, terminando quando viene inserito `-1` (sentinella che non è una fermata). Tutti i piani validi sono interi compresi fra `0` e `20` inclusi.

Si garantisce che **la prima fermata inserita sia diversa dal piano 0**; le fermate successive possono anche coincidere con il piano corrente. Nota: dato che l'ascensore parte dal piano 0, il primo movimento è necessariamente una salita.

Il programma deve contare quante volte l'ascensore **cambia direzione**, passando da salita a discesa o viceversa. Una fermata allo stesso piano non costituisce un movimento e non modifica la direzione precedente.

**Esempio di esecuzione**:

Input:
```text
3
5
2
2
4
1
-1
```
Output atteso:
```text
Cambi di direzione: 3
```
I cambi avvengono negli spostamenti `5 → 2`, `2 → 4` e `4 → 1`.
'''

finito = False
inseriti = 0

SALITA = 1
DISCESA = -1

direzione = 1
cambi = 0

# il piano iniziale è 0
piano = 0
nuovo_piano = -1

while not finito:
    nuovo_piano = int(input("Piano: "))

    # controlla condizione di terminazione inserimento
    if nuovo_piano == -1:
        finito = True
        continue

    if nuovo_piano > piano:
        # se la direzione era in discesa...
        if direzione == DISCESA:
            cambi += 1
        direzione = SALITA
    elif nuovo_piano < piano:
        # se la direzione era in salita...
        if direzione == SALITA:
            cambi += 1
        direzione = DISCESA

    # per il prossimo spostamento, piano diventa il piano attuale (nuovo_piano)
    piano = nuovo_piano

print("Cambi di direzione:", cambi)
