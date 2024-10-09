# the if statement has two budies 
# the first is else statement
# the second is

x = int(input("type an intager\n:"))

if x > 0: # not every if needs an else 
    print("x is a posative number")

    # the second guy is the elif (esle if)
elif x < 0:
    print("x is a negative number")

else: # else always needs an if 
    print("x is a negative number ")


light = input("What color is the light?\n:")

if light.lower() == "green":
    print("GO")

elif light.lower() == "yellow":
    print("STOP IF SAFE")

elif light.lower() == "red":
    print("STOP")

else:
    print("YEILD")

y = int(input("Input a integer"))

if y > 5:
    print("x is greater thatn 5")
######################################

if y > 8:
    print("x is greater thatn 8")