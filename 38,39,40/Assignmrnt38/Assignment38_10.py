import pandas as pd
import matplotlib.pyplot as plt
def Display():
    
    df = pd.read_csv("student_performance_ml.csv")

    SleepHours = df['SleepHours']
    FinalResult = df['FinalResult']

    df.boxplot(
        column = "SleepHours",
        by = "FinalResult",
    )
   
    plt.title("Students Sleep Hours  vs Result")
    plt.ylabel("FinalResult")
    plt.ylabel("SleepHours")
    plt.show()


def main():
    Display()

if __name__ == "__main__":
    main()