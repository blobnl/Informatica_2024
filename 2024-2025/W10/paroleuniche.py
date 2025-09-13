'''
1. leggere il file e strarre le parole
2. emorizzare le parole uniche
3. contarle

'''

def main():
    parole = set()
    with open('nurseryrhyme.txt', 'r') as file:
        # estrarre le singole parole
        for line in file:
            words = line.strip().split()
            for parola in words:
                parola = parola.strip(',.;:-_!?"')
                parole.add(parola.lower())

    print(f'Il file contiene {len(parole)} parole uniche')
    for parola in sorted(parole):
        print(parola)

main()
