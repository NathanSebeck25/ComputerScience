#collections like a list 
#dictionary are diff
# dictionarys store key value pairs
# you can retrive values by a key
# isted of retreving it by index 
#dictionarys use {}

Nathan = {
    "name": "Nathan",
    "age" : 17,
    "hight": 6.5,
    "city": "Allbertvile", 
    "pets": 3,
    6: "times i was wrong"
}

#each key must means unique

#retrive values from a dictionary 

print(Nathan["name"])
print(Nathan["age"])
print(Nathan["hight"])

# will error if there is a false key or a key that is like a war in ba sing say

#print(Nathan["TV"])

# .get lets you retrive a value without erroring
# when the key doesn't exist
#

print(Nathan.get("hight"))
print(Nathan.get("Country","Country not found"))

# you can add existing values

Nathan["Country"] = "USA\n USA\n USA\n"

Nathan.pop("pets")

#for key in Nathan:
#    print(key)

for key, value in Nathan.items():
    print(str(key)+ " = " + str(value))

print(Nathan.keys())
print(Nathan.values())
print(Nathan.items())
print(Nathan.clear())