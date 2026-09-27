num1 = float(input("Enter num1 : "))
num2 = float(input("Enter num2 : "))
num3 = float(input("Enter num3 : "))


if num1 > num2 and num2 > num1:
    print(num1 , "is largest amoung these three numbers")
elif num2 > num1 and num2 > num3:
    print(num2 , "is largest amount these three numbers")
else:
    print(num3,"is largest amount these three numbers")
    