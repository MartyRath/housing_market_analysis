import pandas as pd
file = pd.read_csv("C:\\Users\\User\\Desktop\\PPR.csv", encoding='latin1')
df = pd.DataFrame(file)
print(df.head())

#print(df.head())
#print(df.columns)
#print(df.info())
#print(df.describe())

#df.shape - how many rows, columns
#df.values - data values in 2D Numpy array
#df.columns # Shows columns
#f.index

#print(df['SALE_PRICE'])
