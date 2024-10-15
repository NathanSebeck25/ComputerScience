# convert to nested if statements 


Prime = True
Cost = 20
Age = 17
Consent = False

#if (Prime == True or Cost >= 25) and (Age >= 18 or Consent == True)
if Prime:
    if Age >= 18:
        print("YOU ARE ELLIGABLE FOR FREE SHIPING")
    elif Consent:
        print("YOU ARE ELLIGABLE FOR FREE SHIPING")
    else:
        print("YOU DON'T HAVE FREE SHIPING THAT SUCKS FOR YOU")

elif Consent >= 25:
    if Age >= 18:
        print("YOU ARE ELLIGABLE FOR FREE SHIPING")
    elif Consent:
        print("YOU ARE ELLIGABLE FOR FREE SHIPING")
    else:
        print("YOU DON'T HAVE FREE SHIPING THAT SUCKS FOR YOU")

else:
    print("YOU DON'T HAVE FREE SHIPING THAT SUCKS FOR YOU")

#Decide if we need an umbrella
# you need an umbrella if its raning and you are going outside that day 

raining = input("Is it raining oustide y or n?\n:")

if raining.lower() ==("y"):
    outside = input("Do you plan on going outside y or n ?\n:")
    if outside.lower ==("y"):
        print ("Bring an umbrella")
    else:
        print("No need for an umbrella")
else:
    print("No need for an umbrella")