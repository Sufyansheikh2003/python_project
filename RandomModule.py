import random as rd

pakistan_cities = ["Karachi", "Lahore", "Islamabad", "Faisalabad", "Hyderabad", "Multan", "Sheikhupura", "Sialkot", "Bahawalpur", "Sargodha"]

#Print 3 random cities
print(rd.sample(pakistan_cities, 3))

#Shuffle List
rd.shuffle(pakistan_cities)
print(pakistan_cities)

#Select One City
print(rd.choice(pakistan_cities))



