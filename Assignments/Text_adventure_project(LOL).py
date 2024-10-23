# Asking what lane they want to play 
Ap  = "Abilitys or spells "
Hp_tank    = "Health Points "
Resistance_tanks = "Arrmor or Magic Resistance "
Ad  = "Attacks "
def start():
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
        
def  item_select():
    input("What item do you want?\n The staff of the ages (an item from an achient civalazation) it boosts your " + Ap +"\n The infinaty edge (A steel browad sword) " + Ad + 
          "\n The helm of Jack (a legendary warrier of the past) it boosts your" + Resistance_tanks+ "\n The Lantern of dispair it's a relic of the elders that heals you and boosts your" + Hp_tank 
          + "\n So which do you chose\n (please be careful you must type the item you chose as [roa] for the rod of the ages\n[IE]) for the infinity edge\n [Jak'sho] for the helm of jack\n or [UND] for the Lantern of dispair?\n:").lower()
    if item_select == "roa" or "[roa]":
        print("You now have better abilitys or spells")
    elif item_select == "ie" or "[ie]":


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
    Top_champ = input("What champ are you going to play Naut, Sett, Mord(please answer with one of the listed camp in that format)\n:").lower()
    #Naut = Ad, Ap, Hp_tank, Resistance_tanks
    #Sett = Ad, Hp_tank
    #Mord = Ap, Resistance_tanks
    if Top_champ == "mord":
        print("You picked Mordakiser is a " + Ap + "or " + Resistance_tanks + "bassed champ.\n:" )
    elif Top_champ == "sett":
        print("You picked Sett a " + Ad + "or " + Hp_tank + "bassed champ.")
    elif Top_champ == "naut":
        print("Nautales is a "  + Hp_tank + "or " + Resistance_tanks + "bassed champ.")
    else:
        print("You need to fix yourself.\n Try again.")
        Top_champs("kai")

def Mid_champs():

    Mid_champ = input("What champ are you going to play Diana, Xerath, Smolder(please answer with one of the listed camp in that format)\n:").lower()

    if Mid_champ == "diana":
        print("You picked Diana an " + Ap + " bassed champion")

    elif Mid_champ == "xerath":
        print("You picked Xerath an" + Ap + " bassed champion")
    
    elif Mid_champ == "smolder":
        print("You picked Smolder an" + Ad + " bassed champion")
    else:
        print("You need to fix yourself.\n Try again.")
        Mid_champs("akali")

def Bot_champs():
    Bot_champ = input("What champ are you going to play Smolder, Jhin, Senna (please answer with one of the listed camp in that format)\n:").lower()

    if Bot_champ == "smolder":
        print("You picked Smolder an " + Ad + " bassed champion")
    
    elif Bot_champ == "jhin":
        print("You picked Jhin an " + Ad + " bassed champion")

    elif Bot_champ == "senna":
        print("You picked Senna an " + Ad + " or " + Ap + " bassed champion")
    else:
        print("You need to fix yourself.\n Try again.")
        Bot_champs("vayne")

start()