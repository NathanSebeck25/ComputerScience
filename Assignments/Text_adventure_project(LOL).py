# Asking what lane they want to play 
Ap  = "abillity "
Hp_tank    = "Hp or arrmor "
Resistance_tanks = "Arrmor or Magic Resistance "
Ad  = "Attack "
def start():
    start1 = input("What lane type do you mant to play top, mid, or bot?(please answer with one of the listed roles)\n:").lower()
    if start1 == "top":
        Top_champs("kai")
    elif start1 == "mid":
        Mid_champs()
    else:
        print("try again ok?")
        start()
        

#List of champs
    #Nautaless = Ad, Ap, Hp_tank, Resistance_tanks
    #Sett = Ad, Hp_tank
    #Mordakiser = Ap, Resistance_tanks
    #Diana = ap 
    #Xerath = ap
    #Smolder = ad 
    #Jhin = ad
    #Senna = ad
def Top_champs(Top_champ): 
    global Resistance_tanks
    Top_champ = input("What champ are you going to play Naut, Sett, Mord(please answer with one of the listed camp in that fotmat)\n:").lower()
    #Naut = Ad, Ap, Hp_tank, Resistance_tanks
    #Sett = Ad, Hp_tank
    #Mord = Ap, Resistance_tanks
    if Top_champ == "mord":
        print("You picked Mordakiser is a " + Ap + "or " + Resistance_tanks + "bassed champ.\n:" )
    elif Top_champ == "sett":
        print("You picked Sett a " + Ad + "or " + Hp_tank + "bassed champ.")
    elif Top_champ == "naut":
        print("Nautales is a " + Ad + "or " + Ap +  "or " + Hp_tank + "or " + Resistance_tanks + "bassed champ.")
    else:
        print("You need to fix yourself")
        Top_champs()


def Mid_champs(Mid_champ):
    Mid_champ = input("What champ are you going to play Naut, Sett, Mord(please answer with one of the listed camp in that fotmat)\n:").lower()


start()