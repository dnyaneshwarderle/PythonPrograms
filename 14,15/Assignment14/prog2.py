Cube = lambda x : x * x * x

def main():
    no = int(input("Enter the Number: "))
    ret = Cube(no) 
    print(f"Cube of {no} is ",ret)
    
        
if __name__ == "__main__":
    main()