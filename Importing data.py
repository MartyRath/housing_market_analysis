#importing necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

#importing the csv dataset and converting to dataframe using pandas
df = pd.read_csv(r'C:\Users\User\Desktop\UCD DATA\Test\Property_Price_Register_Ireland-28-05-2021.csv')

#Dataframe was truncated to width 80 in Pycharm, so found the following options here to get a better overview: https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
pd.options.display.width= None
pd.options.display.max_columns= None

print(df.columns)
#print(df.head())
#print(df.shape)
#print(df.describe())

#SIMPLIFY
#Dropping columns I won't need. Going by county is enough for location, as excluding Dublin.
#Market price doesn't tell if above/below price sold, so not useful.
#Vat excluded just tells if old/new
df.drop(['POSTAL_CODE', 'ADDRESS', 'IF_MARKET_PRICE', 'IF_VAT_EXCLUDED'],axis=1,inplace=True)

#Missing Values
#Checking if there are missing values
missing_values = df.isnull().sum()
#print(missing_values[0:])

#what percent of these missing values against total rows minus column row
total_rows = df.shape[0] - 1

# % PROPERTY_SIZE_DESC missing values
#missing_values_PROPERTY_SIZE_DESC = df['PROPERTY_SIZE_DESC'].isnull().sum() / total_rows * 100
#print(missing_values_PROPERTY_SIZE_DESC)

#With over 80% missing, using this column won't show valuable and accurate insights
#Dropping column PROPERTY_SIZE_DESC due to missing values
df.drop(['PROPERTY_SIZE_DESC'],axis=1,inplace=True)
#print(df.head())

#Some descriptions were in Irish, so I replaced them with English
df['PROPERTY_DESC'].replace({'Teach/�ras�n C�naithe Nua': 'New Dwelling house /Apartment', 'Teach/?ras?n C?naithe Nua': 'New Dwelling house /Apartment', 'Teach/�ras�n C�naithe Ath�imhe': 'Second-Hand Dwelling house /Apartment'}, inplace=True)

description = df['PROPERTY_DESC']
#for unique_values in df:
#    print(description.unique())

#missing_values = df.isnull().sum()
#print(missing_values[0:])

#If I wanted to replace missing values, I could have executed the following two lines:
#df['POSTAL_CODE'] = df['POSTAL_CODE'].fillna('Unknown')
#df['PROPERTY_SIZE_DESC'] = df['PROPERTY_SIZE_DESC'].fillna('Unknown')

#To get unique values in PROPERTY DESC
#size = df['PROPERTY_SIZE_DESC']
#for unique_values in df:
#    print(size.unique())



#With a budget of 110K, finding cheap properties under this price
#cheap = df[['SALE_PRICE']]<100000
#cheap = df.loc[:, 'SALE_PRICE']
#cheap = df.iloc[:, 3]
#print(cheap) #All properties under 100000

#print(df.describe())