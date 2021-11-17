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

df.drop(['Kerry', 'Clare'],axis=0,inplace=False)

print(df.head())
#index = [4,6,7,8,9,10,12,14,15,17,20,22,23,24]
#LEINSTER=np.delete(county, index)
#df['LEINSTER'] =
#SALE_STATS_COUNTY = df.groupby('COUNTY')['SALE_PRICE'].agg([np.min, np.max, np.mean, np.median])
#print(SALE_STATS_COUNTY)

#print(df2020.head())
#mean = SALE_STATS_COUNTY['mean']
#for unique_values in df:
 #   county=(df['COUNTY'].unique())

#index = [4,6,7,8,9,10,12,14,15,17,20,22,23,24]
#LEINSTER=np.delete(county, index)

#SALE_STATS_LEINSTER = df.groupby('LEINSTER')['SALE_PRICE'].agg(np.mean)


#plt.scatter(x=LEINSTER, y=mean, color=['green'])
plt.xlabel('County')
plt.ylabel('Sale Price (€)')
plt.title('Average Sale Price Per County')
#plt.yticks([200000, 220000, 240000, 260000, 280000, 300000, 320000], ['200K', '220K', '240K', '260K', '280K', '300K', '320K'])
#plt.show()

