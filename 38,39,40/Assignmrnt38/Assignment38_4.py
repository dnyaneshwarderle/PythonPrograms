import pandas as pd

def Display():
    
    df = pd.read_csv("student_performance_ml.csv")

    passFailCount = df['FinalResult'].value_counts()
    print("Average Study hours: ", passFailCount)

    totalStud = len(df)

    passStud = (passFailCount[1]/totalStud)*100
    print(f"Pass student: {passStud} %" )

    failStud = (passFailCount[0]/totalStud)*100 
    print(f"Fail student: {failStud} %")


def main():
    Display()

if __name__ == "__main__":
    main()