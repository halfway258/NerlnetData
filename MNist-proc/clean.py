import pandas as pd

## moves label to front
def move_first_to_last(file):
    df = pd.read_csv(file, header=None)
    first_column = df.pop(df.columns[0])
    df.insert(len(df.columns), first_column.name, first_column)
    df.to_csv(file, index=None, header=None)

## example: label = 2 ==> 0,0,1,0,0,0,...
def label_num_to_array(file):
    df = pd.read_csv(file, header=None)
    labels = df.pop(df.columns[len(df.columns)-1])
    label_df = pd.DataFrame(0, index=list(range(len(df.index))), columns=list(range(10)))
    for i in range(len(df.index)):
        label_df.at[i, labels[i]] = 1
    
    for i in range(len(label_df.columns)):
        df.insert(len(df.columns), "col"+str(i), label_df.pop(label_df.columns[0]))

    df.to_csv(file, index=None, header=None)

## take <file>_test.csv -> <file>_prediction.csv without the label columns
def make_predict(labels, file):
    df = pd.read_csv(f'{file}_test.csv', header=None)
    df_predict_test = df.iloc[:,:-labels]

    df_predict_test.to_csv(f"{file}_prediction.csv", index=None, header=None)

## split single file to training/predict/test (here in 5:1)
def splitToFiles():
    df = pd.read_csv('mnist_full_labeled.csv', header=None)
    df_train = df.iloc[:int(len(df.index)*5/6),:]
    df_predict = df.iloc[int(len(df.index)*5/6):,:]
    labels = 10
    df_predict_test = df_predict.iloc[:,:-labels]

    df_train.to_csv("mnist_training.csv", index=None, header=None)
    df_predict.to_csv("mnist_prediction_test.csv", index=None, header=None)
    df_predict_test.to_csv("mnist_prediction.csv", index=None, header=None)

def shuffle(file):
    df = pd.read_csv(file, header=None)
    df = df.sample(frac = 1)
    df.to_csv(file, index=None, header=None)

## keep only frac of beggining file
def split(file, frac):
    df = pd.read_csv(file, header=None)
    df = df.iloc[:int(len(df.index)*frac),:]
    df.to_csv(file, index=None, header=None)

if __name__ == "__main__":

    # move_first_to_last("MNist-proc2_train.csv")
    # label_num_to_array("MNist-proc2_train.csv")
    # shuffle("MNist-proc2_train.csv")
    # make_predict(10, "MNist-proc2")
    split("MNist-proc2_training.csv", 1/2)

