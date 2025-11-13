'''
operazioni fondamentali
apertura
uso
chiusura
'''
# apertura
fileLettura = open('testo.txt', "r")

# elaborazione
print(fileLettura.read())

# chiusura
fileLettura.close()

#con with
with open('testo.txt', 'r', encoding = 'utf-8') as fileLettura:
    print(fileLettura.read())

with open('fileScritto.txt', 'w', encoding = 'utf-8') as fileScrittura:
    fileScrittura.write('questo è un file in scrittura....')
