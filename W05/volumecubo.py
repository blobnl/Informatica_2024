

def main():
    lato = float(input("Lato cubo: "))
    volCubo = volumeCubo(lato)
    print(f'Il volume del cubo di lato {lato} è {volCubo}')

def volumeCubo(latoCubo):
    # corpo fx
    if latoCubo < 0:
        return 0
    else:
        volume = latoCubo ** 3
        return volume


main()