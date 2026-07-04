Divisible = lambda x : x % 5 == 0 

def main():
    no = int(input("Enter the Number: "))
    ret = Divisible(no) 
    if ret == True:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")
    
        
if __name__ == "__main__":
    main()