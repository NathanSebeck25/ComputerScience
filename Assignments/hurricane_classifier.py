wind_speeds = int(input("What is the wind speeds of the high wind (type in integer form)?\n:"))

if wind_speeds < 74:
    print("That is a Tropical storm")

elif wind_speeds < 96:
    print("That is a Catagory 1 Hurricane")

elif wind_speeds < 111:
    print("That is a Catagory 2 Hurricane")

elif wind_speeds < 130:
    print("That is a Catagory 3 Hurricane")

elif wind_speeds < 157:
    print("That is a Catagory 4 Hurricane")

elif wind_speeds >= 157:
    print("That is a Catagory 5 Hurricane")

