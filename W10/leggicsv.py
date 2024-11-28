from csv import reader, writer

def main():
    dati = []
    '''
    with open('file.csv', 'r') as file:
        for line in file:
            campi = line.strip().split(',')
            #print(campi)
            dati.append(campi)
    '''
    with open('file.csv', 'r') as file:
        csvReader = reader(file)
        next(csvReader)
        for record in csvReader:
            dati.append(record)

    # elaboro i contenuti...
    with open('filout.csv', 'w') as file:
        csvWriter = writer(file, delimiter=';')
        # salva le informazioni...
        csvWriter.writerows(dati)


    print(dati)


main()