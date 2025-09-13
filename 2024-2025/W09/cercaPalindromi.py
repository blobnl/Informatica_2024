'''
scrivere un programma che legga un file che contiene un insieme di parole
(una parola per riga). Il programma deve stampare su schermo le sole parole
palindrome

e.g.:
Elenco parole palindrome:
radar
level
...

# algoritmo:
------------
per ogni parol nel file
    se è palindroma: -->
        stampa la parola


'''

def main():
    INPUT_FILE = 'parole_input.txt'
    with open(INPUT_FILE, 'r', encoding = 'utf-8') as file:
        for line in file:
            parola = line.strip().lower()
            if parola == parola[::-1]:
                print(parola)

main()
