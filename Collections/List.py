# Exercise 1. Perform Basic List Operations

list1 = [1,2,3,4,5,6,7]

print(sum(list1))
print(max(list1))
print(min(list1))

#Exercise 2. Perform List Manipulation

print(list1[2])
# clearlist=list1.clear()
# print(clearlist,"List Clear") #why i am getting NONE in Output here

list1.append("Radhe") #list is not going to store in new variable with append

print(list1,"\nList is updated") 

list1[1]="Uncodemy"           #update list item position
print(list1,"\nUpdated 2nd List item")
print("\nPrinting remove\n")

list1.remove("Radhe")         #remove item from list
print(list1)

print("Delete")
del list1[1]   #list deleted 
print(list1)


#Exercise 3. Sum and Average of All Numbers in a List

list2 = [2,4,6,7,9]

length = len(list2)
sum = 0

for i in range(0,length):
    # print(list2[i])
    sum = list2[i] + sum
print(sum)