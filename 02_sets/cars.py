# Create an empty set
showroom = set()

# Update the set with four of your favorite vehicles
showroom.update({"Rolls Royce Phantom", "BMW M4", "Mercedes-Benz G-Class", "Jeep Grand Cherokee"})

# Print length of set

print(len(showroom))

# Add recent item to showroom again
# Sets can only be unique items

showroom.update({"Ford Mustang", "Dodge Challenger"})

# Remove one item from showroom

showroom.discard("Dodge Challenger")

# New array with another set of vehicles

junkyard = set()
junkyard.update({"Old Car 1", "Old Car 2", "Old Car 3", "BMW M4", "Jeep Grand Cherokee"})

# Intersection method finds the commonality between two sets

print(showroom.intersection(junkyard))

# Union method combines the two sets into one

showroom = showroom.union(junkyard)

# Discard removes one element your set

showroom.discard("Old Car 1")

print(showroom)


