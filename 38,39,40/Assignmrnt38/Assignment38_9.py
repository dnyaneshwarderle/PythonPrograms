import pandas as pd
import matplotlib.pyplot as plt
def Display():
    
    df = pd.read_csv("student_performance_ml.csv")

    AssignmentsCompleted = df['AssignmentsCompleted']
    FinalResult = df['FinalResult']

    df.boxplot(
        column = "AssignmentsCompleted",
        by = "FinalResult",
    )
   
    plt.title("Students Assignmens completed vs Result")
    plt.ylabel("FinalResult")
    plt.ylabel("AssignmentsCompleted")
    plt.show()


def main():
    Display()

if __name__ == "__main__":
    main()