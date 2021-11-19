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
DFLeinster = df[df['COUNTY'].isin(['Dublin', 'Laois', 'Meath', 'Kilkenny', 'Carlow', 'Wicklow', 'Wexford', 'Longford', 'Offaly', 'Kildare', 'Louth', 'Westmeath'])]

#################################
df2020= df[df['YEAR'] == 2020]
###################################################
#df.set_index('COUNTY', inplace=True)
#LEINSTER = df.loc[['Dublin', 'Laois', 'Meath', 'Kilkenny', 'Carlow', 'Wicklow', 'Wexford', 'Longford', 'Offaly', 'Kildare', 'Louth', 'Westmeath']]
#LEINSTER_AVG = LEINSTER.groupby('COUNTY')['SALE_PRICE'].agg(np.mean)
#counties=LEINSTER_AVG.index.tolist()
#plt.scatter(x=counties, y=LEINSTER_AVG, color=['green'])
#plt.show()

#fig, ax = plt.subplots()
#ax.plot(df2020['SALE_DATE'], df2020['SALE_PRICE'])
#plt.show()

Leinster = df['COUNTY'].isin(['Dublin', 'Laois', 'Meath', 'Kilkenny', 'Carlow', 'Wicklow', 'Wexford', 'Longford', 'Offaly', 'Kildare', 'Louth', 'Westmeath'])
DFLEINSTER = df[Leinster]

#print(DFLEINSTER.sort_values('SALE_PRICE', ascending=False))
#print(DFLEINSTER[DFLEINSTER['SALE_PRICE']<10000])
#print(DFLEINSTER['SALE_PRICE'].min())
#Wexford= DFLEINSTER[DFLEINSTER['COUNTY']=='Wexford']
#Wexford['SALE_PRICE'].min())
#df2020[(df2020['COUNTY']=='Wexford') & (df2020['SALE_PRICE']<100000)]) #In 2020 there were 258 houses sold in Wexford under 100K
Wexford=DFLEINSTER[DFLEINSTER['COUNTY']=='Wexford']
#(Wexford.sort_values('SALE_PRICE')) #THIS WORKS! Just not with Dublin, consider dropping DUB anyway
cheap=DFLEINSTER[DFLEINSTER['SALE_PRICE']<100000]
cheap2020 = DFLEINSTER[(DFLEINSTER['YEAR']==2020) & (DFLEINSTER['SALE_PRICE']<100000)]
#(cheap2020[['COUNTY','SALE_PRICE']].sort_values('SALE_PRICE'))
#print(df2020['SALE_PRICE'].mean())
LEINSTER2020=DFLEINSTER[DFLEINSTER['YEAR']==2020]
#(LEINSTER2020['SALE_PRICE'].mean())
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
print(LEINSTER2020['SALE_PRICE'].agg(iqr)) #because there's outliers in this data, IQR is preferred over standard deviation. Shows where the bulk of the data lies
print(LEINSTER2020['SALE_PRICE'].median())
cumstatsstop
