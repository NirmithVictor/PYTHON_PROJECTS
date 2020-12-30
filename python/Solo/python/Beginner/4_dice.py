import random
roll=input("WOULD YOU LIKE TO ROLL (y/n)?")
while roll=="y":
    a=random.randint(1,6)
    print(a)
    roll=input("WOULD YOU LIKE TO ROLL (y/n)?")
    
print("THANK YOU!!!")