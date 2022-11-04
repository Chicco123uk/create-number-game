import math
import random

num = 0

def generate_random_number():
  math.random()
  print(random.randint(1,9))


def difference_from_answer(guess,answer):
  answer = generate_random_number()
  guess = int(input("Input a number 1 to 9"))
  if guess == answer:
    print("Correct")
  if guess < answer:
    print("Too Low")
  else:
    print("Too High")