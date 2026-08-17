import pandas as pd

def Display():
    
    df = pd.read_csv("student_performance_ml.csv")

    print("Average Study hours: ", df['StudyHours'].mean())

    print("Average Attendance :", df['FinalResult'].mean())

    print("Average Attendance :", df['PreviousScore'].max())

    print("Average Attendance :", df['SleepHours'].min())

def main():
    Display()

if __name__ == "__main__":
    main()