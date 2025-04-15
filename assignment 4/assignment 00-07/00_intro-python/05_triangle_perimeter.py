def main ():
    side01 : float = float(input("What is the lenght of 1 side : "))
    side02 : float = float(input("What is the lenght of 2 side : "))
    side03 : float = float(input("What is the lenght of 3 side : "))

    print("The perimeter of the triangle is " + str(side01 + side02 + side03))

if __name__ == '__main__':
    main()