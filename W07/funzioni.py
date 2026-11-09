'''
- dichiarare e creare un funzione
- chiamare una funzione

- parametri di una funzine (naed parameters)
- argomenti e parametri
- valori di ritorno

- parametri di default

ES: 
- stampa listino
- gestione costo biglietto cinema (prezzo, qtà)
- sconto+ supplemento 3d

'''
def costo_totale(prezzo, quantita = 1, sconto = False, supplemento_3d = False):
    SCONTO = prezzo * 0.2
    SUPPELEMENTO = 3.50
    totale = prezzo * quantita
    if sconto:
        totale -= SCONTO * quantita
    if supplemento_3d:
        totale += SUPPELEMENTO * quantita
    return totale



def main():
    finito = False
    BIGLIETTO_BASE = 6.50
    
    while not finito:
        dato = input("Insreire numero di biglietti: ")
        if dato == '':
            finito = True
            continue
        sconto = input("Hai uno sconto (s/n)? ")
        haSconto = False
        if sconto == 's':
            haSconto = True
        conto = costo_totale(BIGLIETTO_BASE, int(dato), sconto = haSconto)
        
        print(f"Il totale è {conto:.2f}€")
            
main()
    
   


