# def is_even():
#     num = int(input("Enter number : "))
#     if num%2 == 0:
#         print(num,"is even no")
#     else:
#         print(num,"is odd no")

# is_even()
    
# def largest_no(a,b,c):
#     if a>b & a>c:
#         print("a is largest no")
#     elif b>a & b>c:
#         print("b is largest no")
#     else:
#         print("c is largest no")

# largest_no(12,13,16)


# def check_vowel():
#     ch = input("Enter char : ")

#     if ch == "AaEeIiOoUu":
#         print("This is vowel ")
#     else:
#         print("This is not vowel")

# check_vowel()

# #Check whether a number is divisible by both 5 and 11.

# def is_divisible():
#     num = int(input("Enter number : "))
#     if num%5 == 0 and num%11 == 0:
#         print("Number is divisible by both 5 and 11")
#     else:
#         print("Number is not divisble by both 5 and 11")



# is_divisible()

#  #rate of eletricty bills are 
#  # 0 to 100 unit = 5rs
#  #100 to 300 unit = 7rs
#  #above 300 unit = 9rs
# def electricity_bill():
#     last_unit = float(input("Enter last Unit : "))
#     current_unit = float(input("Enter current unit : "))

#     Total_unit = current_unit - last_unit
#     if Total_unit <100:
#         bill = Total_unit*5
#         print("Your total electricity bill is = ",bill)
#     elif Total_unit >=100 and Total_unit <300:
#         bill = Total_unit*5
#         print("Your total electricity bill is = ",bill)
#     else:
#         bill = Total_unit*5
#         print("Your total electricity bill is = ",bill)

# electricity_bill()

# def login():
#     username = input("Enter username : ")
#     password = input("Enter password : ")

#     if username == "Radhe" and password == "12345":
#         print("User login successfully!!")
#     else:
#         print("username or password incorrect")

# login()


# def is_triangle():
#     a = int(input("Enter value of angle a : "))
#     b = int(input("Enter value of anagle b"))
#     c = int(input("Enter value of anagle c"))

#     if a+b+c == 180:
#         print("This is Triangle")
#     else:
#         print("This is not triangle")


# is_triangle()

#Find the second largest among three numbers.
# def is_secondlargest():
#      a = int(input("Enter value of a : "))
#      b = int(input("Enter value of b : "))
#      c = int(input("Enter value of c : "))

#      largest = max(a,b,c)
#      print(largest)

#      if b>largest and b>c:
#         print("b is second largest number")
#      else:
#         print("C is second largest number") 


# is_secondlargest()

#Check whether a character is:
# Alphabet
# Digit
# Special Character

ch = input("Enter a character: ")

if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
    print("Alphabet")

elif '0' <= ch <= '9':
    print("Digit")

else:
    print("Special Character")


    


    

