import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Leinster = pd.read_csv(r'C:\Users\User\Desktop\UCD DATA\Leinster_PPR_2010-2020.csv')
inflation = pd.read_csv(r'C:\Users\User\Desktop\UCD DATA\Inflation.csv')

# CHART #6: 'Total Sales Distribution per Month in Leinster 2010-2020'
salespermonth= Leinster.groupby('MONTH')['COUNTY'].count()
salespermonth.plot(kind='bar', rot=45, title= 'Total Sales Distribution per Month in Leinster 2010-2020')
plt.show()
####################################
# Inflation 2010 - 2020
inflation= inflation[inflation['YEAR'] >= 2010]
inflation= inflation[inflation['YEAR'] <= 2020]
print(inflation)
fig, ax = plt.subplots()
ax.plot(inflation['YEAR'], inflation['INFLATION'])
#plt.show()



################################################

########################################################################
###################################################################################
#More or less sales in cheaper month
