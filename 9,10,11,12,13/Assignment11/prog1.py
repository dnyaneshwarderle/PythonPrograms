def CheckPrime(val):
    for no in range(2,val):
        if (val % no == 0):
            return False
    return True

def main():
    no = int(input("Enter number: "))
    ret = CheckPrime(no)
    if ret == True:
        print("Its Prime numbers ")
    else:
        print("Not Prime Number")
    

if __name__ == "__main__":
    main()