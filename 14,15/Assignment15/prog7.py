StrCheck = lambda x : len(x) > 5

def main():
    str_list = ["Python","Jay Ganesh","Hello","Marvellous"]

    ret = list(filter(StrCheck, str_list)) 
    print("Word length greate than 5  : ",ret)
    
        
if __name__ == "__main__":
    main()