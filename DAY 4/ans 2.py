# Question 1
#ans

class Test:

    def sum(self, a, b):
        s = a + b
        return s


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

obj = Test()
s = obj.sum(a, b)

print("Sum is:", s)