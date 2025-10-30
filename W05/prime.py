'''
scrivere un programma che dato un numero N in ingresso, mi dica
se N è un numero primo oppure no

ALGORITMO:
inserire N
divisore = 2
divisoreTrovato = falso
se divisore <= N//2 e non ho trovato un divisore
    se divisore è divisore di N
        divisoreTrovato = vero
    altrimenti
        divisore = divisore + 1 
'''

N = int(input("Inserire numero: "))
divisore = 2
divisoreTrovato = False

while divisore <= N // 2 and not divisoreTrovato:
    if N % divisore == 0:
        divisoreTrovato = True
    else:
        divisore = divisore + 1

if divisoreTrovato:
    print(f"Il numero {N} non è primo")
else:
    print(f"Il numero {N} è primo")