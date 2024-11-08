#loop control statements
#allow you to change how loops operate
#the let you do diff things or nothings at all
#break
#contune
#pass

#break
# exits a  loop prematurally 
#   (A.K.A before it was supposed to end)
# Program continious where the loop ended 


# exaample

bag_of_fruit = ["apple", "orange", "strawberry", "bug", "kiwi", "watermelon", "mango"]

for fruit in bag_of_fruit:
        if fruit == "bug":
                print("You found a nasty ah bug.........")
                print("You procide to throw up")
                break # the breack ends the loop 
        else:
                print("You ate a "+  fruit)

print("All done!")

#Continuie
#skips current loop 

orders = [15, 30, 35, 23, 100, 3, 10, 22]

#disscout applying thing
# got worms?

for order in orders:
        if order < 20:
            continue
        print("$" + str(order) + " order disscounted 5% to $" +str(order * 0.95))

#pass deos nothing used as a place holder while writeing code 

def enter_forest():
       #smash
       pass
def swim_river():
    pass

def eat_icecream():
       pass

if True:
       pass