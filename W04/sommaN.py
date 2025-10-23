# somma dei primi N numeri interi

# istruzioni di inizlaizzazione - A
N = int(input("Inserisci numero: "))
numero = N
somma = 0

# condizione C
while N > 0:
    # corpo del ciclo - B
    somma = somma + N
    N = N -1


# istrzuioni successive
print(f"La sooma dei primi {numero} è uguale a {somma}")