#importing necessary packages
import pandas as pd
import numpy as np
import matplotlib as mplt
import seaborn as sb

#importing the csv dataset and converting to dataframe using pandas
file = pd.read_csv(r'C:\Users\User\Desktop\UCD DATA\Property Price Register Datasets\Property_Price_Register_Ireland-28-05-2021.csv')
df = pd.DataFrame(file)
#print(df.head())
print(df.head())

#sale_price = df['Price ()']
#county = df['County']

#import matplotlib.pyplot as plt

#plt.plot(sale_price, county)
#plt.show()
