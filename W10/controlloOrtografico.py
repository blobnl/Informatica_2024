'''
Controllare il corretto ‘spelling’ di un documento,
stampando tutte le parole che non compaiono in un apposito dizionario

words --> dizionario
alice30.txt --> testo

ALGORITMO:
 dizionario = leggi parole dizionario
 testo = leggi parole testo
 parole non corrette = testo - dizionario

'''

def leggiParoleUniche(filename):
    parole = set()
    with open(filename, 'r', encoding = 'utf-8') as file:
        for line in file:
            # puliziza carteri "strani" tra parole
            line = line.replace('--', ' ').replace('/', ' ')
            parti = line.strip().split()
            for parte in parti:
                parola = parte.lower().strip(',;.:?!"\'()[]{}*+-_')
                if parola != '':
                    parole.add(parola)

    return parole


def main():
    dizionario = leggiParoleUniche('words')
    testo = leggiParoleUniche('alice30.txt')
    nonCorrette = testo.difference(dizionario)

    for parola in sorted(nonCorrette):
        print(parola)

main()
