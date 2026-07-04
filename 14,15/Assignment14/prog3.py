Maximum = lambda x,y :x if  x > y else y 

def main():
    no1 = int(input("Enter the 1st Number: "))
    no2 = int(input("Enter the 2nd Number: "))
    ret = Maximum(no1, no2) 
    print("Maximum is ",ret)
    
        
if __name__ == "__main__":
    main()