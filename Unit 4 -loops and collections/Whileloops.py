#There are quite a few types of loops im python
# The for loop lets you iterate through a list
# _great for a set # of times 

# What about an uncerten # of times?
# Entering your password on the first time
# or 1 billion times
# Or anything in between 
import random

real_pass = "ninjalowtaper"
attemps = 0
entered_pass = "" 

while entered_pass != real_pass:
    #Ask for password
    entered_pass = input("Type the password\n:")
    #if attemps <= 5:
    # Check if password is correct
    if entered_pass == real_pass:
            print("Your in")
    else:
            print("Access Denied.\n try again...")
            attemps +=1
            print("Your attemps are at " + str(attemps))
    #else:
        #print("Your cooked")
        
      
    
#print("Welcome!")

#count = 0
#while True:
#    count += random.randint(0,100000000000000000000000000000000000000000000000)
#    print(count)



user_input = ""

while user_input!="exit":
      user_input = input("Enter something!")
      print("Type 'exit' to quit")
      print("You typed " + user_input)
    
print("All done!")