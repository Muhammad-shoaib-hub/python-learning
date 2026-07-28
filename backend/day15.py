# today we do (Lists - creating, indexing, slicing )

# create a list of favorite fruits 
fruits = ["apple","banana","cherry","date","elderberry"]
print("my favorite fruits list is = ",fruits)

print("\n--- 2. Indexing, (getting a single item)---")
# Python starts counting positions from 0!
# ["apple", "banana", "cherry", "date", "elderberry"]
#     0         1         2        3          4

print("the first fruits is = ", fruits[0])
print("the 3  fruits = ", fruits[2])
print("the last fruit is = ", fruits[-1])


print("\n--- 3. SLICING (Getting a slice/chunk of the list) --- ")
# Slicing syntax is list[start : stop] -> it goes up to, but does NOT include the stop index!

print("fruits from 1 to 2 is = ", fruits[1:3])
print("fruits from start to 4 =", fruits[:5] )
print("fruits from 2 to the end = ", fruits[2:])

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


heroes = ["shoaib","khan","jan","zia","Ali","shan"]
print("these are our heroes = ", heroes)

print("our first hero is = ", heroes[0])
print("our third hero is = ", heroes[2])

print("our first three heroes are here = ", heroes[0:3])
print("our last three heroes are here =", heroes[3:])
