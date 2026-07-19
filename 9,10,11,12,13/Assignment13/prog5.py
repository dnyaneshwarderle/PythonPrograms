def Grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    elif marks < 50:
        return "Fail"

def main():
    marks = int(input("Enter the Number: "))
    ret = Grade(marks) 
    print(ret)
    
        
if __name__ == "__main__":
    main()