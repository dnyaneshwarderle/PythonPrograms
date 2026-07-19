class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    
    def Accept(self):
        self.Value1 = float(input("Enter the value1: "))
        self.Value2 = float(input("Enter the value1: "))

    def Addition(self):
        Result = self.Value1 + self.Value2 
        return Result

    def Substraction(self):
        Result = self.Value1 - self.Value2 
        return Result

    def Multiplication(self):
        Result = self.Value1 * self.Value2 
        return Result

    def Division(self):
        Result = self.Value1 / self.Value2 
        return Result

obj1 = Arithmetic()

obj1.Accept()
add = obj1.Addition()
sub = obj1.Substraction()
mult = obj1.Multiplication()
div = obj1.Division()

print("Addition is: ",add)
print("Substraction is: ",sub)
print("Multiplication is: ",mult)
print("Division is: ",div)

