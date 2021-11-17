#CHART #1 House prices are rising year by year, buy now. Think adding GDP rise per year too
SALE_PRICE_STATS = df.groupby('YEAR')['SALE_PRICE'].agg([np.min, np.max, np.mean, np.median])

mean = SALE_PRICE_STATS['mean']
for unique_values in df
    year=(df['YEAR'].unique())

plt.bar(x=year, height=mean, color=['green'])
plt.xlabel('Year')
plt.ylabel('Sale Price (€)')
plt.title('Average Sale Price Per Year')
plt.yticks([200000, 220000, 240000, 260000, 280000, 300000, 320000], ['200K', '220K', '240K', '260K', '280K', '300K', '320K'])
#plt.show()
#################################################################
#CHART2 Noteworthy drop in house price sales in May
SALE_STATS_MONTH = df.groupby('MONTH')['SALE_PRICE'].agg([np.min, np.max, np.mean, np.median])

mean = SALE_STATS_MONTH['mean']
for unique_values in df:
    month=(df['MONTH'].unique())

plt.bar(x=month, height=mean, color=['orange'])
plt.ylim(230000, 270000)
plt.xlabel('Month')
plt.ylabel('Sale Price (€)')
plt.title('Average Monthly Sale Price 2010-2021')
plt.yticks([230000, 240000, 250000, 260000, 270000], ['230K', '240K', '250K', '260K', '270K'])
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
#plt.show()
################################################
#CHART3 Average monthly sale prices. Heightens theory May is the best time to buy
df2020= df[df['YEAR'] == 2020]
SALE_STATS_MONTH = df2020.groupby('MONTH')['SALE_PRICE'].agg([np.min, np.max, np.mean, np.median])

mean = SALE_STATS_MONTH['mean']
for unique_values in df:
    month=(df['MONTH'].unique())

plt.bar(x=month, height=mean, color=['orange'])
plt.ylim(260000, 360000)
plt.xlabel('Month')
plt.ylabel('Sale Price (€)')
plt.title('Average Monthly Sale Price 2020')
plt.yticks([260000, 280000, 300000, 320000, 340000, 360000], ['260K', '280K', '300K', '320K', '340K', '360K'])
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
#plt.show()
########################################################################
#Super quick missing values bar chart
missing_values.plot.bar()
plt.show()
###################################################################################
#More or less sales in cheaper month