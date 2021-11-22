# Importing necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import seaborn as sns
# Importing CSV as DataFrame using Pandas
Leinster = pd.read_csv(r'C:\Users\User\Desktop\UCD DATA\Test\Property_Price_Register_Ireland-28-05-2021.csv')
pd.options.display.width= None
pd.options.display.max_columns= None
Leinster.head()
Leinster.columns
Leinster.shape

#here we see date range is 2010 - 2021-05-28
Leinster.iloc[[0,-1]]

# Ensuring there isn't duplicate entries
Leinster.drop_duplicates(subset=['SALE_DATE', 'ADDRESS'])

# Checking for missing values, with plot
missing_values = Leinster.isna().sum()
#missing_values.plot(kind='bar', rot=45, title='Missing Values')
#plt.show()

# Dropping unnecessary columns
Leinster.drop(['POSTAL_CODE', 'PROPERTY_SIZE_DESC', 'ADDRESS', 'IF_MARKET_PRICE', 'IF_VAT_EXCLUDED'],axis=1,inplace=True)

# Noticed 'PROPERTY_DESC' seems to only have two values, 'New Dwelling...' and 'Second Hand Dwelling...'. Checking this.
for unique_values in Leinster:
    unique_desc=Leinster['PROPERTY_DESC'].unique()

# Found there are two entries, but some are in Irish. Replacing these to with English, and shortening, so only two entries remain, 'New', 'Second-Hand'.
Leinster['PROPERTY_DESC'].replace({'Teach/�ras�n C�naithe Nua': 'New',
                             'Teach/?ras?n C?naithe Nua': 'New',
                             'Teach/�ras�n C�naithe Ath�imhe': 'Second-Hand',
                             'Second-Hand Dwelling house /Apartment': 'Second-Hand',
                             'New Dwelling house /Apartment': 'New'}, inplace=True)
# Formatting dates in 'SALE_DATE' to be usuable.
Leinster['SALE_DATE'] = pd.to_datetime(Leinster['SALE_DATE'])

# Creating two new columns, 'YEAR' and 'MONTH', for later convenience.
Leinster['YEAR'], Leinster['MONTH'] = Leinster['SALE_DATE'].dt.year , Leinster['SALE_DATE'].dt.month

# Focusing on Leinster properties, so modifying Dataframe to only contain counties in Leinster.
Leinster = Leinster[Leinster['COUNTY'].isin(['Dublin', 'Laois', 'Meath', 'Kilkenny', 'Carlow', 'Wicklow', 'Wexford', 'Longford', 'Offaly', 'Kildare', 'Louth', 'Westmeath'])]

# Creating a new CSV of Leinster (Leinster Property Price Register)
Leinster.to_csv(r'C:\Users\User\Desktop\UCD DATA\Leinster_PPR_2010-2020.csv')

# Limiting data from 2010-2020. More rounded results, for calculations like cheapest month, as not including unfinished year 2021
Leinster = Leinster[Leinster['YEAR'] <= 2020]

# Alternatively, could have used loc to create 'Leinster'
# Leinsterloc =Leinster.set_index('SALE_DATE') ; Leinsterloc.loc['2010':'2020']

# Merge. Import: 'Inflation rate, average consumer prices (Annual percent change)'
inflation= pd.read_excel(r'C:\Users\User\Desktop\Inflation rate, average consumer prices (Annual percent change).xls')

# Cleaning inflation dataframe
inflation.drop(['Inflation rate, average consumer prices (Annual percent change)'],axis=1,inplace=True)
inflation.drop(labels=0, axis=0, inplace=True)
inflation.reset_index(drop=True, inplace=True)

# This is in the wrong shape to merge, with years as columns, as percentage change as the only row.
percentages=inflation.values
percentages= percentages[0]
years=inflation.columns.tolist()
inflation=pd.DataFrame(
    {'YEAR': years,'INFLATION': percentages})

# Mergining Inflation with Leinster
Leinster = Leinster.merge(inflation, on=['YEAR'])

Leinster2020= Leinster[Leinster['YEAR'] == 2020]
Leinster_budget=Leinster[Leinster['SALE_PRICE']<110000]
#################################################################################
###############################
# Which county has most cheap houses?
salespermont= Leinster_budget['COUNTY']
#print(Leinster_budget)
#salespermonth.plot(kind='bar', rot=45)
plt.show()
# Are second hand houses much cheaper?
oldnew = Leinster.groupby('PROPERTY_DESC')['SALE_PRICE'].mean()
#print(oldnew)

# not much difference, though worth checking under 100K
oldnewwithbudget= Leinster_budget.groupby('PROPERTY_DESC')['SALE_PRICE'].mean()
#print(oldnewwithbudget)
#Distribution house prices under 100K


#print(Leinster.sort_values('SALE_PRICE', ascending=False))
#print(Leinster[Leinster['SALE_PRICE']<110000])
#print(Leinster['SALE_PRICE'].min())
#Wexford= Leinster[Leinster['COUNTY']=='Wexford']
#Wexford['SALE_PRICE'].min())
#Leinster2020[(Leinster2020['COUNTY']=='Wexford') & (Leinster2020['SALE_PRICE']<100000)]) #In 2020 there were 258 houses sold in Wexford under 100K
#Wexford=Leinster[Leinster['COUNTY']=='Wexford']
#(Wexford.sort_values('SALE_PRICE')) #THIS WORKS! Just not with Dublin, consider dropping DUB anyway
#cheap=Leinster[Leinster['SALE_PRICE']<100000]
#cheap2020 = Leinster[(Leinster['YEAR']==2020) & (Leinster['SALE_PRICE']<100000)]
#(cheap2020[['COUNTY','SALE_PRICE']].sort_values('SALE_PRICE'))
#print(Leinster2020['SALE_PRICE'].mean())
#Leinster2020=Leinster[Leinster['YEAR']==2020]
#(Leinster2020['SALE_PRICE'].mean())
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
#print(Leinster2020['SALE_PRICE'].agg(iqr)) #because there's outliers in this data, IQR is preferred over standard deviation. Shows where the bulk of the data lies
#print(Leinster2020['SALE_PRICE'].median())

#print(Leinster.drop_duplicates(subset='COUNTY')) # See individual counties. (for multiple conditions, pass list [] to subset)


#cheapzz = Leinster[Leinster['SALE_PRICE']<100000]
#cheapzz['COUNTY'].value_counts(sort=True) # how many sold per county under 100K
#PPC_under100K = cheapzz['COUNTY'].value_counts(normalize=True) #proportions houses sold under 100K per county

#Leinster[Leinster['COUNTY']=='Dublin']['SALE_PRICE'].mean() #Average price in Dublin of houses sold
###############
#sully.plot(x=’date’, y=’weight’, kind=’line’, rot=45)
#
#start 278554.521035
##########