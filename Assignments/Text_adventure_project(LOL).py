# Asking what lane they want to play 
import random
Ap  = "Abilitys or spells "
Hp_tank    = "Health Points "
Resistance_tanks = "Arrmor or Magic Resistance "
Ad  = "Attacks "
Ap_champs = 1
Ad_champs = 1
Resistance_champs = 1
Hp_champs = 1

def start():
    play_the_game=input("Do you wish to enter the Arena Y or N(please input in that format)\n:").lower()
    if play_the_game == "y":
         start1 = input("What lane type do you want to play top(tankyer), mid(more magic or ability), or bot(more attack)?(please answer with one of the listed roles)\n:").lower()
         if start1 == "top":
                Top_champs()
         elif start1 == "mid":
                Mid_champs()
         elif start1 == "bot":
                Bot_champs()
         else:
                print("try again ok?")
                start()
    else:
        print("Fine you wont enter the arena be that way \n If you want to try agian go restart the program now leave")
    
        #Item select will either make you stronger or change nothing
def  item_select():
    item = input("What item do you want?\n The staff of the ages (an item from an achient civalazation) it boosts your " + Ap +"\n The infinaty edge (A steel browad sword) " + Ad + 
          "\n The helm of Jak (a legendary warrier of the past) it boosts your" + Resistance_tanks+ "\n The Lantern of dispair it's a relic of the elders that heals you and boosts your" + Hp_tank 
          + "\n So which do you chose\n\n please be careful you must type the item you chose as\n [ROA] for the rod of the ages\n[IE] for the infinity edge\n [Jak'sho] for the helm of jak\n or [UND] for the Lantern of dispair?\n:").lower()
    if item == "roa" or item == "[roa]":
        print("You have chosen the Staf of the ages")
        print("You now have better abilitys or spells")
        if Ap :
             print("You are now truly stronger")
             Ap_champs+2
    elif item == "ie" or item == "[ie]":
        print("You have choses the Infinity Edge")
        print("Your attacks are now stronger")
        if Ad :
            print("You are now truly stronger")
            Ad_champs+2
    elif item == "jak'sho" or item == "[jak'sho]":
        print("You have chosen the Helm of jak")
        print("Your now able to take more hit's")
        if Resistance_tanks  :
             print("You are now truly stronger")
             Resistance_champs+2
    elif item == "und" or item == "[und]":
        print("You have chose the Lantern of dispair")
        print("You now gain more life over time and 'regen' in fights")
        if Hp_tank :
             print("You are now truly stronger")
             Hp_champs+2
    else:
        print("I said it onece and im not repeating myself so now game over bo womp")

#List of champs
    #Nautaless = Ad, Ap, Hp_tank, Resistance_tanks
    #Sett = Ad, Hp_tank
    #Mordakiser = Ap, Resistance_tanks
    #Diana = ap 
    #Xerath = ap
    #Smolder = ad 
    #Jhin = ad
    #Senna = ad
    #Below functions are for different champs
def Top_champs(): 
    global Resistance_tanks
    Top_champ = input("What champ are you going to play Naut, Sett, Mord(please answer with one of the listed champs in that format)\n:").lower()
    #Naut = Ad, Ap, Hp_tank, Resistance_tanks
    #Sett = Ad, Hp_tank
    #Mord = Ap, Resistance_tanks
    if Top_champ == "mord":
        print("You picked Mordakiser is a " + Ap + "or " + Resistance_tanks + "bassed champ.\n:" )
        "mord" == Ad_champs and Resistance_tanks
        
    elif Top_champ == "sett":
        print("You picked Sett a " + Ad + "or " + Hp_tank + "bassed champ.")
        "sett" == Ad and Hp_champs
    elif Top_champ == "naut":
        print("Nautales is a "  + Hp_tank + "or " + Resistance_tanks + "bassed champ.")
        "naut" == Hp_champs and Resistance_tanks
        
    else:
        print("You need to fix yourself.\n Try again.")
        Top_champs()

def Mid_champs():

    Mid_champ = input("What champ are you going to play Diana, Xerath, Smolder(please answer with one of the listed champs in that format)\n:").lower()

    if Mid_champ == "diana":
        print("You picked Diana an " + Ap + " bassed champion")
        "diana" == Ap_champs

    elif Mid_champ == "xerath":
        print("You picked Xerath an" + Ap + " bassed champion")
        "xerath" == Ap_champs
    
    elif Mid_champ == "smolder":
        print("You picked Smolder an" + Ad + " bassed champion")
        "smolder" == Ad_champs
    else:
        print("You need to fix yourself.\n Try again.")
        Mid_champs()

def Bot_champs():
    Bot_champ = input("What champ are you going to play Smolder, Jhin, Senna (please answer with one of the listed champs in that format)\n:").lower()

    if Bot_champ == "smolder":
        print("You picked Smolder an " + Ad + " bassed champion")
        "smolder" == Ad_champs
    
    elif Bot_champ == "jhin":
        print("You picked Jhin an " + Ad + " bassed champion")
        "jhin" == Ad_champs
    elif Bot_champ == "senna":
        print("You picked Senna an " + Ad + " or " + Ap + " bassed champion")
        "senna" == Ad_champs and Ap_champs
    else:
        print("You need to fix yourself.\n Try again.")
        Bot_champs()
#this it to save changes
def Minnion_wave_1():
    wave_option_1 = input("You have spawed in the battle area and enter right by what you assume to be your Gaurdian/Sentinal being and it tels you\n 'You have three options to continue'\n"
          +"Option 1\nYou can leave but that will not end well\n\n Option 2 you can clear that aproching wave of ghouls\n\n" 
          + "Option 3 you will let your own wave of Skeletions to clear it for you\n\n 'So which will it be'\n(pleas answer options as 1, 2, or 3.)" ).lower()
    if wave_option_1 == "1":
        print("Mr.Burns from the simpsons was watching from affar and got upset with you he has released the hounds.\n (you suck at this)")
    elif wave_option_1 == "2":
        print("The Sentinal watches as you clear the minnion wave with ease quite frankly he is shoked by it the sentinal gives you a potion that gives you a +1")
        





start()
item_select()