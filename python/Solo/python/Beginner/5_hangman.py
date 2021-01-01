'''

author:Nirmith Victor D'Almeida
instagram: 

'''

#this is a hangman game 

import random
import os

#clear the screen if feel necessary

#display hanging device
def print_hangman(values):
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
    print("\t{} {}      | |".format(values[5],values[6]))
    print("\t         | |")
    print("  _______________|_|___")
    print("  `````````````````````")
    print()


#display the hangman when person won
def print_hangman_win():
    print()
    print("\t +--------+")
    print("\t |       | |")
 
    print("\t         | |")
    print("\t O       | |")
    print("\t/|\\      | |")
    print("\t |       | |")
    print("  ______/_\\______|_|___")
    print("  `````````````````````")
    print()

#function to print the word to be guessed
def print_word(values):
    print()
    print("\t", end="")
    for x in values:
        print(x, end="")
    print()

#function to check for the win
def check_win(values):
    for char in values:
        if char == '_':
            return False
    return True 

# Function for each hangman game
def hangman_game(word):
 
 
 
    # Stores the letters to be displayed
    word_display = []
 
    # Stores the correct letters in the word
    correct_letters = []
 
    # Stores the incorrect guesses made by the player
    incorrect = []
 
    # Number of chances (incorrect guesses)
    chances = 0
 
    # Stores the hangman's body values
    hangman_values = ['O','/','|','\\','|','/','\\']
 
    # Stores the hangman's body values to be shown to the player
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
 
    # Loop for creating the display word
    for char in word:
        if char.isalpha():
            word_display.append('_')
            correct_letters.append(char.upper())
        else:
            word_display.append(char)
 
    # Game Loop         
    while True:
 
        # Printing necessary values
        print_hangman(show_hangman_values)
        print_word(word_display)            
        print()
        print("Incorrect characters : ", incorrect)
        print()
 
 
        # Accepting player input
        inp = input("Enter a character = ")
        if len(inp) != 1:
            
            print("Wrong choice!! Try Again")
            continue
 
        # Checking whether it is a alphabet
        if not inp[0].isalpha():
            
            print("Wrong choice!! Try Again")
            continue
 
        # Checking if it already tried before   
        if inp.upper() in incorrect:
            print("Already tried!!")
            continue   
 
        # Incorrect character input 
        if inp.upper() not in correct_letters:
             
            # Adding in the incorrect list
            incorrect.append(inp.upper())
             
            # Updating the hangman display
            show_hangman_values[chances] = hangman_values[chances]
            chances = chances + 1
             
            # Checking if the player lost
            if chances == len(hangman_values):
                print()
                
                print("\tGAME OVER!!!")
                print_hangman(hangman_values)
                print("The word is :", word.upper())
                break
 
        # Correct character input
        else:
 
            # Updating the word display
            for i in range(len(word)):
                if word[i].upper() == inp.upper():
                    word_display[i] = inp.upper()
 
            # Checking if the player won        
            if check_win(word_display):
                
                print("\tCongratulations! ")
                print_hangman_win()
                print("The word is :", word.upper())
                break
     
     
 
if __name__ == "__main__":
 
 
    # Types of categories
    topics = {1: "DC characters", 2:"Marvel characters", 3:"Anime characters"}
 
    # Words in each category
    dataset = {"DC characters":["SUPERMAN", "JOKER", "HARLEY QUINN", "GREEN LANTERN", "FLASH", "WONDER WOMAN", "AQUAMAN", "MARTIAN MANHUNTER", "BATMAN"],\
                 "Marvel characters":["CAPTAIN AMERICA", "IRON MAN", "THANOS", "HAWKEYE", "BLACK PANTHER", "BLACK WIDOW"],
                 "Anime characters":["MONKEY D. LUFFY", "RORONOA ZORO", "LIGHT YAGAMI", "MIDORIYA IZUKU"]
                 }
     
    # The GAME LOOP
    while True:
 
        # Printing the game menu
        print()
        print("-----------------------------------------")
        print("\t\tGAME MENU")
        print("-----------------------------------------")
        for key,value in topics.items():
            print("Press", key, "to select", value)
        print("Press", len(topics)+1, "to quit")    
        print()
         
        # Handling the player category choice
        choice = int(input("Enter your choice = "))
   
 
        # Sanity checks for input
        if choice > len(topics)+1 or choice<1:
         
            print("No such topic!!! Try again.")
            continue   
 
        # The EXIT choice   
        elif choice == len(topics)+1:
            print()
            print("Thank you for playing!")
            break
 
        # The topic chosen
        chosen_topic = topics[choice]
 
        # The word randomly selected
        ran = random.choice(dataset[chosen_topic])
 
        # The overall game function
        hangman_game(ran)
