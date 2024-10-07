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
Q2=
Q3=
Q4=
Q5=