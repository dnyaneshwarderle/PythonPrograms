import pandas as pd
import matplotlib.pyplot as plt
def Display():
    
    df = pd.read_csv("student_performance_ml.csv")

    StudyHours = df['StudyHours']

    plt.hist(
        StudyHours,
        bins = 5,
        edgecolor = 'black',
        alpha = 0.8,
        rwidth = 0.9
    )
   
    plt.title("Students Study Hours")
    plt.xlabel("Study Hours")
    plt.ylabel("Frequency")
    plt.show()


def main():
    Display()

if __name__ == "__main__":
    main()