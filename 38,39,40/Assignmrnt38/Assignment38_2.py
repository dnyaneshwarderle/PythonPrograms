import pandas as pd

def Display():
    
    df = pd.read_csv("student_performance_ml.csv")

    print("Total number of students: ", len(df))

    print("Passed Students :", len(df[df['FinalResult'] == 1]))

    print("Failed Students :", len(df[df['FinalResult'] == 0]))


def main():
    Display()

if __name__ == "__main__":
    main()