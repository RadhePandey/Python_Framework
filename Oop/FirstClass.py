class A:
    a = 33

    def M(self):
        print("Uncodemy")

obj = A()

print(obj.a)
print(A.a)

obj.M()
#wheneve we want to call method using object we can not call directly , we have to use Self as argument inside Method
#  - Which is called Instance function



