def complex(real = 0, img = 0):
    if img == 0:
        print(f"{real}")
    elif real == 0:
        print(f"{img}i")
    else:
        print(f"{real}{img:+}i")

    return

def main():
    complex()
    complex(1)
    complex(img = 5)

main()