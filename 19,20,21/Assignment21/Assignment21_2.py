import threading

def ListMax(InputLst):
    MaxVal = 0
    for val in InputLst:
        if MaxVal < val:
            MaxVal = val  
    print(MaxVal)

def ListMin(InputLst):
    MinVal = InputLst[0]
    for val in InputLst:
        if MinVal > val:
            MinVal = val  
    print(MinVal)
    
def main():
    t1_obj = threading.Thread(target=ListMax, args=([1,2,3,4,5,6,7,8,9],))
    t1_obj.start()
    t1_obj.join()  

    t2_obj = threading.Thread(target=ListMin, args=([1,2,3,4,5,6,7,8,9],))
    t2_obj.start()
    t2_obj.join()

    print("Exit from main.")

if __name__ == "__main__":
    main()