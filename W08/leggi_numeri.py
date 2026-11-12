'''
leggere il fie numeri.txt
il file contiene un valore float per riga
creare un file in uscita di nome dati_e_totale.txt
che contenga i valori allineati in tabella e 
stampati uno per riga con due cifre decimali, 
poi un separatore
e il totale della loro somma

'''


def main():
    FILE_IN = 'numeri.txt'
    FILE_OUT = 'dati_e_totale.txt'
    
    with open(FILE_IN, 'r') as fileIn:
        with open(FILE_OUT, 'w') as fileOut:
            somma = 0
            for riga in fileIn:
                dato = float(riga)
                somma += dato
                fileOut.write(f'{dato:10.2f}\n')
              
              
            fileOut.write("="*10 + '\n') 
            fileOut.write(f'{somma:10.2f}\n') 

            


main()