# def sum(x, y):
#     print(x + y)

# def div(x, y):
#     print(x / y)

# def name(firstname, lastname):
#     print(firstname, lastname)

# sum(10, 12.2)
# div(12, 34)
# name("Radhe", "Pandey")

# 1. Write a Python function to find the maximum of three numbers.
# def maximum(a,b,c):
#     print(max(a,b,c),"is max no")

# maximum(1,2,3)

# # 2. Write a Python function to sum all the numbers in a list.

# def add():
#     list1 = [1, 2, 3, 4]

#     listlength = len(list1)
#     sum = 0

#     for i in range(listlength):
#         sum = sum + list1[i]

# #     print("Sum =", sum)

# # add()
    
# # 3. Write a Python function to multiply all the numbers in a list.

# def multiply():
#     list1 = [11, 10, 3, 4]

#     result = 1
#     listlength = len(list1)

#     for i in range(listlength):
#         result = result * list1[i]

#     print("Multiplication =", result)

# multiply()



# 4. Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result = result * i

    print("Factorial =", result)

factorial(5)


# 5. Write a Python program to print the even numbers from a given list.

# def num(a):
#     if a/2 == 0:
#         print("This is even no")
#     else:
#         print("This is odd no")

# num(5)