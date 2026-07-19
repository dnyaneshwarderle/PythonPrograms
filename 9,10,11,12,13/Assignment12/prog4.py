def ManyNumber(val):
    NumberList = list()
    for no in range(1,val+1):
        NumberList.append(no)
    return NumberList
    
def main():
    no = int(input("Enter the Number: "))
    ret = ManyNumber(no)
    print("Starting from 1 to ",no, " is ", ret)
    for i in ret:
        print(i)
        
if __name__ == "__main__":
    main()