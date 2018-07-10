# Example of a LIST items

planets_list = [ "Mercury", "Mars"]


# Append method can only take one argument and appends item and the end of the list
# Adding it has an array [1, 2] adds it but is nested

# planets_list.append(
# ["Jupiter",
# "Saturn"])

# Expected Result: [Merc, Ven, Earth, Mars, Uranus, Neptune, [Jupiter, Saturn]]

# Extends method takes one item too but "merges" the lists together

planets_list.extend(["Jupiter", "Saturn"])

# Expected Result: [Mercury, Venus, Earth, Mars, Uranus, Neptune, Jupiter, Saturn]

# Insert method takes two arguments (index#, "item")

planets_list.insert(1, "Venus")
planets_list.insert(2, "Earth")

# Add Pluto to the end of the list

planets_list.append("Pluto")


# Syntax below is a slice method that grabs the first item you want and stopping before the last index listed
# Index 0 is included, while 4 is not included

rocky_planets = planets_list[0:4]

print(rocky_planets)

# Remove Pluto.

del planets_list[6]

print(planets_list)


# Tuples are immutable Ex. zoo = ("1", "2", "3")

satelites = [("Voyager", "Saturn"), ("Expedition", "Mercury"), ("Apollo", "Jupiter"), ("Adventurer", "Earth")]

for planet in planets_list:
    for satelite in satelites:
        if satelite[1] == planet:
            print(f"{planet} was visited by {satelite[0]}")