#this is a random number generator game which basically hopes that the user guesses the number and gives the user the message if he is closer
#or farther or if he is on point if it is ask the user to start again or exit
import random
a=random.randint(0,100)
b=int(input("Enter a number: "))

while(True):
    if a<b:
        print("TOO HIGH MATE")
        print("=================\n")
        b=int(input("Enter a number: "))

    elif a==b:
        print("ON POINT MATE") 
        print("=================\n")
        break

    else:
        print("TOO LOW")
        print("=================\n")
        b=int(input("Enter a number: "))