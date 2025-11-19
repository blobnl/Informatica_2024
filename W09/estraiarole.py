with open('lyrics.txt', 'r') as file:
    for line in file:
        #line = line.strip()
        #parti = line.split()
        parti = line.strip().split()
        for parola in parti:
            parola = parola.strip('.,;:?!')
            print(parola)
