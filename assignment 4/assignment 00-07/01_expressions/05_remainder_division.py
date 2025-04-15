def main():

    num1: int = int(input("Please enter an number 1 to be divided: "))
    num2: int = int(input("Please enter an number 2 to divide by: "))

    quotient: int = num1 // num2  
    remainder: int = num1 % num2 
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

if __name__ == '__main__':
    main()