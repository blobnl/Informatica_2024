''''
discografia...
soluzione con lista
'''

from operator import itemgetter

def creaDatabase(filename):
    db = []
    with open(filename, 'r') as file:
        for line in file:
            parti = line.strip().split(';')
            (id, fileCanzoni) = (parti[0], parti[1])

            with open(fileCanzoni, 'r') as fc:
                for line in fc:
                    parti = line.strip().split(';')
                    (anno, titolo) = (parti[0], parti[1])
                    db.append((anno, titolo, id))

    return db


def main():
    db = creaDatabase('artisti.txt')
    db.sort(key = itemgetter(0))

    annoCorrente = 0
    for (anno, titolo, id) in db:
        if anno != annoCorrente:
            annoCorrente = anno
            print(f'{anno}:')

        print(f'{titolo:30s} {id}')

main()