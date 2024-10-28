import pandas as pd
mydata=pd.read_csv('./test.csv',sep=',',dtype=object)
print(mydata)
print(mydata.loc[2:4,'LANGUAGE'])

