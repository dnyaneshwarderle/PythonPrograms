Square = lambda x : x * x

def main():
    no = int(input("Enter the Number: "))
    ret = Square(no) 
    print(f"Square of {no} is ",ret)
    
        
if __name__ == "__main__":
    main()