'''
BJ: 2 carte all'inzio, poi gioca il giocatore
(sceglie se chiedere una carta o fermarsi)
se non ha superato 21, gioca il banco (computer)
(chiede carte fino a quando non ha raggiunto 17,
se supera 21 perde). Alla fine vince chi ha il
punteggio più alto (in caso id parità. vince computer)

alg:
dai carta banco
dai due carte al giocatore

finchè nn termina
    se giocatore vuole carta
        aggiorna il punteggio
        se sforato
            termina
    altrimenti, termina

se giocatore in gioco e finchè non termina
    gioca banco
    se punteggio >= 17
        termina
    se sforato
        termina

stampa chi ha vinto


'''

import random

MAX_PUNTI = 21
STOP = 17

puntiGiocatore = 0
puntiBanco = 0
# dai cart banco e due al giocatore

carta = random.randint(1, 11)
puntiBanco += carta

carta = random.randint(1, 11)
print(f"Carta iniziale giocatore = {carta}")
puntiGiocatore += carta
carta = random.randint(1, 11)
puntiGiocatore += carta
print(f"Estratta carta = {carta}, punti = {puntiGiocatore}")

'''
finchè nn termina
    se giocatore vuole carta
        aggiorna il punteggio
        se sforato
            termina
    altrimenti, termina
'''

termina = False
while not termina:
    scelta = input("Vuoi una carta (s/n)? ")
    # ipotizzo input sempre corretto
    if scelta == 'n':
        termina = True
    else:
        carta = random.randint(1, 11)
        puntiGiocatore += carta
        print(f"Estratta carta = {carta}, punti = {puntiGiocatore}")
        if puntiGiocatore > MAX_PUNTI:
            termina = True

'''
se giocatore in gioco e finchè non termina
    gioca banco
    se punteggio >= 17
        termina
    se sforato
        termina
'''


print(f"Carta iniziale banco = {puntiBanco}")
termina  = False
while puntiGiocatore <= 21 and not termina:
    carta = random.randint(1, 11)
    puntiBanco += carta
    print(f"Estratta carta = {carta}, punti = {puntiBanco}")
    if puntiBanco >= STOP or puntiBanco > MAX_PUNTI:
        termina = True

# risultati
if puntiBanco <= MAX_PUNTI and puntiGiocatore <= MAX_PUNTI:
    if puntiBanco >= puntiGiocatore:
        print(f"Ha vinto il banco ({puntiBanco} a {puntiGiocatore})")
    else:
        print(f"Hai vinto tu ({puntiGiocatore} a {puntiBanco})")
elif puntiGiocatore > MAX_PUNTI:
    print("Hai sofrato, ha vinto il banco")
else:
    print("Il banco ha sforato, hai vinto tu")



