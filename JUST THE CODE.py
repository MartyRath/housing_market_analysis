import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\User\Desktop\UCD DATA\Test\Property_Price_Register_Ireland-28-05-2021.csv')
pd.options.display.width= None
pd.options.display.max_columns= None
df.drop(['POSTAL_CODE', 'ADDRESS', 'IF_MARKET_PRICE', 'IF_VAT_EXCLUDED'],axis=1,inplace=True)
missing_values = df.isnull().sum()
df.drop(['PROPERTY_SIZE_DESC'],axis=1,inplace=True)
df['PROPERTY_DESC'].replace({'Teach/�ras�n C�naithe Nua': 'New Dwelling house /Apartment', 'Teach/?ras?n C?naithe Nua': 'New Dwelling house /Apartment', 'Teach/�ras�n C�naithe Ath�imhe': 'Second-Hand Dwelling house /Apartment'}, inplace=True)
df['SALE_DATE'] = pd.to_datetime(df['SALE_DATE'])
df['YEAR'], df['MONTH'] = df['SALE_DATE'].dt.year , df['SALE_DATE'].dt.month

#################################
df2020= df[df['YEAR'] == 2020]
SALE_STATS_MONTH = df2020.groupby('MONTH')['SALE_PRICE'].agg([np.min, np.max, np.mean, np.median])

mean = SALE_STATS_MONTH['mean']
for unique_values in df:
    month=(df['MONTH'].unique())

#print(mean)
#plt.scatter(x=year, y=mean, c=colours)
plt.bar(x=month, height=mean, bottom=0, color=['orange'])
plt.ylim(260000, 360000)
plt.xlabel('Month')
plt.ylabel('Sale Price (€)')
plt.title('Average Monthly Sale Price 2020')
plt.yticks([260000, 280000, 300000, 320000, 340000, 360000], ['260K', '280K', '300K', '320K', '340K', '360K'])
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
plt.show()
#print(df.head())

#plt.show()

#COUNTY PRICE STATS
#COUNTY_PRICE_STATS = df2020.groupby('COUNTY')['SALE_PRICE'].agg([np.min, np.max, np.mean, np.median])
#somean= COUNTY_PRICE_STATS['mean'].tolist()
#print(somean)
#plt.hist(somean, bins=32)
#plt.show()