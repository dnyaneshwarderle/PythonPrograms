Addition = lambda x,y :x + y 

def main():
    no1 = int(input("Enter the 1st Number: "))
    no2 = int(input("Enter the 2nd Number: "))
    ret = Addition(no1, no2) 
    print("Addition is ",ret)
    
        
if __name__ == "__main__":
    main()