'''

Author: Nirmith Victor D'Almeida
Instagram: @jay_codes_

'''


#use of multiple if statements and functions
#plot: we will do a horror run themed story of a boy escaping a ghoul

#join the wizard armed and dangerous
def wizard_armed():
    sheild=1
    sword=1
    print('\n')
    print("YOU DECIDED TO JOIN THE WIZARD AND THEN YOU ARRIVE AT A TREE THAT SEEMS OUT OF THE WORLD")
    print("THE WIZARD SUGGESTS TO EAT THE FRUIT OF THE TREE. DO YOU TAKE THE FRUIT (y/n)?")
    a=input()
    if a.lower()=="y":
        print("YOU ENTER A DEEP SLUMBER AND YOU SEE A VISION OF A FLOWER QUITE UNSUAL BUT BEAUTIFUL")
        print("YOU WAKE UP AND SEE THE WIZARD NEXT TO YOU TO HAVE DISAPPEARED BUT LEFT BEHIND A NOTE SAYING WHERE TO FIND THE FLOWER... DO YOU TAKE IT (y/n)?")
        b=input()
        if b.lower()=="y":
            print("YOU READ OUT THE WORDS AND TELEPORT TO A FAMILIAR PLACE AND YOU REALIZE THAT IT IS YOUR OLD HOME AND YOU FIND THE FLOWER")
            print('\n')
            print("DO YOU TAKE IT (y/n)")
            c=input()
            if c.lower()=="y":
                print("THE GHOUL APPEARS OUT OF THE NO WHERE AND STANDS BEFORE YOU HOLDING OUT THE FLOWER THE GHOUL TAKES IT AND TURNS AROUND DO YOU STAB IT IN THE BACK(Y/N)")
                d=input()
                if d.lower()=="y":
                    print("THE GHOUL WAS HURT AND TURNED AROUND KILLING YOU!!!")
                    print("\n==================THE END=================\n")
                else:
                    print("THE GHOUL TURNS BACK AND TRANSFORMS INTO A BEAUTIFUL WOMAN THAT YOU TAKE AS YOUR WIFE\n")
                    print("\n==================THE END=================\n")
            else:
                print("THE GHOUL APPEARS OUT OF NO WHERE AND YOU TRY TO DEFEND YOURSELF BUT THE GHOUL ENDS UP KILLING YOU\n")
        else:
            print("YOU DISREGARD THE NOTE AND KEEP RUNNING TILL THE END OF YOUR DAYS\n")
            print("\n==================THE END=================\n")
    else:
        print("YOU TAKE OUT YOUR DAGGER AND STAB THE WIZARD WHICH ANGERS HIM AND ENDS UP KILLING YOU")
        print("YOU INFLICTED A HEAVY INJURY ON THE WIZARD WHO SPENT HIS LAST FEW MOMENTS CRYING FOR YOU")
        print("\n==================THE END=================\n")


#not join the wizard but armed and dangerous
def notwizard_armed():
    print("OUT OF FEAR YOU STAB THE WIZARD AND RUN AWAY FROM HIM\n")
    print("THE WOUNDED WIZARD SCREAMT OUT AND YELLED OUT AFTER YOU AND YOU PAUSE IN YOUR STEPS.  DO YOU ACCEPT HIS WORDS (y/n)?")
    a=input()
    if a.lower()=="y":
        print("YOU HEAR AND REMEMBER THE WORDS AND WHEN YOU STOP FOR A QUICCK RESPITE AND REMEMBER THAT THE WIZARD DIRECTED HIM TO THE FLOWER TO DEFEAT THE GHOUL")
        print("YOU GO AFTER THE FLOWER AND GETS JUMPED BY THE GHOUL YOU TWIST AND TURN AND DODGE ALL OF ITS ATTACKS AND REACH THE FLOWER DO YOU TAKE IT (y/n)?")
        b=input()
        if b.lower()=="y":
            print("YOU OFFERED THE FLOWER TO THE GHOUL AND IT DISAPPEARED\n")
            print("\n==================THE END=================\n")
        else:
            print("YOU TOOK OUT YOUR DAGGER AND PLUNGED IT DEEP INTO THE GHOULS HEART AND THE GHOUL VANISHED\n")
            print("\n==================THE END=================\n")
    else:
        print("YOU SPENT THE REST OF YOUR DAYS RUNNING TILL THE END OF TIME\n")
        print("\n==================THE END=================\n")


#WIZARD BUT YOU ARE UNARMED
def wizard_unarmed():
    print("\n===================================\n")
    print("YOU FOLLOWED THE WIZARD THROUGH JUNGLES AND CAME ACROSS AN ABADONED HOUSE")
    print("THE WIZARD INDICATED TO YOU A BOX AND YOU OPENED AND SAW A GOLDEN CASKET")
    print("IN IT YOU SAW A FLOWER AND A NOTE THAT SAID 'IN DARKNESS SHALL IT BLOOM BRIGHT' ")
    print("YOU TURNED AROUND TO ASK THE WIZARD WHAT IT MEANT BUT HE WAS GONE LEAVING BEHIND A LITTLE BIRD")
    print("YOU GO OUTSIDE AND SEE THAT THE GHOUL IS WAITING OUT THERE SHARPENING HIS NAILS WAITING")
    print("DO YOU OFFER THE FLOWER (y/n)?")
    a=input()
    if a.lower()=="y":
        print("GHOUL IS SURPRISED AND ACCEPTS THE FLOWER ON ONE CONDITION THAT YOU LEAVE AND NEVER RETURN")
        print("\n===================THE END==================\n")
    else:
        print("YOU TRIED TO RUN AWAY BUT WAS STOPPED WITH A SHARP STAB TO THE CHEST THE GHOUL LIFTED YOU AND MADE YOU ITS LUNCH")
        print("\n===================THE END==================\n")



#NO TO WIZARD AND YOU ARE UNARMED
def notwizard_unarmed():
    print("YOU RUN AWAY FROM HIM AND FALL INTO A DITCH\n")
    print("YOU START SCREAMING FOR HELP AND WIZARD COMES AND OFFERS HELP DO YPU ACCEPT IT (y/n)?")
    a=input()
    print("IN THERE YOU FOUND AN OLD SWORD DO YOU TAKE IT (y/n)?\n")
    b=input()
    if a.lower()=="y":
        wizard_unarmed()
    elif a.lower()=="y" and b.lower()=="y":
        wizard_armed()
    else:
        print("YOU WERE DRAGGED OUT OF THE DITCH BY FORCE AND TAKEN INTO THE CUSTODY OF THE WIZARD")
        wizard_unarmed()
        


#armed guy plot
#after armed ask user if he wants to defend himself or drop 
def armed(sheild,sword):
    if(sheild and sword):
        print("YOU ARE ARMED")
        print("\n")
        print("WOULD YOU LIKE TO DISARM Y'SELF (y/n)?")
        a=input()
        if a=="y":
            print("\n")
            print("YOU HAVE DROPPED A DAGGER AND SHEILD")
            print("=================\n")
            sword=0
            sheild=0
            unarmed()
        else:
            print("\n")
            print("YOU COME ACROSS A BUNCH OF SOLDIERS IN DEFENSIVE POSITION WOULD YOU GO TO THEM (y/n)?")
            a=input()
            if a=="y":
                print("\n")
                print("YOU HAVE A DAGGER AND SHEILD")
                print("=================\n")
                sword=1
                sheild=1
                print("SUDDENLY THE GHOUL COMES AND STARTS ATTACKING THE TROOPS\n")
                print("A MAGE COMES OUT OF NO WHERE AND ASKS YOU TO JOIN HIM.  DO YOU TAKE HIS OFFER (y/n)?")
                b=input()
                if b=="y":
                    wizard_armed()
                else:
                    notwizard_armed()
            else:
                print("YOU KEEP RUNNING TILL THE END OF TIME")


#unarmed plot
#if unarmed the user comes across a bunch of soldiers and gets asked to join the mage

def unarmed():
    print("\n")
    print("YOU KEEP RUNNING AND COME ACROSS A BUNCH OF ABANDONED BUILDINGS DO YOU TAKE REFUGE (y/n)")
    a=input()
    if a=="y":
        print("\n")
        print("YOU HIDE BEHIND IN A ABANDONED HOUSE AND SEE AN UNUSUAL CASKET WHICH WAS OPENED AND IN IT WAS A MESSAGE ADRESSED TO HI ON HOW TO DEFEAT THE GHOUL")
        print("SURPRSIED BY THIS ALL OF A SUDDEN YOU HEAR A VOICE WHICH STARTLES YOU AND YOU TURN AROUND AND SEE A OLD MAN SMOKING A WEED PIPE AND STATING THAT YOU ARE THE SON OF THE PROPEHCY FORETOLD MEANT TO DESTROY THE GHOUL AND SAVE EVERYONE")
        print("HE ASKS YOU TO JOIN HIM DO YOU (y/n)?")
        a=input()
        
        if a=="y":
            wizard_unarmed()
        else:
            notwizard_unarmed()



        
        


def main():
    print("=================\n")
    print("YOU ARE A WAR-BOY IN A WAR TORN VILLAGE RUNNING AWAY FROM THE GHOUL KILLING YOUR VILLAGERS ONE BY ONE")
    print("=================\n")

    print("YOU COME ACROSS A FALLEN SOLDIER'S BODY AND FIND A SHIELD AND A DAGGER DO YOU PICK THEM UP (y/n)?")
    a=input()

    #armed
    if a=="y":
        print("\n")
        print("YOU HAVE A DAGGER AND SHEILD")
        print("=================\n")
        sword=1
        sheild=1
        armed(sheild,sword)


    #defenceless
    elif a=="n":
        print("\n")
        print("YOU CONTINUE TO RUN")
        print("=================\n")
        unarmed()
       

main() 
