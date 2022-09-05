#Password cracker using random
#TTA
#April 2022

import random

print ("\n\t ##### Welcome to the password cracker ####\n")


# taking input from user
user_pass = input("\n\t Please enter your password : ")

# storing letters of the alphabet to 
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z','_','!','@','%','$','1','2','3']

pin=[0,1,2,3,4,5,6,7,8,9]
guess = "" # initializing an empty string


# using while loop to generate many passwords until one of
# them matches user_pass

while (guess != user_pass):
    guess = ""
    # generating random passwords using for loop
    for letter in range(len(user_pass)): # generates the number of characters
        guess_letter = password[random.randint(0, len(password)-1)]
        guess = str(guess_letter) + str(guess) # creates a guess
    # printing guessed passwords
    print(guess)
    
# printing the matched password
print("\n Your password is ",guess)
