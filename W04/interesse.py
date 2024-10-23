# lettura valori iniziali
saldo = float(input("Saldo iniziale: "))
tasso = float(input("interesse (in %): "))

# inizializzazione
obiettivo = saldo * 2
anni = 0

# ciclo gestione aggiornamento saldo
# condizione
while saldo < obiettivo:
    # isturzioni iterative
    saldo = saldo + saldo * tasso / 100.0
    # aggiornamento condizione
    anni = anni + 1

# termine while
print("il numero di anni per raddoppiare il saldo è", anni)