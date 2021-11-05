import pandas as pd
#x =
#print(x.head())
#df=pd.DataFrame(x)
#print(df.head())

file = pd.read_csv("C:\\Users\\User\\Desktop\\PPR.csv", encoding='latin1')
df = pd.DataFrame(file)
print(df.head())
