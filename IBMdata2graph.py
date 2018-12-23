import pandas as pd


def DataInput():
    df = pd.read_table("AR.data",delim_whitespace=True,header=None)  
    df = df.drop(labels=1, axis=1)
    df.set_index(0,inplace=True)
    return df
    
def Data2Graph(df):
    Graph7 = pd.DataFrame()
    Graph8 = pd.DataFrame()
    for i in range(1,df.index.max()):
        Transaction = df[2][i].tolist()
        if type(Transaction) != list:
            Transaction = [Transaction]
            continue
        for j in range(1,len(Transaction)):
            Graph7 = Graph7.append([[Transaction[j-1], Transaction[j]]],ignore_index=True)
            Graph8 = Graph8.append([[Transaction[j-1], Transaction[j]]],ignore_index=True)
            Graph8 = Graph8.append([[Transaction[j], Transaction[j-1]]],ignore_index=True)
    return Graph7,Graph8
    
if __name__ == '__main__':
    df = DataInput()
    Graph7,Graph8 = Data2Graph(df)
    Graph7.to_csv('graph_7.txt',header=False,index=False)
    Graph8.to_csv('graph_8.txt',header=False,index=False)