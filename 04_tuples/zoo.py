zoo = ("Jaguar", "Elephant", "Lion", "Bear")

print(zoo.index("Elephant"))

for animal in zoo:
    if animal == "Jaguar":
        print("This animal is in the zoo.")
    else:
        print("This animal is not at the zoo.")

(Jaguar, Elephant, Lion, Bear) = zoo

print(Jaguar)


zoo = list(zoo)

zoo = tuple(zoo)

print(type(zoo))

