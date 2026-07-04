Even = lambda x : x % 2 == 0 

def main():
    no = int(input("Enter the Number: "))
    ret = Even(no) 
    if ret == True:
        print("Even Number")
    else:
        print("Odd Number")
    
        
if __name__ == "__main__":
    main()