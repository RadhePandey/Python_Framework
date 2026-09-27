first_name = "Radhe"
last_name = "Pandey"
age = 28

print(first_name+last_name+str(age))  #concatination
print(first_name,last_name) 

print("Loop")
for i in first_name:
    #print(i)
    print(i, end="")
# print('\n')
#print()
print(f"My name is {first_name} {last_name} and My age is {age}")


#----------------------------------------------------------------
#List

a = [12,3.3,3.4,"RadhePandey",False]

print(a[1]) #use to print entire list
print(a[1:4]) #use to print list values
print(a[3][4]) #use to print string values
print(a[::-1]) #use to reverse printing
