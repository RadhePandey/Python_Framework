class student:
    def __init__(self, Fullname):
        self.name = Fullname
        print("Adding new student in Database")

s1 = student("Radhe")
print(s1.name)

s2 = student("Kaushal")
print(s2.name)


def add(a,b):
    a = 10
    b = 12
    sum = a+b
    print(sum)

add(2,4)

# def factorial(num):
#     result = 1

#     for i in range(1, num + 1):
#         result = result * i

#     print("Factorial =", result)

# factorial(5)

def factorial(num):
    result = 1
    for i in range(1,num+1):
        result = result*i

    print(result)

factorial(12)
