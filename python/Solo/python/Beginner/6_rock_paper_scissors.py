#rock paper scissors 
#a simple game where the AI asks the users what he chooses and then randomly generate a number which is that of the AI
#rock beats scissor
#scissors beat paper
#paper beats rock

import random


a={1:"rock",2:"scissor",3:"paper"}
user_win_count=0
AI_win_count=0
#THE GAME CONDITIONS
def condition(AI_choice,User_choice):
    print(AI_choice,User_choice)
    #same
    if AI_choice == User_choice:
        print("It is a tie")
    #rock beats scissors
    elif AI_choice==1 and User_choice==2:
        print("AI WINS")
        
    #scissors beats paper
    elif AI_choice==2 and User_choice==3:
        print("AI WINS")
        
    
    #paper beats rock
    elif AI_choice==3 and User_choice==1:
        print("AI WINS")
       
    else:
        print("YOU WIN")
        


#the AI choice
def AI_choice():
    AI=random.randint(1,3)
    return AI

#the users
def main():
    
    
    #if false
    while True:
        print(" ==============================")
        print("\n ---------- THE GAME ----------")
        print(" ==============================")
        print()
        print(" MENU OPTIONS")
        print()    
        for key,val in a.items():
            print(" -> press",key,"for",val)
        print(" -> press 4 to quit")
        b=int(input(" Enter a option:"))
        #user choice
        choice=[]
        
        if b>len(a)+1 or b<1:
            print()
            print(" =====================")
            print(" No option like that please choose it again")
            print(" =====================")
            print()
            
        elif b==4:
            print()
            print(" =====================")
            print(" THANK YOU FOR PLAYING")
            print(" =====================")
            break
        else:
            choice.append(a[b])
            c=AI_choice()
            print("",c,"",choice)
            condition(c,b)


main()