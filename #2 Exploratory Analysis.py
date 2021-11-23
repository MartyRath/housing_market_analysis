import pandas as pd
import numpy as np

Leinster = pd.read_csv(r'C:\Users\User\PycharmProjects\MartyRath\Leinster_PPR_2010-2020.csv')
inflation = pd.read_csv(r'C:\Users\User\PycharmProjects\MartyRath\Inflation.csv')
Leinster_budget=Leinster[Leinster['SALE_PRICE']<110000]
Leinster2020= Leinster[Leinster['YEAR'] == 2020]

SALE_PRICE_STATS = Leinster2020.groupby('YEAR')['SALE_PRICE'].agg([np.min, np.max, np.mean, np.median])
#print(SALE_PRICE_STATS)

# Are second hand houses much cheaper?
oldnew = Leinster.groupby('PROPERTY_DESC')['SALE_PRICE'].mean() # not much difference
#print(oldnew)

# Cheapest houses sold in 2020 # 6500 cheapest
Leinster2020.sort_values('SALE_PRICE')

# How many houses sold for under 110K in 2020 # 1845
Leinster2020[Leinster2020['SALE_PRICE']<110000]

# Cheapest houses in 2020 by county=Wexford # 6500 cheapest
Wexford= Leinster2020[Leinster2020['COUNTY']=='Wexford']
Wexford['SALE_PRICE'].min()

# How many houses sold under 110K in Wexford 2020 # 296
Leinster2020[(Leinster2020['COUNTY']=='Wexford') & (Leinster2020['SALE_PRICE']<110000)]

# Custom code using IQR, instead of standard deviation, as there's outliers in property prices. This shows where most of the data lies.
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
IQR2020 = Leinster2020['SALE_PRICE'].agg(iqr)
#print(IQR2020) # 196500.0