'''
scrivere un programma che sia ingrado di fare la conversione in ca2
su 8 bit di un numero letto da tastiera

1. coversione in binario buro
2. se numero è negativo
    compelemento a 1 dei bit
    aggiugo 1

'''

BITS = 8

def num2bin(numero):
    binario = [0] * BITS
    idx = -1
    while numero > 0:
        bit = numero % 2
        numero //= 2
        binario[idx] = bit
        idx -= 1

    return binario

def ca2(numero):
    # 1. conversione in binario puro

    binario = num2bin(abs(numero))
    # 2 se il numero è negativo:
    if numero < 0:
        # ompelemnto a 1
        for i in range(BITS):
            binario[i] = 1 - binario[i]

        # somma 1
        
        carry = 1
        for idx in range(BITS-1, -1, -1):
            if binario[idx] == 1 and carry == 1:
                binario[idx] = 0
            else:
                binario[idx] += carry
                carry = 0


        '''
        carry = 0
        for i in range(BITS -1, -1, -1):
            if i == BITS - 1:
                if binario[i] == 1:
                    # 1 + 1 = 1 carry 1
                    binario[i] = 0
                    carry = 1
                else:
                    # 1 + 0 = 1 carry 0
                    binario[i] = 1
                    carry = 0
            else:
                if binario[i] == 1 and carry == 1:
                    binario[i] = 0
                    carry = 1
                else:

                    binario[i] += carry
                    carry = 0
        '''


    return binario

    # 1 conversione in binario puro

def bin2str(binario):
    stringa = ''
    for val in binario:
        stringa += str(val)

    return stringa

def main():
    numero = int(input('Inserire un numero: '))
    binario = ca2(numero)
    print(bin2str(binario))

main()    
