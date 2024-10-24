def volumeCubo(latoCubo):
    # corpo fx
    volume = latoCubo ** 3
    return volume
lato = float(input("Lato cubo: "))
volCUbo = volumeCubo(lato)
print(f'Il volume del cubo di lato {lato} è {volCubo}')