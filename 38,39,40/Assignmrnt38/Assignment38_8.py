import pandas as pd
import matplotlib.pyplot as plt
def Display():
    
    df = pd.read_csv("student_performance_ml.csv")

    Attendance = df['Attendance']

    plt.boxplot(
        Attendance
    )
   
    plt.title("Students Attendance")
    plt.ylabel("Attendance")
    plt.show()


def main():
    Display()

if __name__ == "__main__":
    main()