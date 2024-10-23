nome = "carlo"

for carattere in nome:
    print(carattere)

print()

for indice in range(len(nome)):
    elemento = nome[indice]
    print(indice, elemento)

print()

for (posizione, valore) in enumerate(nome):
    print(posizione, valore)

