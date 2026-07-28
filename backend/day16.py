# day16 is (List methods (append, remove, sort, etc.)

# the normal list of cars
cars = ["Toyota","Honda","BMW"]
print("Orignal list = ", cars)

# 1. adding a item in the end by using .append()
cars.append("Ford")
print("After the append = ", cars)

# 2. inserting a item at a specific position (index 1 ) using .insert()
cars.insert(1,"tesla")
print("After inserting = ", cars )

# 3. removing an item from list( cars ) by name using .remove()
cars.remove("BMW")
print("After removing = ", cars)

# 4. Sorting the list alphabetically using .sort()
cars.sort()
print("After sorting the list alphabetically = ", cars)


print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


gro = ["milk","eggs","bread"]
print("orignal list is = ", gro)

gro.append("butter")
print("after the append = ",gro)

gro.insert(0,"chocolate")
print("after the inserting = ", gro)

gro.remove("eggs")
print("afther removing = ", gro)

gro.sort()
print("after sorting = ", gro)