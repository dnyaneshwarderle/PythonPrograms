from functools import reduce
Sum = lambda x,y : x + y

def main():
    number_list = [2,3,4,5,8,7,9]

    ret = reduce(Sum, number_list) 
    print("Sum of all numbers are : ",ret)
    
        
if __name__ == "__main__":
    main()