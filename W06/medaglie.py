'''
stampare tabella incolonnata con medaglie + medaglie per tipo + somma medaglie per nazione

'''

MEDALS = 3
COUNTRIES = 8

# lista di nomi di paesi
countries = ["Canada",
             "Italy",
             "Germany",
             "Japan",
             "Kazakhstan",
             "Russia",
             "South Korea",
             "United States"]

# tabella medaglie, per ogni nazione -> una riga: oro, argento, bronzo              
counts = [
    [0, 3, 0],
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0],
    [0, 0, 1],
    [3, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
]
