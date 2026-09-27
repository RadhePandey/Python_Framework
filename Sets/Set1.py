# a = {1,2,3,3,True,"Radhe"}
# print(a)

# a.add(8)
# print(a)

# a.discard("Radhe")
# print(a)

# Exercise 1: Basic Set Operations

set1 = {"Apple","Mango",2,3,}
print(set1)

set1.add("Python")
print(set1,"Python added\n")

set1.discard("Mango")
print(set1,"Discarded\n")

# Exercise 2: Clear All Elements

set1 = {"Apple", "Mango", 2, 3}

print("Before clear:", set1)

set1.clear()

print("After clear:", set1)

# Exercise 3: Find the Length of a Set
set1 = {"Apple", "Mango", 2, 3}
print(len(set1))

# Exercise 4: Check if a Set is Empty
set2 = {1}
res = print(len(set2))

if res == 0:
    print("set2 is empty")
else:
    print("set2 is not empty")

# Exercise 5: Union of Sets

sets1 = {"Apple", "Mango", 2, 3}
sets2 = {4.6, 193, 'R', False}

result = sets1.union(sets2)

print("Union of sets:", result)


# Exercise 6: Intersection of Sets



# Exercise 7: Difference of Sets


# Exercise 8: Symmetric Difference


# Exercise 9: Find Max and Min


# Exercise 10: Sum of Set Elements