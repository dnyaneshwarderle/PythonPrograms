def Factors(val):
    FactorList = list()
    for no in range(1,val+1):
        if val % no == 0:
            FactorList.append(no)
    return FactorList
    
def main():
    no = int(input("Enter the Number: "))
    ret = Factors(no)
    print("factors of number ",no, " is ", ret)
    for i in ret:
        print(i)
        
if __name__ == "__main__":
    main()