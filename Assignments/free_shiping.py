# Create a function called free shiping 
# that tells you if you qualify for free shiping or not
# you only get free shiping if
# you are a Prime memver or if order costs $25
# you are at least 16 years or older or have parent consent
# Yor function should take four paramiters
# prime(bool), cost (float), age (int), consent(bool)
#HINT!
# you can use more thatn on logical operator in a conditional

def Free_shiping(Prime,Cost,Age,Consent):
    Prime = input("Do you have Prime y or n\n:").lower()
    Age = int(input("What is your age?\n:"))
    Consent = input("Do you have parentl or garudian consent? pleas type y or n \n:").lower()
    Cost = int(input("What was the cost of your order?\n"))
    if Prime == "y" and (Age >= 18 or Consent == "y") or Cost >= 25:
        print("You have free shiping.\n")
    else:
        print("You do not have free shiping\n")
Free_shiping("y",0,"y",0,)


# this is without the input functions 
#def Free_shiping(Prime,Cost,Age,Consent):
# if Prime == True and (Age >= 18 or Consent == True) or Cost >= 25:
        # print("You have free shiping.\n")
    # else:
        #print("You do not have free shiping\n")
#Free_shiping(True, 0, True, 0)