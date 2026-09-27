#list is mutual and can store duplicate values 

student = ["name","Age","Class",9721707235]
marks = [1,2,6,3,3]
print(student[1:5])
student.append(123)
print(student)
marks.sort()
print(marks)

print(set(marks))


marks.remove(2)
print(marks)

marks.reverse()
print(marks)

# for i in student:
#     print(i)