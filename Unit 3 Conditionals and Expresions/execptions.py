# exeption handaling
# write a program theat asks for two numbers and devides them

# if    = try
#elif   = except with error type
# else  = except
def divide_two_numbers(): 
    try:    # We always enter the try block, there is no condition 
        x = int(input("What is the first number?\n:"))
        y = int(input("What is the second number?\n:"))
        print(x/y)
    except ZeroDivisionError:
        print("Can't divide by zer, try again")
        divide_two_numbers()

    except ValueError:
        print("Please entar a valid numarical sybol, try again\n")
        divide_two_numbers()
    except: # If anything in the try block causes an error,
            # the try block stops immediatly
            # the te exept is ran
            # the rest of the try block never finnishes runing. it's skipped 
            # if the try block executes without an error, the except is skipped
            # the the only way to get into the except is to "throw" an error (threw an error means cause an error)
        print("Invalid input, try again (I have no idea what the heck you did to get here).\n")
        divide_two_numbers()

divide_two_numbers()
