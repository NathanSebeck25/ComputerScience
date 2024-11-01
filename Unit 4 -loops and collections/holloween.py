import random
#Python has four types of collections
#Tuple
#set
#>List
#>Dictonary

#Today is about list es
# A list is a way to storre more than one value in a single variable
# the values are called items 
#Items can be access by their INDEX(Position in the list)
#Index                      0                   1           2                   3         4
Best_elden_ring_wapons = ["Blasphemus Blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhound's Fang"]
Best_years = [1776, 1985, 1994, 1957, 2016]

print(Best_years[0])
myint =6-9
print(Best_years[myint])
print(Best_elden_ring_wapons[0])#Print first
print(Best_elden_ring_wapons[4])#print the last?
print(len(Best_elden_ring_wapons))
print(Best_elden_ring_wapons[len(Best_elden_ring_wapons)-1])

#list items can be changed!!!

Best_elden_ring_wapons[3]="Spiked Fist"
print(Best_elden_ring_wapons)


#List functions
# .pop()
    #Remove an item at a given index
Best_elden_ring_wapons.pop(1)
# .remove()
    #Removes an item by value -- removes the first instance of a value
Best_elden_ring_wapons.remove("Blasphemus Blade") #If the value exist, it errors :(
print(Best_elden_ring_wapons)

# .append()
    # Adds a new item at the end of the list
Best_elden_ring_wapons.append("Death's Poker")

Ranints = [random.randint(0,100), random.randint(0,100),   random.randint(0,100),  random.randint(0,100),   random.randint(0,100)]

# .Sort()
Ranints.sort()

# max()
    #Print's max
print(max(Ranints))
# min()
    #prints in number
print(min(Ranints))


#Strings are just Lists of charecters 
print(len("Osowski"))