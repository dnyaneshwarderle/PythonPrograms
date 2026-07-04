Minimum = lambda x,y :x if  x < y else y 

def main():
    no1 = int(input("Enter the 1st Number: "))
    no2 = int(input("Enter the 2nd Number: "))
    ret = Minimum(no1, no2) 
    print("Minimum is ",ret)
    
        
if __name__ == "__main__":
    main()