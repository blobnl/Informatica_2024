'''
leggere da un file strutturato un coppia di numeri separati da (spazi...))
stampare su schermo la loro differenza
'''

def main():
    with open('listanumeri.txt', 'r') as file:
        for line in file:
            campi = line.strip().split(',')
            differenza = int(campi[0]) - int(campi[1])
            print(differenza)

main()