'''
calcola scomposizione fattori primi di numero intero (n)
8 --> 2, 2, 2
54 -> 2, 3, 3, 3
17 -> 17

1. primes = insieme numeri primi comresi tra 2 e n (incluso)
2. fattori = []
3. finchè n > 1:
    div = cerca divisore di n in primes
    aggiungi div a fattori
    n = n // div
4. stamp/ritorna fattori

numero primo?
1. per tutti i valori tra 2 e n-1
    se valore è divisore di n
        non primo

2. se ho verificato tutti i numeri, il numero è primo


'''
def numeroPrimo(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def fattoriPrimi(valore):
    primes = []
    for n in range(2, valore + 1):
        if numeroPrimo(n):
            primes.append(n)

    fattori = []
    while valore > 1:
        for div in primes:
            if valore % div == 0:
                fattori.append(div)
                valore //= div
                break
    return fattori
    

def main():
    valore = int(input('Inserire valore intero: '))
    fattori = fattoriPrimi(valore)

    print(f'La scoposizione in fattori primi di {valore} è {fattori}')

main()