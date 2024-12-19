'''
INPUT
elenco cani in file csv info su razza, livello, score

OUTPUT
elenco per razza di valori medi per livello (se livello non presente, non stampare)
razza con punteggio medio expert più alto

i --> 0
info x razza --> dizionario (razza, ...?)
valori medi livello -> num cani per livello, media livello
--> dizionario (livello: {num, media})

dizionario razza : {livello : (num, media)}

'''

import csv

def leggiRazze(filename):
    razze = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            razza = row['Breed']
            livello = row['Training Level']
            score = float(row['Obedience Score'])

            if razza not in razze:
                razze[razza] = {}

            if livello not in razze[razza]:
                razze[razza][livello] = [1, score]
            else:
                razze[razza][livello][0] += 1
                razze[razza][livello][1] += score

            print(razza, livello, razze[razza])

    return razze

def main():
    razze = leggiRazze('dogs.csv')
    print(razze)

    maxExpert = 0
    maxRazza = ''

    for (razza, training) in razze.items():
        print(f'Razza: {razza}')
        for level in ["Beginner", "Intermediate", "Advanced", "Expert"]: # per stampare i livelli nell'ordine richiesto
            if level in training: # se un livello NON ha cani, allorta NON è presente nell'elenco (e quindi lo salto)
                media = training[level][1] / training[level][0]
                print(f'\tLivello {level}: media {media:.2f}')
                if level == 'Expert' and media > maxExpert:
                    maxExpert = media
                    maxRazza = razza

    print(f'La razza con punt max è {maxRazza}')

main()