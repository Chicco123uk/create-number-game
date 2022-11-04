import random
num = random.randint(1, 9)
guess = int(input("Enter an integer from 1 to 9: "))
while num != "Guess":
    print
    if guess < num:
      print ("Guess is low")
      guess = int(input("Enter an integer from 1 to 9: "))
      
    elif guess > num:
      print ("Guess is high")
      guess = int(input("Enter an integer from 1 to 9: "))
      
    else:
      print ("you guessed it!")
      break
    print