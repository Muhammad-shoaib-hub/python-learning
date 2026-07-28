# Day 20 Sets and set operations

# 1. Creating a set with duplicates
# Notice that "apple" is written twice!

my_fruits = {"apple", "banana", "apple", "orange"}
print("---1 Automatic Duplicate Removel---")
print("my fruits set is = ", my_fruits)

# 2. Set Operations (Comparing two sets)
shoaib_skills = {"HTML","CSS", "python"}
job_requirements = {"python","#","C++"}

print("--- 2. Intersection (what do they have common?)")
# .intersection() finds items that exist in BOTH sets
matching_skills = shoaib_skills.intersection(job_requirements)
print("skills you have for a job = ", matching_skills)

print("---3. Union (combine everthing, no duplicates!)")
# .union() mixes both sets together into one master set
all_skills = shoaib_skills.union(job_requirements)
print("All Skills combined = ", all_skills)




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



shoaib_movies = {"batman","superman","spiderman"}
friend_movies = {"spiderman","ironman","Avengers"}

we_both =  shoaib_movies.intersection(friend_movies)
print("the movies we both love is = ", we_both)

the_movies = shoaib_movies.union(friend_movies)
print("the movies we watched is = ", the_movies)