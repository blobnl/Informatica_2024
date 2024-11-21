'''
Leggere il testo di una canzone dal file lyrics.txt
e separare tutte le parole del testo, rimuovendo eventuali caratteri di punteggiatura
e stampare su schermo ogni parola su una riga diversa

# algoritmo
finchè ci sono righe nel file
    separa in parti la riga
    per ogni parte:
        rimuovi eventuali caratteri di punteggiatura
        stampa parte

'''

def main():
    with open('lyrics.txt', 'r', encoding = 'utf-8') as file:
        for line in file:
            line = line.strip()
            parti = line.split()
            #print(parti)

            for parte in parti:
                parte = parte.strip('.,;:!?')
                print(parte)

main()
