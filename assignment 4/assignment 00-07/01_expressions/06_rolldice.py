import random

num_sides:int = 6

def main():
   die1: int = random.randint(1, num_sides)
   die2: int = random.randint(1, num_sides)

   total: int = die1 + die2
   print ("Dice have" , num_sides , "each sides")
   print ("First die", die1)
   print ("Second die", die2)
   print ("Total die" , total)

if __name__ == '__main__':
    main()
