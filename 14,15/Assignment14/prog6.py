Odd = lambda x : x % 2 != 0 

def main():
    no = int(input("Enter the Number: "))
    ret = Odd(no) 
    if ret == True:
        print("Odd Number")
    else:
        print("Even Number")
    
        
if __name__ == "__main__":
    main()