Square = lambda x :x * x

def main():
    number_list = [2,3,5,8,7,9]

    ret = list(map(Square, number_list)) 
    print("Square of all numbers are : ",ret)
    
        
if __name__ == "__main__":
    main()