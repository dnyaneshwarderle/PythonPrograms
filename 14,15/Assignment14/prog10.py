Largest = lambda x,y,z :x if  x > y and x > z else ( y if y > x and y > z else z)

def main():
    no1 = int(input("Enter the 1st Number: "))
    no2 = int(input("Enter the 2nd Number: "))
    no3 = int(input("Enter the 3rd Number: "))
    ret = Largest(no1, no2, no3) 
    print("Largest number is ",ret)
    
        
if __name__ == "__main__":
    main()