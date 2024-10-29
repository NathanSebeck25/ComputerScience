# Asking what lane they want to play 
import random
Ap  = "Abilitys and/or spells "
Hp_tank    = "Health Points "
Resistance_tanks = "Arrmor or Magic Resistance "
Ad  = "Attacks "
Ap_champs = 1
Ad_champs = 1
Resistance_champs = 1
Hp_champs = 1
Player_char = 1
def start():
    play_the_game=input("Do you wish to enter the Arena Yes or No(please input y or n )\n:").lower()
    if play_the_game == "y":
         start1 = input("What type do you want to play top(tankyer), more magic or ability(type ap for this one), or more attack?(please answer with one of the listed types)\n:").lower()
         if start1 == "Tankyer":
                Top_champs()
         elif start1 == "ap":
                Mid_champs()
         elif start1 == "more attack":
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
    #Nautaless = Hp_tank, Resistance_tanks
    #Sett = Ad, Hp_tank
    #Mordakiser = Ap, Resistance_tanks
    #Diana = ap 
    #Xerath = ap
    #Smolder = ad 
    #Jhin = ad
    #Senna = ad
    #Below functions are for different champs
def Top_champs(): 
    global Player_char
    Champ = input("What champ are you going to play Naut, Sett, Mord(please answer with one of the listed champs in that format)\n:").lower()
    #Naut = Ad, Ap, Hp_tank, Resistance_tanks
    #Sett = Ad, Hp_tank
    #Mord = Ap, Resistance_tanks
    if Champ == "mord":
        print("You picked Mordakiser a " + Ap + "or " + Resistance_tanks + "bassed champ." )
        "mord" == Ap_champs and Resistance_tanks
        Player_char=="mord"
        "mord"
        
    elif Champ == "sett":
        print("You picked Sett a " + Ad + "or " + Hp_tank + "bassed champ.")
        "sett" == Ad_champs and Hp_champs
        Player_char == "sett"
    elif Champ == "naut":
        print("Nautales is a "  + Hp_tank + "or " + Resistance_tanks + "bassed champ.")
        "naut" == Hp_champs and Resistance_champs
        Player_char == "naut"
        
    else:
        print("You need to fix yourself.\n Try again.")
        Top_champs()

def Mid_champs():
    global Player_char
    Champ = input("What champ are you going to play Diana, Xerath, Smolder(please answer with one of the listed champs in that format)\n:").lower()
    
    if Champ == "diana":
        print("You picked Diana an " + Ap + " bassed champion")
        "diana" == Ap_champs
        Player_char == "dianna"

    elif Champ == "xerath":
        print("You picked Xerath an" + Ap + " bassed champion")
        "xerath" == Ap_champs
        Player_char == "xerath"
    
    elif Champ == "smolder":
        print("You picked Smolder an" + Ad + " bassed champion")
        "smolder" == Ad_champs
        Player_char == "smolder"
    else:
        print("You need to fix yourself.\n Try again.")
        Mid_champs()

def Bot_champs():
    global Champ
    Champ = input("What champ are you going to play Smolder, Jhin, Senna (please answer with one of the listed champs in that format)\n:").lower()

    if Champ == "smolder":
        print("You picked Smolder an " + Ad + " bassed champion")
        "smolder" == Ad_champs
        Player_char == "smolder"
    
    elif Champ == "jhin":
        print("You picked Jhin an " + Ad + " bassed champion")
        "jhin" == Ad_champs
        Player_char == "jhin"
    elif Champ == "senna":
        print("You picked Senna an " + Ad + " or " + Ap + " bassed champion")
        "senna" == Ad_champs and Ap_champs
        Player_char == "senna"
    else:
        print("You need to fix yourself.\n Try again.")
        Bot_champs()
#this it to save changes
def Minnion_wave_1():
    global Player_char
    Minnion_wave_options_1 = input("You have spawed in the battle area and enter right by what you assume to be your Gaurdian/Sentinal being and it tells you\n 'You have three options to continue'\n"
          +"Option 1\nYou can leave but that will not end well\n\n Option 2 you can clear that aproching wave of ghouls\n\n" 
          + "Option 3 you will let your own wave of Skeletons to clear it for you\n\n 'So which will it be'\n(pleas answer options as 1, 2, or 3.)" ).lower()
    if Minnion_wave_options_1 == "1":
        print("Mr.Burns from the Simpsons was watching from affar and got upset with you he has released the hounds.\n (you suck at this)")
    elif Minnion_wave_options_1 == "2":
        print("The Sentinal watches as you clear the minnion wave with ease quite frankly he is shoked by it the sentinal gives you a potion that gives you a +1 on top of the experience that you gained")
        Player_char =+2

    elif Minnion_wave_options_1 == "3":
        print("The ghouls and skeletons start brwaling in the middle and you 'Bark' comands at the Skeletons they semingly understand push through the wave leaving a few surounding you.\n"+
              "You have gained knolage from this encounter you get a +1 you also hear a bunch of poor taste jokes about bones")
        Player_char=+1
    else:
         print("Mr.Burns from the Simpsons was watching from affar and got upset with you he has released the hounds.\n (you suck at this)")
def Minnion_wave_2():
    global Player_char
    Minnion_wave_options_2 =input("In the distance you see the next wave of ghouls approaching. You turn around and see the next wave of skeletons aproaching. You assume your choices are the same as before so you chose option 1, 2, or 3?\n").lower()
    if Minnion_wave_options_2 == "1":
        print("Mr.Burns from the Simpsons was watching from affar and got upset with you he has released the hounds.\n (you suck at this)")
    elif Minnion_wave_options_2 == "2" or Minnion_wave_options_2 == "3":
        print("You approach the enemy wave and with your extra numbers you reach the choke point in front of the enemy sentinal quite esally ")
        Player_char =+1
    else:
        print("I dont like you any more now leave")
def Enemy_sentinal():
    global Player_char
    Enemy_sentinal_interaction = input("As you turn the corner you see the opposing Sentinal.\n your Skeletons start attacking it and you can see the they wont be able to take the sentinal down without your help So do you?(Y or N)").lower()
    if Enemy_sentinal_interaction == "y" and Player_char > 4:
        print("You slay the oposing Sentinal with the help of your Skeletons and you feal as if you could slay a god and with that you see the rest of the sentinals down this road or lane if you could call it that " +
              "Crash down and turn to what looks like ruble. You see the next wave of ghouls stop and turn into lights accross the wall and your skeletons do the same along your side")
        Player_char +=55
    elif Enemy_sentinal_interaction == "y" and Player_char <= 3:
        print("As you run up to attack the Sentinal you get feal and hear a thwunk and you get smaked into a wall giveing you a sevire Tua Tagoviloa. This leads to you being sidelined for "
              +"the rest of the game you are now T.K.OD.")
    else:
        print("Are you reallly denser than Osmium you {insert random gordon ramsey quote}.\n You don't dessirve to try agin over this are you kiding me.")


def John_bbeg():
    global Player_char 
    if Player_char >= 20:
        print("You walk to the enemy base you feal your mind breack and shater and then put it's self back together.\n"
              +"you walk up futher twards the light and you see a glowing throne and a lare being of in consrehencible strength.")
    else:
        print("You feal an Aura that is so overwhelming your mind just pops")
#############################################################           The rest of this is "Fluff" to make the story more intertaning          ########################################
def The_desent():
    yes_or_no =input("As yo dessend into this structure you hear 'Elevator music' do you leave it on or turn it off ( Type Off or On)\n ").lower()
    if yes_or_no == "Off":
        y_or_n = input("Are you sure(Y or N)").lower()
        if y_or_n == "y":
            print("You win this is only one of the 2 good endings as you stoped this annoying music.")
        else:
            print("Thank you for listesning to the music ")
    else:
        print("Thank you for listesning to the music ")

def The_walk():
    print("As you march through the lands to get to the arena you hear music.")
    sirens = input("Do you 1. Go twards the music or 2. keep walking forewards(type 1 or 2)\n ")
    if sirens == "1":
        print("You aboslute bofon you never go twards music it is always a trap or scam. Do i need to get you a coipy of Adventuring for dumies.")
    elif sirens == "2":
        print("Wow you made the smart and educated deccision.\n You aproach a tomb or enterance of a biulding ")
def The_telaporter():
    telaporter = input("As you enter this biulding you see a 'Telaporter' you can either 1. Go down or 2. Stay upstairs")
    if telaporter =="1." or telaporter =="1":
        print("You push the button to go down the elevator it's just an elavator.")
    else:
        print("I mean you decided to not go down the elavator this is your own fault and out of my hands.\n You see a screen turn on and some creepy doll say let's play a game.")

def Skeletor_jokes():
    print("you read a sigh on the elavator that says your 'Minnions' will be makeing jokes espesially if you have the skeletons")
    jokes = input("Do you want skeletons Y or N").lower()
    if jokes == "y":
        print("Bad dessision but ok")
    else:
        print(" I gave you the illusion of choice so no you dont get to pick option 2")
start()
item_select()
The_walk()
The_telaporter()
The_desent()
Skeletor_jokes()
Minnion_wave_1()
Minnion_wave_2()
Enemy_sentinal()
John_bbeg()
#put this here to save stuff 
