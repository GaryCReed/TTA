#Gary Reed - 2022 - Random Lib Example
import random
print("Welcome to Guess a Number Between 1 and 10\n")
num=(random.randint(1,10))
print(num)
guess=6
ans=0
while guess>0 and num!=ans:
  ans=int(input("\nEnter a guess: "))
  guess=guess-1
  if ans>num:
    print("No! Thats too high!")
  elif ans<num:
    print("No! Thats too low !")
  if ans==num:
    print("Well Done Thats Correct")
  elif guess==0:
    print("\nNo more guesses left!")