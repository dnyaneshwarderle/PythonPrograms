from functools import reduce
Maximum = lambda x,y :x if x > y else y

def main():
    number_list = [2,3,4,5,8,7,9]

    ret = reduce(Maximum, number_list) 
    print("Maximum of all numbers is : ",ret)
    
        
if __name__ == "__main__":
    main()