'''
In python le tabelle si possono gestire come liste di liste (righe x colonne)

esempio:
creare tabella 3x3, stampare somma per riga e per colonna

'''


tabella = [ [1,2,3],
           [4,5,6],
           [7,8,9]]

RIGHE = len(tabella)
COLONNE = len(tabella[0])

# somma righe
for r in range(RIGHE):
    print(f"Riga {r}, somma = {sum(tabella[r])}")  
    
# sooma per colonne
for c in range(COLONNE):
    somma = 0
    for r in range(RIGHE):
        somma += tabella[r][c]
    print(f"Colonna {c}, somma = {somma}")
    
for r in range(RIGHE):
    for c in range(COLONNE):
        tabella[r][c] = tabella[r][c] ** 2
        
print(tabella)

