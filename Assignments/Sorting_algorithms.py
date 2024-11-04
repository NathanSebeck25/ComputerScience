#gets random from narnia
import random
# generates list
a = random.randint(0,101)
b = random.randint(0,101)
c = random.randint(0,101)
d = random.randint(0,101)
e = random.randint(0,101)
Int_list = [a ,b ,c ,d ,e]
print(Int_list)
def Bub_sort(n):#Take list as a peramitor

    global Int_list
    n = Int_list
    steps = 0
    for j in range(0,len(n)-1):
    #iterate through every item in the list
        for i in range (0,len(n)-1):
        
            if n[i]> n[i+1]:
            # Swap therir values 
             n[i], n[i+1] = n[i+1],n[i]

             steps += 1
        print(n)
        print(str(steps) + " Steps to sort.")

Bub_sort(Int_list)