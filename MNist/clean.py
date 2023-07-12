import pandas as pd

## moves label to front
def move_first_to_last():
    df = pd.read_csv('mnist_train.csv', header=None)
    first_column = df.pop(df.columns[0])
    df.insert(len(df.columns), first_column.name, first_column)
    df.to_csv("mnist_full.csv", index=None, header=None)

## example: label = 2 ==> 0,0,1,0,0,0,...
def label_num_to_array():
    df = pd.read_csv('mnist_full.csv', header=None)
    labels = df.pop(df.columns[len(df.columns)-1])
    label_df = pd.DataFrame(0, index=list(range(len(df.index))), columns=list(range(10)))
    for i in range(len(df.index)):
        label_df.at[i, labels[i]] = 1
    
    for i in range(len(label_df.columns)):
        df.insert(len(df.columns), "col"+str(i), label_df.pop(label_df.columns[0]))

    df.to_csv("mnist_full_labeled.csv", index=None, header=None)

## s
def split():
    df = pd.read_csv('mnist_full_labeled.csv', header=None)
    df_train = df.iloc[:int(len(df.index)/2),:]
    df_predict = df.iloc[int(len(df.index)/2):,:]
    labels = 10
    df_predict_test = df_predict.iloc[:,:-labels]

    df_train.to_csv("mnist_training.csv", index=None, header=None)
    df_predict.to_csv("mnist_prediction.csv", index=None, header=None)
    df_predict_test.to_csv("mnist_prediction_test.csv", index=None, header=None)

if __name__ == "__main__":

    # move_first_to_last()
    # label_num_to_array()
    split()