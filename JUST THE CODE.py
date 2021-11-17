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
###################################################
df.set_index('COUNTY', inplace=True)
LEINSTER = df.loc[['Dublin', 'Laois', 'Meath', 'Kilkenny', 'Carlow', 'Wicklow', 'Wexford', 'Longford', 'Offaly', 'Kildare', 'Louth', 'Westmeath']]
LEINSTER_AVG = LEINSTER.groupby('COUNTY')['SALE_PRICE'].agg(np.mean)
counties=LEINSTER_AVG.index.tolist()
plt.scatter(x=counties, y=LEINSTER_AVG, color=['green'])
plt.show()

