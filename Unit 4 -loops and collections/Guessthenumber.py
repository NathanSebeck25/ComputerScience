import random

password = random.randint(0,101)
user_input = ""
while password != user_input:
        user_input = int(input("Input a number from 1-100\n:"))
        if user_input < password:
                print("Higher")
        elif user_input > password:
                print("Lower")
        elif user_input == password: 
               print("Good job ")
        else:
            print("How did you get here?")