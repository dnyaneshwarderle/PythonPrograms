from functools import reduce
product = lambda x,y :x * y

def main():
    number_list = [2,3,4,5,8,7,9]

    ret = reduce(product, number_list) 
    print("Product of all numbers is : ",ret)
    
        
if __name__ == "__main__":
    main()  