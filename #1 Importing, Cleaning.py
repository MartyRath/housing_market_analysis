# Importing necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import seaborn as sns

# Importing CSV as DataFrame using Pandas
Leinster = pd.read_csv(r'C:\Users\User\PycharmProjects\MartyRath\Property_Price_Register_Ireland-28-05-2021.csv')
pd.options.display.width= None
pd.options.display.max_columns= None
Leinster.head()
Leinster.columns
Leinster.shape

# Checking date range using iloc. Range is 2010 - 2021-05-28
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

# Limiting data from 2010-2020. More rounded results, for calculations like cheapest month, as not including unfinished year 2021
Leinster = Leinster[Leinster['YEAR'] <= 2020]

# Alternatively, could have used loc to limit dates from 2010 to 2020
# Leinsterloc =Leinster.set_index('SALE_DATE') ; Leinsterloc.loc['2010':'2020']

# Creating a new CSV backup of Leinster (Leinster Property Price Register)
Leinster.to_csv(r'C:\Users\User\PycharmProjects\MartyRath\Leinster_PPR_2010-2020.csv')

# To merge excel for inflation column.
# Import: 'Inflation rate, average consumer prices (Annual percent change)'
inflation= pd.read_excel(r'C:\Users\User\PycharmProjects\MartyRath\Inflation rate, average consumer prices (Annual percent change).xls')

# Cleaning inflation Dataframe
inflation.drop(['Inflation rate, average consumer prices (Annual percent change)'],axis=1,inplace=True)
inflation.drop(labels=0, axis=0, inplace=True)
inflation.reset_index(drop=True, inplace=True)

# This is in the wrong shape to merge, with years as columns, as percentage change as the only row.
# Creating new Dataframe, extracting data as lists, then turning this to Dataframe.
percentages=inflation.values
percentages= percentages[0]
years=inflation.columns.tolist()
inflation=pd.DataFrame(
    {'YEAR': years,'INFLATION': percentages})

# Inflation Dataframe backup
inflation.to_csv(r'C:\Users\User\PycharmProjects\MartyRath\Inflation.csv')

# Merging 'inflation' with 'Leinster'
Leinster = Leinster.merge(inflation, on=['YEAR'])

# Creating alt Dataframes for exploratory convenience
Leinster2020= Leinster[Leinster['YEAR'] == 2020]
Leinster_budget=Leinster[Leinster['SALE_PRICE']<110000]
#Alternativively, could have used Leinster.loc[:, 'SALE_PRICE'], Leinster.iloc[:, 3]