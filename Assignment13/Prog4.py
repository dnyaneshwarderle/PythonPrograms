def CheckBinary(val):
    BinaryNumberStr = str()
    while val > 0:
        BinaryNumberStr = str(val % 2) + BinaryNumberStr
        val //= 2
    return BinaryNumberStr 
    
def main():
    no = int(input("Enter the Number: "))
    ret = CheckBinary(no) 
    print("Binary of number ", no," is", int(ret))
    
        
if __name__ == "__main__":
    main()