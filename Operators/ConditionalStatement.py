#WAP to check the eligibility criteria for participating in election

# age= 19

# if 18<= age <=21:
#     print("Eligible for Election and Voting ")
# else:
#     print("Not eligible for voting")


# age = 21

# if age >= 21:
#     print("Eligible for Election")
# else:
#     print("Not eligible for Election")

# User = int(input("Enter age of user "))

# if User >=21:
#     print("User is eligible for Election and Voting")
# elif User >=18 and User<21:
#     print("User is only eligible for voting not for election")
# else:
#     print("Not Eligible for Voting and Election")



#wap to compare three no 

# a = 10
# b = 27
# c = 16

# if a > b and a > c:
#     print("a is the greatest")
# elif b > a and b > c:
#     print("b is the greatest")
# else:
#     print("c is the greatest")


#WAP to check whether 10 is divisible in both 2 and 4.

# num = 10

# if num % 2 == 0 or num % 4 == 0:
#     print("num is divisible by 2 or 4.")
# else:
#     print("num is not divisible by 2 or 4.")


#WAP to check whether 8 is divisible in either 3 or 4.

# num = 8 
# a= 3
# b= 4

# if num%a == 0 or num%b==0:
#     print("num is divisble by either 3 or 4")
# else:
#     print("num is not divisble by either 3 or 4")



# Grade A: if marks is beteween 76 and 100
# marks = int(input("Enter marks to print Grades = "))

# if marks >=76 and marks <=100:
#     print(" \nGrade A")
# elif marks >=51 and marks <=75:
#     print("Grade B")
# elif marks >=26 and marks <=50:
#     print("Grade C")
# else:
#     print("Grade D")




# Grade B: if marks is beteween  51 and 75
# Grade C: if marks is beteween 26 and 50
# Grade D: if marks is beteween 0 and 25


# Write a Python program to check if a number is positive, negative, or zero.

#num = int(input("Enter num = "))

# if num >0:
#     print("This is Positive number")
# elif num <0:
#     print("This is Negative number")
# else:
#     print("This is Zero")



# Write a Python code to check if a number is even or odd

# num = int(input("Enter num = "))

# if num % 2 == 0 :
#     print("This is Even Number")
# else:
#     print("This is Odd Number")

# Write a Python program to find the maximum of three numbers

num1 = int(input("Enter num = "))
num2 = int(input("Enter num = "))
num3 = int(input("Enter num = "))

if num1 > num2 and num1 > num3:
    print("num1 is greatest")
elif num2 > num1 and num2 > num3:
    print("num2 is greatest")
else:
    print("num3 is greatest")
