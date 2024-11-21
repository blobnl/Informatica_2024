# 1. apertura e chiusura esplicita di file in scrittura

#outfile = open("fileOutput.txt", "w", encoding = "utf-8")
# usare il file in scrittura
#outfile.close()

# apertura 
##with open("fileOutput.txt", "w", encoding = "utf-8") as outfile:
#    print('scrittura del file')

#infile = open('fileInput.txt', 'r', encoding = 'utf-8')
# lettura dati
#infile.close()

with open('fileInput.txt', 'r', encoding = 'utf-8') as infile:
    #testo = infile.read()
    #print(testo)

    #for line in infile:
    #    print(line)

    linea = infile.readline()
    while linea != '':
        print(linea)
        linea = infile.readline()
