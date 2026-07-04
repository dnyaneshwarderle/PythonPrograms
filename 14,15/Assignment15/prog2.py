Even = lambda x : x % 2 == 0

def main():
    number_list = [2,3,4,5,8,7,9]

    ret = list(filter(Even, number_list)) 
    print("Even numbers are : ",ret)
    
        
if __name__ == "__main__":
    main()