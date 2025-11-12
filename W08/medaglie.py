def main():
    COUNTRIES = 9
    MEDALS = 3

    counts = [
            [0,3,0],
            [0,0,1],
            [0,2,0],
            [1,3,0],
            [1,2,3],
            [0,3,4],
            [4,3,0],
            [1,3,0],
            [0,0,0]
        ]
    
    stampaMedagliere(counts)
    medaglieTotali = contaMedaglie(counts)
    print(medaglieTotali)

    maxMedaglie = max(medaglieTotali)
    for (idx, medaglie) in enumerate(medaglieTotali):
        if medaglie == maxMedaglie:
            print(f'Nazione: {idx+1}, medaglie = {maxMedaglie} {counts[idx]}')


def stampaMedagliere(tabella):
    for riga in tabella:
        medaglie = 0
        for dato in riga:
            print(f'{dato:10}', end = '')
            medaglie += dato
        print(f'\t{medaglie=}')

def contaMedaglie(tabella):
    medaglieTotali = [sum(riga) for riga in tabella]
    return medaglieTotali
    '''
    medaglieTotali = []
    for riga in tabella:
        medaglieTotali.append(sum(riga))
    '''

    return medaglieTotali


main()