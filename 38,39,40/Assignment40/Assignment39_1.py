import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix


def TrainTestSplit(df):

    X = df.drop("FinalResult",axis = 1)
    Y = df['FinalResult']

    x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size = 0.3, random_state = 42) 
    
    return x_train, x_test, y_train, y_test

def ModelTraining(x_train, y_train):

    model = DecisionTreeClassifier(max_depth=None)
    model = model.fit(x_train, y_train)

    return model

def EvaluateMode(model, x_train, x_test, y_train, y_test):

    # training accuracy 
    Y_pred = model.predict(x_train)

    accuracy = accuracy_score(y_train, Y_pred)

    print("Training Accuracy is : ", accuracy*100)

    print(confusion_matrix(y_train,Y_pred))    

    # Testing acuuracy 
    Y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, Y_pred)

    print("Testing Accuracy is : ", accuracy*100)

    print(confusion_matrix(y_test,Y_pred))

    # New Student details
    StudyHours = 6
    Attendance = 65
    PreviousScore = 66
    AssignmentsCompleted = 7
    SleepHours = 7

    NewStudent = pd.DataFrame([{
        "StudyHours":StudyHours,
        "Attendance":Attendance,
        "PreviousScore":PreviousScore,
        "AssignmentsCompleted":AssignmentsCompleted,
        "SleepHours":SleepHours
    }])

    NewStudent = NewStudent[model.feature_names_in_]

    result = model.predict(NewStudent)
    if result[0] == 0:
        print("New Student Result is Fail ")
    else:
        print("New Student Result is Pass ")



def LoadData():

    df = pd.read_csv("student_performance_ml.csv") 

    return df

def main():
    df = LoadData()
    x_train, x_test, y_train, y_test = TrainTestSplit(df)
    model = ModelTraining(x_train, y_train)
    EvaluateMode(model,x_train,x_test,y_train,y_test)


if __name__ == "__main__":
    main()