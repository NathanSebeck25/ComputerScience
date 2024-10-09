# If statements evaluate boolean experssions!
#they make decisions about which code to run next 

# Take a temperature
#print <temp> is "hot" if its >=80 
#otherwise print "<temp> is not hot"
temp = input("What is the temperature in F?\n:")
temp = int(temp)

# If is a keyword like, def, else, and return
#if <boolean expresion> :
#should be simaler to a function
# def <name>():
if temp >= 80:
    print(str(temp) + "° is hot!")

if temp < 80:
    print(str(temp) + "° is hot not hot...")

else: #else requires a if statement "Otherwise..."
    print(str(temp) + "° is hot not hot...")

#No if statements REQUIRE else statments they are optinal. 
#but ALL else satements REQIRE a If statement 
# an if statement can only have one else statement 


# creaate a program that asks for a password 
# if correct print acces granted
#otherwise print acces denied 
# passowrd = skibidi 68.9
real_pass="skibidi68.9:"
input_pass = input("What is the password?\n:")
if input_pass == real_pass:
    print("Access Granted")
else:
    print("Access Denied")


#Activity 2, electric boogaloo
#EZ

Q1= input("What is 5 == too?\n:")
if Q1 =="five" or "5" or "Five":
    print("Correct")
else:
    print("inncorect")





print("Give all answers in integer form.") #basic instructions
tally=0
answer_1 = int(input("Give a whole number that is less than 18.\n:")) #the bascic function for the question renced and repedted  
if answer_1 < 18:
   print("Correct")
   print(answer_1 < 18)
   tally+=1
else:
    print("Inncorect")

answer_2 = int(input("Give a whole number that is less than 27.\n:"))
if answer_2 < 26:
    print("Correct")
    print(answer_2 < 27)
    tally= tally+1
else:
    print("Inncorect")

answer_3 = int(input("Give a whole number that is greater than 5.\n:"))
if answer_3 > 5:
    print("Correct")
    print(answer_3 > 5)
    tally+=1
else:
    print("Inncorect")

answer_4 = int(input("Give a whole number that is greater than 78.\n:"))
if answer_4 > 78:
    print("Correct")
    print(answer_4 > 78)
    tally+=1
else:
    print("Inncorect")

answer_5 = int(input("Give a number that is equal to 7.\n:"))
if answer_5 == 7:
    print("Correct")
    print(answer_5 == 7)
    tally+=1
else:
    print("Inncorect")

print(tally) #final answer 



#String functions 
# String functions are functions that modify Strings

#.lower() changes the string to uppercase

#.upper() changes the string to uppercase

#.capitalize() changes the entire string to lowercase, then capitalizes the first letter
#"hello world"> "Hello world"

#.title() changes the string to titlecase
# "hello world">"Hello World" 

#.swapcase() inverts the capitalazation of each charecter \
#"Hello World">"hELLO wORLD"

x = "Lord of the Rings"
x=x.lower()
print(x)

x = "Lord of the Rings".lower()


input("type y\n:")

