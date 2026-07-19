def AreaOfCircle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area
    
def main():
    radius = int(input("Enter the radius: "))
    ret = AreaOfCircle(radius)
    print("Area of Circle is", ret)

        
if __name__ == "__main__":
    main()