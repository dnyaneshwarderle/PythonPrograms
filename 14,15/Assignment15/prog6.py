from functools import reduce
Minimum = lambda x,y :x if x < y else y

def main():
    number_list = [2,3,4,5,8,7,9]

    ret = reduce(Minimum, number_list) 
    print("Minimum of all numbers is : ",ret)
    
        
if __name__ == "__main__":
    main()