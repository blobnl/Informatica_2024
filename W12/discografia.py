''''
discografia...
soluzione con dizionario
'''

def creaDatabase(filename):
    db = {}
    with open(filename, 'r') as file:
        for line in file:
            parti = line.strip().split(';')
            (id, fileCanzoni) = (parti[0], parti[1])

            with open(fileCanzoni, 'r') as fc:
                for line in fc:
                    parti = line.strip().split(';')
                    (anno, titolo) = (parti[0], parti[1])
                    if anno in db:
                        db[anno].append( (titolo, id) )
                    else:
                        db[anno] = [(titolo, id)]

    return db


def main():
    db = creaDatabase('artisti.txt')

    for anno in sorted(db):
        canzoni = db[anno]
        print(f'{anno}:')
        for (titolo, id) in canzoni:
            print(f'{titolo:30s} {id}')

main()