class MyNumber:
    def __init__(self, num):
        self.num = num

    def __add__(self, other): # Overloading the + operator
        return self.num - other.num # Subtraction instead of addition

n1 = MyNumber(9)
n2 = MyNumber(4)
print(n1 + n2) #Output: 5 (9 - 4)
print(1 + 2) #Output: 3 (normal addition)




