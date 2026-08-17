import pandas as pd

def Display():
    
    df = pd.read_csv("student_performance_ml.csv")

    print("First 5 Record: \n", df.head())

    print("First 5 Record: \n", df.tail())

    print("Total Number of rows and columns: \n", df.shape)

    print("List of columns:\n", df.columns)

    print("Datatype of each columns:\n", df.dtypes)


def main():
    Display()

if __name__ == "__main__":
    main()