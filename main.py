import random
n = random.randint(1, 9)
guess = int(input("Enter an integer from 1 to 9: "))
while n != "Guess":
    print
    if guess < n:
      print ("Guess is low")
      guess = int(input("Enter an integer from 1 to 9: "))
      
    elif guess > n:
      print ("Guess is high")
      guess = int(input("Enter an integer from 1 to 9: "))
      
    else:
      print ("you guessed it!")
      break
    print