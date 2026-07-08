import threading

def EvenFactors(No):
    EvenList = list()
    for i in range(1,No+1):
        if i % 2 == 0:
            EvenList.append(i)
    print(sum(EvenList))
    
def OddFactors(No):
    OddList = list()
    for i in range(1,No+1):
        if i % 2 != 0:
            OddList.append(i)
    print(sum(OddList))
    

def main():
    print("Sum of Even Factors is: ", end=" ")
    t1_obj = threading.Thread(target=EvenFactors, args=(10,))
    t1_obj.start()
    t1_obj.join()

    print("Sum of Odd Factors is: ", end=" ")
    t2_obj = threading.Thread(target=OddFactors, args=(10,))
    t2_obj.start()
    t2_obj.join()

    print("Exit from main.")



if __name__ == "__main__":
    main()