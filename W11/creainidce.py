
def leggiIndice(filename):
    indice = {}
    with open(filename, 'r') as file:
        for line in file:
            parti = line.strip().split(':')
            parola = parti[1]
            pagina = int(parti[0])
            if parola in indice:
                indice[parola].add(pagina)
            else:
                indice[parola] = {pagina}

    return indice


def main():
    indice = leggiIndice('indexdata.txt')
    
    for parola in sorted(indice):
        print(f'{parola}: ', end = '')
        pagine = sorted(indice[parola])
        for pagina in pagine:
            print(f'{pagina} ', end = '')
        print()


main()