add = lambda x,y : x+y
# print(add_lambda(5,7))
print(add(1,2))


div = lambda a,b : a/b 
print(div(3.12,9))

num = lambda a,b,c : max(a,b,c)
print(num(33,44,55))


# Write a Python program to sort tuples using Lambda.

tup = (1, 2, 3, 4, 9, 5, 32, 7)
list_tup = list(tup)

print("\nTuple:", tup)
print("List:\n", list_tup)

list_tup.sort(key=lambda x:x)
print(tuple(list_tup))
print("1st ")




# Write a Python program to square and cube every number in a given list of integers using Lambda

number = [1,2,3,4,5,6]
square_number = list(map(lambda x: x**2, number))
print("Output is ", square_number)

cube_number = list(map(lambda x : x**3, number))
print("Output is : ",cube_number)
# Write a Python program to count the even and odd numbers in a given list of integers using Lambda.

even_number = list(filter(lambda x : x%2==0,number))
print("This is even numbers :" ,even_number)

# Write a Python program to add two given lists using map and lambda.
list1 = [1,23,4.4,5]
list2 = [11,12,1,2]

merge = list(map(lambda x,y : x+y , list1,list2))
print(merge,"5th")