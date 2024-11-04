# for loops
# is big deal 
# allows for programers to repeat or what we call loop

# Write a program that lists numbers 1-10 each on a new line

for i in range(90,101):
    print(i)

Fav_foods = ["Burger", "Pizza", "ice cream", "Krusty Crab pizza" ]

for food in Fav_foods:
    print(food)
    #Runs all of the lines inside the for loop
    #When it reaches the bottom the list, it runs again
    #and moves on to the nest item in the list
    #It ends when there are no list items left 
#for <var> in <List> 

# print a countdown: Create a countdown from 10-1 useing a for loop 

for i in range(10,0,-1):# Start , Stop , Step
    print(i)


#Sum of a list
numbers = [68,70,419,421,665]
sum = 0
for n in numbers:
    sum = sum + n
    
print(sum)

#Square of each Number 

ints = [3,2,5,4,1]
newlist = []

for i in ints:
    newlist.append(i*i)

print(newlist)

#Car  Count 

stringy = input("Please enter a string\n:")
numvowels = 0
for s in stringy:

    if s.lower() in {"a","e","i","o","u"}:
        numvowels = numvowels +1

print(numvowels)



#Print multiuplacation table

try:
    multi = int(input("Give an integer\n:"))

except:
    print("WOMP WOMP MF DOOM")
n = 0
for i in range(0,multi+1):
    print(str(multi) + " x " + str(i) + " = " + str(multi*i))

names = ["Peter", "John", "Paul", "Luke"]
for name in names:
    print("Hello, " + name + "!")

    import random
multi = random.randint(0,69999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
n = 0
for i in range(0,multi+1):
    print(str(multi) + " x " + str(i) + " = " + str(multi*i))

    