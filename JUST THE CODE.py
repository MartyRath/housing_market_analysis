# Importing necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
# Importing CSV as DataFrame using Pandas
df = pd.read_csv(r'C:\Users\User\Desktop\UCD DATA\Test\Property_Price_Register_Ireland-28-05-2021.csv')
pd.options.display.width= None
pd.options.display.max_columns= None
df.head()
df.columns
df.shape
#here we see date range is 2010 - 2021-05-28
df.iloc[[0,-1]]
# Ensuring there isn't duplicate entries
df.drop_duplicates(subset=['SALE_DATE', 'ADDRESS'])
# Checking for missing values, with plot
missing_values = df.isna().sum()
missing_values.plot(kind='bar', rot=45, title='Missing Values')
#plt.show()
# Dropping unnecessary columns
df.drop(['POSTAL_CODE', 'PROPERTY_SIZE_DESC', 'ADDRESS', 'IF_MARKET_PRICE', 'IF_VAT_EXCLUDED'],axis=1,inplace=True)
# Noticed 'PROPERTY_DESC' seems to only have two values, 'New Dwelling...' and 'Second Hand Dwelling...'. Checking this.
for unique_values in df:
    unique_desc=df['PROPERTY_DESC'].unique()
#print(unique_desc)
# Found there are two entries, but some are in Irish. Replacing these to with English, so only two entries remain.
df['PROPERTY_DESC'].replace({'Teach/�ras�n C�naithe Nua': 'New Dwelling house /Apartment', 'Teach/?ras?n C?naithe Nua': 'New Dwelling house /Apartment', 'Teach/�ras�n C�naithe Ath�imhe': 'Second-Hand Dwelling house /Apartment'}, inplace=True)
# Formatting dates in 'SALE_DATE' to be usuable.
df['SALE_DATE'] = pd.to_datetime(df['SALE_DATE'])
# Creating two new columns, 'YEAR' and 'MONTH', for later convenience.
df['YEAR'], df['MONTH'] = df['SALE_DATE'].dt.year , df['SALE_DATE'].dt.month
# Focusing on Leinster properties, so modifying Dataframe to only contain counties in Leinster.
Leinster = df[df['COUNTY'].isin(['Dublin', 'Laois', 'Meath', 'Kilkenny', 'Carlow', 'Wicklow', 'Wexford', 'Longford', 'Offaly', 'Kildare', 'Louth', 'Westmeath'])]
# Creating a new CSV of Leinster (Leinster Property Price Register)
Leinster.to_csv(r'C:\Users\User\Desktop\UCD DATA\Leinster_PPR_2010-2020.csv')
# Will predominantly be using two Dataframes, 'Leinster', and then 'Leinster2020'
Leinster = df[df['YEAR'] <= 2020] #more rounded results, for calculations like cheapest month, as not including unfinished year 2021
Leinster2020= df[df['YEAR'] == 2020] #to contrast long-term vs. more recent data
#print(Leinster)




#*ARG against LOC
# Alternatively, could have used loc to create 'Leinster', 'Leinster2020'
#Leinsterloc =df.set_index('SALE_DATE') ; Leinsterloc.loc['2010':'2020'] #ALT 'Leinster' ; Leinster2020=Leinsterloc.loc['2020'] #ALT 'Leinster2020'
###################################################
# Merge 'Inflation rate, average consumer prices (Annual percent change)'
import xlrd
inflation= pd.read_excel(r'C:\Users\User\Desktop\Inflation rate, average consumer prices (Annual percent change).xls')
# Cleaning
inflation.drop(['Inflation rate, average consumer prices (Annual percent change)'],axis=1,inplace=True)
inflation.drop(labels=0, axis=0, inplace=True)
inflation.reset_index(drop=True, inplace=True)
# This is in the wrong shape to merge, with years as columns, as percentage change as the only row.
percentages=inflation.values
percentages= percentages[0]
years=inflation.columns.tolist()
inflation=pd.DataFrame(
    {'YEAR': years,'INFLATION': percentages})

Leinster_inflation = Leinster.merge(inflation, on=['YEAR'])
print(Leinster_inflation)

Leinster_inflation['SALE_ADJUSTED'] = Leinster_inflation['SALE_PRICE']*Leinster_inflation['INFLATION']
print(Leinster_inflation)
#WOULD NEED MODERN INFLATION AS REFERENCE


#.drop(labels=[1,15,20], axis=0)
#LEINSTER_AVG = LEINSTER.groupby('COUNTY')['SALE_PRICE'].agg(np.mean)
#counties=LEINSTER_AVG.index.tolist()
#plt.scatter(x=counties, y=LEINSTER_AVG, color=['green'])
#plt.show()
###################################################
#fig, ax = plt.subplots()
#ax.plot(df2020['SALE_DATE'], df2020['SALE_PRICE'])
#plt.show()
###################################################
#print(DFLEINSTER.sort_values('SALE_PRICE', ascending=False))
#print(DFLEINSTER[DFLEINSTER['SALE_PRICE']<10000])
#print(DFLEINSTER['SALE_PRICE'].min())
#Wexford= DFLEINSTER[DFLEINSTER['COUNTY']=='Wexford']
#Wexford['SALE_PRICE'].min())
#df2020[(df2020['COUNTY']=='Wexford') & (df2020['SALE_PRICE']<100000)]) #In 2020 there were 258 houses sold in Wexford under 100K
#Wexford=DFLEINSTER[DFLEINSTER['COUNTY']=='Wexford']
#(Wexford.sort_values('SALE_PRICE')) #THIS WORKS! Just not with Dublin, consider dropping DUB anyway
#cheap=DFLEINSTER[DFLEINSTER['SALE_PRICE']<100000]
#cheap2020 = DFLEINSTER[(DFLEINSTER['YEAR']==2020) & (DFLEINSTER['SALE_PRICE']<100000)]
#(cheap2020[['COUNTY','SALE_PRICE']].sort_values('SALE_PRICE'))
#print(df2020['SALE_PRICE'].mean())
#LEINSTER2020=DFLEINSTER[DFLEINSTER['YEAR']==2020]
#(LEINSTER2020['SALE_PRICE'].mean())
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
#print(LEINSTER2020['SALE_PRICE'].agg(iqr)) #because there's outliers in this data, IQR is preferred over standard deviation. Shows where the bulk of the data lies
#print(LEINSTER2020['SALE_PRICE'].median())

#print(DFLEINSTER.drop_duplicates(subset='COUNTY')) # See individual counties. (for multiple conditions, pass list [] to subset)


#cheapzz = DFLEINSTER[DFLEINSTER['SALE_PRICE']<100000]
#cheapzz['COUNTY'].value_counts(sort=True) # how many sold per county under 100K
#PPC_under100K = cheapzz['COUNTY'].value_counts(normalize=True) #proportions houses sold under 100K per county

#DFLEINSTER[DFLEINSTER['COUNTY']=='Dublin']['SALE_PRICE'].mean() #Average price in Dublin of houses sold
#mean_sale=DFLEINSTER.groupby('COUNTY')['SALE_PRICE'].mean() #AVG per county (can use agg multiple functions, can add list to county or sale price bits)
#mean_sale.sort_values(ascending=False) #Sorting average high to low

#cheapzz['COUNTY'].hist(bins=12) #confusing

#mean_sale.plot(kind='bar', title='Average Property Price in Leinster 2010-2020', rot=45) #USE THIS. adjust image in bar showapplication
#plt.show()