'''
scrivere un progamma che sia in grado di giocare a tris (player vs player/player vs pc...)
board: tabella 3x3 di caselle (numerate da 1 a 9)
'''

'''
ALGORITMO
'''

import random

PLAYER_1 = 'X'
PLAYER_2 = 'O' # COMPUTER se umano vs computer

def main():
    # 1 cerazione griglia
    griglia = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    #griglia = [ [' '] * 3  for i in range(3)]

    finito = False
    # scelta giocatore inziale
    if random.randint(1,2) == 1:
        player = PLAYER_1
    else:
        player = PLAYER_2

    print(f'Inizia il giocatore {player}')

    # ciclo di gestione della partita
    while not finito:
        # gioca player/computer
        if player == PLAYER_1:
            inserisciMossa(griglia, player)
        else:
            gicaComputer(griglia, player)
        # stampa griglia
        stampaGriglia(griglia)
        # verfifia fine
        finito = controllaGriglia(griglia)
        # scambia player
        if player == PLAYER_1:
            player = PLAYER_2
        else:
            player = PLAYER_1


def gicaComputer(griglia, computer):
    print("Mossa")
    # algoritmo stupido: scelgo mossa casuale
    mossaNonValida = True
    while mossaNonValida:
        mossa = random.randint(1,9)
        r = (mossa - 1) // 3
        c = (mossa - 1) % 3
        if griglia[r][c] == ' ':
            griglia[r][c] = computer
            mossaNonValida = False

    return

def inserisciMossa(griglia, player):
    # inserimento e controllo mossa
    mossaNonValida = True

    while mossaNonValida:
        mossa = int(input(f'Inserire mossa {player} (1-9):'))
        if mossa < 1 or mossa > 9:
            print('Mossa non valida')
        else:
            riga = (mossa - 1) // 3
            colonna = (mossa - 1) % 3

            if griglia[riga][colonna] == ' ':
                mossaNonValida = False
                griglia[riga][colonna] = player
            else:
                print(f'La casella {mossa} è occupata')

    return





def stampaGriglia(griglia):
    rigaVuota = "-+-+-"
    for riga in range(len(griglia)):
        # scrivi riga
        print('|'.join(griglia[riga]))
        #print(griglia[riga][0] + "|" + griglia[riga][1] + "|" + griglia[riga][2])
        if riga < len(griglia) - 1:
            print(rigaVuota)

    return


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
    for colonna in range(len(griglia[0])):
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
        
    return True

def stampaVincitore(player):
    print(f"Ha vinto {player}")

main()
