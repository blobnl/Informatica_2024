'''
gioco del tris (player1 vs player2)

inizializza griglia
finchè non è finita la parita:
    inserisci e controlla la mossa di giocatore
    stampa griglia
    finito = controlla stato partita
    scambia giocatore

'''
SIZE = 3
def creaGriglia():
    griglia = []
    for r in range(SIZE):
        griglia.append([' '] * SIZE)

    return griglia

def stampaGriglia(griglia):
    for r in range(SIZE):
        print(f'{griglia[r][0]}|{griglia[r][1]}|{griglia[r][2]}')
        if r < SIZE - 1:
            print('-+-+-')


def main():
    PLAYER_1 = 'X'
    PLAYER_2 = 'O'

    griglia = creaGriglia() 
    stampaGriglia(griglia)

main()