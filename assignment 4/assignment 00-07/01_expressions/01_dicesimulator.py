import random

number = 6

def rolldice(): 
    die1: int = random.randint(1, number)
    die2: int = random.randint(1, number)
    totaldie: int = die1 + die2
    print("Total of two Dice:", totaldie)

def main():
    die1: int = 10
    print("Die1 in main() starts as: " + str(die1))
    rolldice()
    rolldice()
    rolldice()
    print("Die1 in main() is: " + str(die1))

if __name__ == '__main__':
    main()