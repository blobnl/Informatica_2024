'''
dato il valore del saldo di un conto
e la precentuale di interesse sul conto,
calcolare il numeo di anni necessari per raddoppiare il saldo iniziale

100 1
105 2
110,25 3
'''

''''
ALGORITMO:

chiedere saldo e tassointeresse
anni = 0
saldocorrente = saldo

finchè saldocorrente < 2 * saldoIniziale
    interesse = saldo corente * tassoInteresse
    saldocorrente = saldocorrente + interesse
    anno = anno + 1

stampa anno
'''

# inizialiazzazion evariabili ciclo
saldoIniziale = float(input("Inserisci saldo "))
tassoInteresse = float(input("Inserisci tasso interesse: "))
anno = 0
saldoCorrente = saldoIniziale

# ciclo
while saldoCorrente < 2 * saldoIniziale:
    saldoCorrente = saldoCorrente * (1 + tassoInteresse)
    anno = anno + 1

# istruzioni successive al ciclo
print(f'IL saldo iniziale di {saldoIniziale:.2f} è raddoppiato in {anno} anni e vale {saldoCorrente:.2f}')