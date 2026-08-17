import pandas as pd
import matplotlib.pyplot as plt
def Display():
    
    df = pd.read_csv("student_performance_ml.csv")

    StudyHours = df['StudyHours']
    PreviousScore = df['PreviousScore']

    plt.scatter(
        StudyHours,
        PreviousScore,
        s = 100,
        marker = 'o',
        edgecolor = 'black',
        alpha = 0.8,
        linewidth = 1,
        label="Student"
    )
   
    plt.title("Students Study Hours vs Previous Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    Display()

if __name__ == "__main__":
    main()