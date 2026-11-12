'''
open() e poi close()
meglio: with open() as file: ....

open:
r -> lettura (lettura da inizio file)
a -> append (scrive al fondo)
w -> write (riscrive il file)

Lettura:
- tutti i caratteri read()
- 1/n caratteri read(n)
- 1 riga readline()
- tutte le righe readlines() --> lista
- file come CONTENTITORE DI RIGHE
for riga in file:
    ....

    
Scrittura:
- per riga/stringa write() --> non inserisce 1n finale
- per insieme di righe writelines(lista) --> tutte le stringhe devono terminare per \n


'''

file = open("testo.txt", "r")

'''
for riga in file:
    print(riga)
'''

righe = file.readlines()
print(righe)
    
print("FINE LETTURA")

file.close()

with open("testo.txt", 'r', encoding='utf-8') as file:
    print(file.read())
    
with open("nuovo_file.txt", 'w', encoding='utf-8') as file:
    file.write("questo è il contenuto del file...\n")
    file.write("Seconda riga\n")
    
    
    with open("nuovo_file_2.txt", 'w', encoding='utf-8') as file:
        testo = ['prima riga\n', 'seconda riga \n','terza....\n']
        file.writelines(testo)
    
