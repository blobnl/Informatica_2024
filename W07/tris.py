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

def inserisciMossa(griglia, player):
    pass

def controllaGriglia(griglia):
    """
    :param griglia: la griglia di gioco
    :return: True se la partita è terminata, False altrimenti
    """
    # orizzontali
    for riga in griglia:
        if riga[0] != " " and riga[0] == riga[1] and riga[1] == riga[2]:
            stampaVincitore(riga[0])
            return True

    # verticali
    for colonna in range(len(riga[0])):
        if griglia[0][colonna] != " " and griglia[0][colonna] == griglia[1][colonna] \
            and griglia[1][colonna] == griglia[2][colonna]:
            stampaVincitore(griglia[0][colonna])
            return True

    # diagonali
    if griglia[0][0] != " " and griglia[0][0] == griglia[1][1] \
        and griglia[1][1] == griglia[2][2]:
        stampaVincitore(griglia[0][0])
        return True

    if griglia[0][2] != " " and griglia[0][2] == griglia[1][1] \
        and griglia[1][1] == griglia[2][0]:
        stampaVincitore(griglia[0][2])
        return True

    # controlla pareggio --> se c'è almeno una casella libera, niente pareggio, altrimenti pareggio
    for riga in griglia:
        if " " in riga:
            return False


    print("Non ci sono più mosse disponibili. Pareggio")
    return True

def main():
    PLAYER_1 = 'X'
    PLAYER_2 = 'O'

    griglia = creaGriglia() 
    stampaGriglia(griglia)

    finito = False
    player = PLAYER_1
    while not finito:
        inserisciMossa(griglia, player)
        stampaGriglia(griglia)
        finito = controllaGriglia(griglia)
        if player == PLAYER_1:
            player = PLAYER_2
        else:
            player = PLAYER_1

main()
