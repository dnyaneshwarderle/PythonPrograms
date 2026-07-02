def ManyNumberReversed(val):
    NumberList = list()
    for no in range(val,0,-1):
        NumberList.append(no)
    return NumberList
    
def main():
    no = int(input("Enter the Number: "))
    ret = ManyNumberReversed(no)
    print("Starting from ",no, " to 1 is ", ret)
    for i in ret:
        print(i)
        
if __name__ == "__main__":
    main()