def AreaOfRectangle(length, width):
    area = length * width
    return area
    
def main():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    ret = AreaOfRectangle(length,width)
    print("Area of Rectangle is", ret)

        
if __name__ == "__main__":
    main()