import csv

def main():
    nazioni = []
    with open('paesi.txt', 'r') as file:
        for line in file:
            parti = line.strip().split(':')
            record = {
                'paese': parti[0],
                'popolazione': int(parti[1])
            }
            nazioni.append(record)

    # uso di dictreader
    nazDR = []
    with open('paesi.txt', 'r') as file:
        reader = csv.DictReader(file, 
                    fieldnames = ['paese', 'popolazione'], delimiter = ':')
        
        for record in reader:
            #print(record)
            nazDR.append(record)

    print(nazDR)


main()