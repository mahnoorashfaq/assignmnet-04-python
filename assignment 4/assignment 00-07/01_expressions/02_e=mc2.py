c : int = 299792458 
def main():
    massInkg: float = float(input("Enter kilos of mass: "))

    energyInJoules: float = massInkg * (c ** 2)

    print("e = m * c^2...")
    print("m = " + str(massInkg) + " kg")
    print("C = " + str(c) + " m/s")

    print(str(energyInJoules) + " Joules of Energy!")

if __name__ == '__main__':
    main()