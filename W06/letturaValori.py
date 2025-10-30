def readIntUpTo(low, high) :
    value = int(input(f"Enter a value between {low} and {high}: "))
    while value < low or value > high :
        print("Error: value out of range.")
        value = int(input(f"Enter a value between {low} and {high}: "))

    return value


def main():
    ora = readIntUpTo(0, 23)
    minuti = readIntUpTo(0, 59)

main()