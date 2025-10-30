''''
scrivere tabella potenze
NMAX -> potenza max
XMAX -> valore massimo

ALG:
stampa riga intestazione
stapa del corpo della tabella
    - per ogni riga
        stampa tutti gli elementi della riga

'''

N_MAX = int(input("n = "))
X_MAX = int(input("x = "))

# stampare instestazione
for n in range(1, N_MAX + 1):
    potenza = f"X^{n}"
    print(f"{potenza:>10}", end = "")

print()

# stampa corpo tabella
# ciclo esterno sulle righe, ogni riga è un valore
for x in range(1, X_MAX + 1):
    # per ogni colonna, n è l'esponente
    for n in range(1, N_MAX + 1):
        # stampa il valora x^n
        print(f"{x ** n:10d}", end = "")

    # vado a capo per nuova riga
    print()