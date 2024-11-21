'''
leggere il file input.txt che contiene un numero float per ogni riga
Stampare un file in output che riporti:
- i numeri incolonnati con 2 cifre decimali
- la somma dei numeri letti
- la loromedia
'''


def main():
    INPUT_FILE = 'input.txt'
    OUTPUT_FILE = 'output.txt'

    dati = []
    with open(INPUT_FILE, 'r') as infile:
        for line in infile:
            dati.append(float(line))

    with open(OUTPUT_FILE, 'w') as outfile:
        for dato in dati:
            outfile.write(f'{dato:8.2f}\n')
            #print(f'f'{dato:8.2f}', file = outfile)

        outfile.write('-------------\n')
        outfile.write(f'Totale = {sum(dati):.2f}\n')
        outfile.write(f'Media = {sum(dati) / len(dati):.2f}')


main()
