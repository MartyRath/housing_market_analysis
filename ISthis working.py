#CHART #1 House prices are rising year by year, buy now. Think adding GDP rise per year too
SALE_PRICE_STATS = Leinster.groupby('YEAR')['SALE_PRICE'].agg([np.min, np.max, np.mean, np.median])

mean = SALE_PRICE_STATS['mean']
for unique_values in Leinster:
    year=(Leinster['YEAR'].unique())

plt.bar(x=year, height=mean, color=['green'])
plt.xlabel('Year')
plt.ylabel('Sale Price (€)')
plt.title('Average Sale Price in Leinster 2010-2020')
#plt.show()
#################################################################
#####DONE - Cheapest counties: 'Mean Property Price in Leinster 2010-2020'#######
mean_sale=Leinster.groupby('COUNTY')['SALE_PRICE'].mean() #AVG per county
mean_sale=mean_sale.sort_values() #Sorting average low to high
#print(mean_sale)
colours= ['green', 'green', 'green', 'green', 'green', 'green', 'yellow', 'yellow', 'red', 'red', 'red', 'purple']
#mean_sale.plot(kind='bar', title='Average Property Price in Leinster 2010-2020', rot=45, color=colours)
#plt.show()
#################################################################################################################

#################################################################################
#DONE - CHART2 WHICH MONTH CHEAPEST? Noteworthy drop in house price sales in May
SALE_STATS_MONTH = Leinster.groupby('MONTH')['SALE_PRICE'].agg([np.min, np.max, np.mean, np.median])
print(SALE_STATS_MONTH)

mean = SALE_STATS_MONTH['mean']
for unique_values in Leinster:
    month=(Leinster['MONTH'].unique())

plt.bar(x=month, height=mean, color=['orange'])
plt.ylim(280000, 350000)
plt.xlabel('Month')
plt.ylabel('Sale Price (€)')
plt.title('Average Monthly Sale Prices Leinster 2010-2020')
plt.yticks([280000, 290000, 300000, 310000, 320000, 330000, 340000, 350000], ['280K', '290K', '300K', '310K', '320K', '330K', '340K', '350K'])
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12], ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
plt.show()
############################################################################################################
###############################
# Inflation 2010 - 2020
inflation= inflation[inflation['YEAR'] >= 2010]
inflation= inflation[inflation['YEAR'] <= 2020]
print(inflation)
fig, ax = plt.subplots()
ax.plot(inflation['YEAR'], inflation['INFLATION'])
plt.show()
################################

################################################

########################################################################
###################################################################################
#More or less sales in cheaper month
