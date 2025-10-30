def cubeVolume(sideLength):
    if sideLength <= 0:
        return 0
    volume = sideLength ** 3
    return volume

def main():
    lato = float(input("Inserire lato: "))
    volume = cubeVolume(lato)
    print(f"{lato=} --> {volume=}")

main()