#Gary Reed -2022 - Addition Subtraction with menu
import random
def menu():
  print("  Menu")
  print("1 Addition")
  print("2 Subtraction")
  choice=input("\nEnter 1 or 2: ")
  if int(choice)==1:
    addit()
  if int(choice)==2:
    subit()

def addit():
  x=(random.randint(5,20))
  y=(random.randint(5,20))
  z=x+y
  answ=int(input("\nWhats is "+str(x)+ " add "+str(y)+"? "))
  if answ==z:
    print("\nThe correct answer is "+str(z)+" and you answered "+str(answ)+"\nWell done! You got it right!")
  if answ!=z:
    print("\nThe correct answer is "+str(z)+" and you answered "+str(answ)+"\nOh dear! That was a bit rubbish!")
  again=input("\nAnother go? y/n ")
  if again=="y" or again=="Y":
    addit()
  else:
    menu()
def subit():
  x=(random.randint(25,50))
  y=(random.randint(1,25))
  z=x-y
  answ=int(input("\nWhats is "+str(x)+ " minus "+str(y)+"? "))
  if answ==z:
    print("\nThe correct answer is "+str(z)+" and you answered "+str(answ)+"\nWell done! You got it right!")
  if answ!=z:
    print("\nThe correct answer is "+str(z)+" and you answered "+str(answ)+"\nOh dear! That was a bit rubbish!")
  again=input("\nAnother go? y/n ")
  if again=="y" or again=="Y":
    subit()
  else:
    menu()

menu()





