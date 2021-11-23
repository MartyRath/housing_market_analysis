import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Leinster = pd.read_csv(r'C:\Users\User\Desktop\UCD DATA\Leinster_PPR_2010-2020.csv')
inflation = pd.read_csv(r'C:\Users\User\Desktop\UCD DATA\Inflation.csv')
Leinster_budget=Leinster[Leinster['SALE_PRICE']<110000]

##############################################################################################################
# CHART #1: 'Average Sale Price in Leinster 2010-2020'
SALE_PRICE_STATS = Leinster.groupby('YEAR')['SALE_PRICE'].agg([np.min, np.max, np.mean, np.median])

mean = SALE_PRICE_STATS['mean']
#Getting list of years, alt to just using .unique()
for unique_values in Leinster:
    years=(Leinster['YEAR'].unique()) #output= years 2010-2020

plt.bar(x=years, height=mean, color=['green'])
plt.xlabel('Year')
plt.ylabel('Sale Price (€)')
plt.title('Average Sale Price per Year in Leinster 2010-2020')
#plt.show()
##############################################################################################################
# CHART #2: 'Inflation in Ireland 2010-2020 (%)'
inflation= inflation[inflation['YEAR'] >= 2010]
inflation= inflation[inflation['YEAR'] <= 2020]
inflation.plot(x='YEAR', y='INFLATION', kind='line', title= 'Inflation in Ireland 2010-2020 (%)')
#plt.show()
##############################################################################################################
# CHART #3: 'Average Sale Price per Year in Leinster 2010-2020'
mean_yearly = Leinster.groupby('YEAR')['SALE_PRICE'].mean()
mean_yearly.plot(x='YEAR', y='mean', kind='line', title='Average Sale Price per Year in Leinster 2010-2020')
#plt.show()
##############################################################################################################
# CHART #4: 'Average Sale Price per County in Leinster 2010-2020'
mean_sale=Leinster.groupby('COUNTY')['SALE_PRICE'].mean() #AVG per county
mean_sale=mean_sale.sort_values() #Sorting average low to high
colours= ['green', 'green', 'green', 'green', 'green', 'green', 'yellow', 'yellow', 'red', 'red', 'red', 'purple']
mean_sale.plot(kind='bar', title='Average Sale Price per County in Leinster 2010-2020', rot=45, color=colours)
#plt.show()
##############################################################################################################
# CHART #5: 'Average Monthly Sale Prices in Leinster 2010-2020'
SALE_STATS_MONTH = Leinster.groupby('MONTH')['SALE_PRICE'].mean()
mean = SALE_STATS_MONTH
months = Leinster['MONTH'].unique()

plt.bar(x=months, height=mean, color=['orange'])
plt.ylim(280000, 350000)
plt.xlabel('Month')
plt.ylabel('Sale Price (€)')
plt.title('Average Monthly Sale Prices in Leinster 2010-2020')
plt.yticks([280000, 290000, 300000, 310000, 320000, 330000, 340000, 350000], ['280K', '290K', '300K', '310K', '320K', '330K', '340K', '350K'])
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
#plt.show()
##############################################################################################################
# CHART #6: 'Total Sales Distribution per Month in Leinster 2010-2020'
distribution=sns.countplot(x='MONTH', data=Leinster)
distribution.set_title('Total Sales Distribution per Month in Leinster 2010-2020')
distribution.set_xticklabels(['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
#plt.show()
