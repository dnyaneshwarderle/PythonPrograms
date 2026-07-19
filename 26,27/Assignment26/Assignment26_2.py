class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    
    def Accept(self):
        self.Radius = float(input("Enter the Radius of circle: "))

    def CalculateArea(self):
        self.Area = self.PI * self.Radius * self.Radius 

    def CalculateCircumference(self):
        self.Circumference = 2 * self.PI * self.Radius

    def Display(self):
        print(f"Radius of circle is: {self.Radius}")
        print(f"Area of circle is: {self.Area}")
        print(f"Circumference of circle is: {self.Circumference}")

obj1 = Circle()


obj1.Accept()
obj1.CalculateArea()

obj1.CalculateCircumference()
obj1.Display()

