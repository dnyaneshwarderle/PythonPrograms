import threading

def Prime(lst):
    ResultLst = list()
    for No in lst:
        PrimeLst = list()
        if No == 1 or No == 2:
            PrimeLst.append(No)
        else:
            for i in range(2,No):
                if No % i == 0:
                    PrimeLst.append(i)
        if len(PrimeLst) == 0:
            ResultLst.append(No)
    print(ResultLst)

def NonPrime(lst):
    
    ResultLst = list()
    for No in lst:
        NonPrimeLst = list()
        for i in range(2,No):
            if No % i == 0:
                NonPrimeLst.append(i)
        if len(NonPrimeLst) != 0:
            ResultLst.append(No)
    print(ResultLst)
    
def main():
    t1_obj = threading.Thread(target=Prime, args=([1,2,3,4,5,6,7,8,9],))
    t1_obj.start()
    t1_obj.join()  

    t2_obj = threading.Thread(target=NonPrime, args=([1,2,3,4,5,6,7,8,9],))
    t2_obj.start()
    t2_obj.join()

    print("Exit from main.")

if __name__ == "__main__":
    main()