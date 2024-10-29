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
    Top_champ = input("What champ are you going to play Naut, Sett, Mord(please answer with one of the listed champs in that format)\n:").lower()
    #Naut = Ad, Ap, Hp_tank, Resistance_tanks
    #Sett = Ad, Hp_tank
    #Mord = Ap, Resistance_tanks
    if Top_champ == "mord":
        print("You picked Mordakiser a " + Ap + "or " + Resistance_tanks + "bassed champ." )
        "mord" == Ap_champs and Resistance_tanks
        Player_char=="mord"
        "mord"
        
    elif Top_champ == "sett":
        print("You picked Sett a " + Ad + "or " + Hp_tank + "bassed champ.")
        "sett" == Ad_champs and Hp_champs
        Player_char == "sett"
    elif Top_champ == "naut":
        print("Nautales is a "  + Hp_tank + "or " + Resistance_tanks + "bassed champ.")
        "naut" == Hp_champs and Resistance_champs
        Player_char == "naut"
        
    else:
        print("You need to fix yourself.\n Try again.")
        Top_champs()

def Mid_champs():
    global Player_char
    Mid_champ = input("What champ are you going to play Diana, Xerath, Smolder(please answer with one of the listed champs in that format)\n:").lower()

    if Mid_champ == "diana":
        print("You picked Diana an " + Ap + " bassed champion")
        "diana" == Ap_champs
        Player_char == "dianna"

    elif Mid_champ == "xerath":
        print("You picked Xerath an" + Ap + " bassed champion")
        "xerath" == Ap_champs
        Player_char == "xerath"
    
    elif Mid_champ == "smolder":
        print("You picked Smolder an" + Ad + " bassed champion")
        "smolder" == Ad_champs
        Player_char == "smolder"
    else:
        print("You need to fix yourself.\n Try again.")
        Mid_champs()

def Bot_champs():
    Bot_champ = input("What champ are you going to play Smolder, Jhin, Senna (please answer with one of the listed champs in that format)\n:").lower()

    if Bot_champ == "smolder":
        print("You picked Smolder an " + Ad + " bassed champion")
        "smolder" == Ad_champs
        Player_char == "smolder"
    
    elif Bot_champ == "jhin":
        print("You picked Jhin an " + Ad + " bassed champion")
        "jhin" == Ad_champs
        Player_char == "jhin"
    elif Bot_champ == "senna":
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
              "You have gained knolage from this encounter you get a +1")
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





start()
item_select()
Minnion_wave_1()
Minnion_wave_2()