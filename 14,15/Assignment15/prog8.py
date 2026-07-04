Divisible = lambda x : x % 3 == 0 and x % 5 == 0

def main():
    number_list = [2,3,4,15,8,30,9]

    ret = list(filter(Divisible, number_list)) 
    print("Divisible by 3 and 5 numbers are : ",ret)
    
        
if __name__ == "__main__":
    main()