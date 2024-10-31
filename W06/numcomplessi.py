def complex(real = 0, imag = 0):
    if real == 0 and imag == 0:
        print("0")
    elif real == 0:
        print(f'{imag}i')
    elif imag == 0:
        print(f'{real}')
    else:
        print(f'{real}{imag:+}i')

def main():
    complex(real = 5)
    complex(imag = 5)
    complex()

main()