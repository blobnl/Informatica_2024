stringa = input("Inserisci una stringa: ")
sottostringa = input("INserisci stringa da cercare")

if sottostringa in stringa:
    print(stringa, "contiene", sottostringa)
else:
    print(stringa, "non contiene", sottostringa)
