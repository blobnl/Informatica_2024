'''
il file lyrics.txt contiene il testo di una canzone
scrivere un programma che separi le singole parole e le stampi a schermo, ordinate

NOTA: le parole possono essere separate da spazi (spacelike)
ma possono contenere anche caratteri di interpunzione 
--> combinare split() e strip()

'''
def leggiParole(filename):
    parole = []
    with open(filename, 'r', encoding='utf-8') as file:
        for riga in file:
            riga = riga.strip()
            parti = riga.split()
            
            for parte in parti:
                parte = parte.strip(",;:.!?")
                parole.append(parte.lower())
                
    return parole
            

def main():
    '''
    1. estrai tutte le parole
    2. ordina
    3. stampa
    '''
    
    parole = leggiParole("lyrics.txt")
    parole.sort()
    for parola in parole:
        print(parola)

main()