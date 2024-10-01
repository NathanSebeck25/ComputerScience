# 2 basic functions 
# You know something is a function because it has ()
#peramiters are information the function need to run
# i say jump you say how high. how high is hte paeramiter 
print("Hello World")#Hello World is the peramiter
input("What is your favorite animal\n: ")
#\n is called an escape charecter [a line break]
# input is nerver required unless specified

#varyables
# varieables are a way to store data for latter use in th program 
# syntax = grammer
#<name> = <value>
x=5 # x= th variable, 5 is the value 
#Snake case is a nameing convention all lowercase and _ are used for sapaces
#Concise: short and descriptive
username= "Nathan" #define string - string of charecters
fav_animal= "snake" #define string
total_accesaries = 3  # ddefine int whole numbers
percentcomplete = 17.45#~#% Define float decimal - numbers
is_cool = True #define boolean T/F values 
first_letter = "c" # define charecter single keyborad symbol 

total_accesaries = 1 


#arethmatic opperatiers (sounds scary is just basic math)
#   +   -     -   /     **  %    //
print(2+2)
print("2" + "2")
print("cat" + "dog") #is "catdog"
print("cat" + 3)  #error use = for string and int 
print("cat"*3) #catcatcat
print("cat"*"dog") #error cannot use * nor string and string

my_cayable = 2+3 # Arithmatic opreations can be done anywhere 

# make working programs add two numbers using input

x = (input("what is x/\n:")) #input allways returns a string even if you input a integer

y = (input("what is y?\n:"))

#x = int(input("what is x/\n:")) #input allways returns a string even if you input a integer

#y = int(input("what is y?\n:"))
x=int(x) #changeing x and y to a int 
y=int(y)

print(x+y)
#print(int(x)+int(y))

#2 convert to celcius 
#temp_calcius = 49
temp_celcius = input("What is the temp in C?\n:")
temp_celcius = int(temp_celcius)
temp_farenhight = (temp_celcius * 1.8) +32

print(temp_celcius + "° C is " + temp_farenhight +"° F")


# # chonverion factrs

str()
int()
float()
bool()
bin()

# functions
# functions are simaler to  varyables
# they have names
# Store information
# Variable store a volue, functions store code
# def <name> ():

def potato():
    print("tomato")

potato() # every function call needs parentahtsies ()
    # even if it has no parameters 

def jump(how_high):
    how_high = str(how_high) #converts to string for concatination 
    print("You jumped " + how_high + "inches high.")
    #how_high = str(how_high) #converts to string for concatination 
    jump(50)

#scope
#Global v local
# global is everywhere
#local defined inside of functions
#global can be used anywhere 

todd = "cool guy"

#local varyables exist in the contest they were defined too
def my_function():
    global todd # in this function, is refering to the global version
    smith = "not cool guy"
    todd = "stramge guy" 
    print(todd)  #stange guy 
    print(smith)    # not cool guy 

print(todd) #cool guy 
print(smith) # error: using a local variable ouside of it's area 

# return functions 
# Functions can also return values 
# the value that is returned is sent back to where the function was called
# this is very simaler to how variables work
#the function does it work, and returns an answer back 

def add_two_numbers(x,y,):
    solution = x+y
    return solution 

print(add_two_numbers(10,5))
answer = add_two_numbers(10,16)
print(answer)


# how to import square root
import math

