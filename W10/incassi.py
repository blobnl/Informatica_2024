'''
Il file vendite.csv contiene in ogni riga la categoria di un prodotto 
e l'importo incassato separati da una virgola, 
ad esempio Elettronica,150.0. 

Scrivi un programma che calcoli l'incasso totale accumulato per ciascuna categoria, 
poi stampa i totali per ogni categoria (arrotondati a due cifre decimali) 
in ordine alfabetico di categoria 

[OPZIONALE: in ordine di guadagno]

algoritmo:
1 leggere le informaizoni e creare dizionario
    per ogni riga del file
        leggi categoria e costo
        aggiorn adizionario
2. stampare i dati oridnati per chiave

'''
def leggiDati(filename):
    incassi = {}
    with open(filename, 'r') as file:
        for riga in file:
            riga = riga.strip()
            parti = riga.split(',')
            categoria = parti[0]
            incasso = float(parti[1])
            
            if categoria not in incassi:
                incassi[categoria] = incasso
            else:
                incassi[categoria] += incasso
            #incassi[categoria] = incassi.get(categoria, 0) + incasso
            
    return incassi
                


def main():
    incassi = leggiDati('vendite.csv')
    
    for categoria in sorted(incassi):
        print(f'{categoria:15} {incassi[categoria]:10.2f}')

main()