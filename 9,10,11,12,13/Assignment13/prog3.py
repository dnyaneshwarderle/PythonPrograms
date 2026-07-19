def PerfectNumber(val):
    DivisorNumber = list()
    for i in range(1,val):
        if val % i == 0:
            DivisorNumber.append(i)
    return sum(DivisorNumber) == val
    
def main():
    no = int(input("Enter the Number: "))
    ret = PerfectNumber(no)
    if ret == True:
        print(no, " is a Perfect Number")
    else:
        print(no, " is not Perfect Number")

        
if __name__ == "__main__":
    main()