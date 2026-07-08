import threading

def EvenList(lst):
    EvenList1 = list()
    for i in lst:
        if i % 2 == 0:
            EvenList1.append(i)
    print("Sum of Even Numbers is: ",sum(EvenList1))
    
def OddList(lst):
    OddList1 = list()
    for i in lst:
        if i % 2 != 0:
            OddList1.append(i)
    print("Sum of Odd number is: ",sum(OddList1))
    

def main():
    t1_obj = threading.Thread(target=EvenList, args=([1,2,3,4,5,6,7,8,9],))
    t2_obj = threading.Thread(target=OddList, args=([1,2,3,4,5,6,7,8,9],))

    t2_obj.start()
    t1_obj.start()

    t1_obj.join()    
    t2_obj.join()

    print("Exit from main.")



if __name__ == "__main__":
    main()