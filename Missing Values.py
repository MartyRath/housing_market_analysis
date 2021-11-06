#Missing Values
#Checking if there are missing values
missing_values = file.isnull().sum()
#print(missing_values[0:])

#what percent of these missing values against total rows minus column row
total_rows = file.shape[0] - 1

# % POSTAL_CODE missing
missing_values_POSTAL_CODE = file['POSTAL_CODE'].isnull().sum() / total_rows * 100
print(missing_values_POSTAL_CODE)

# % PROPERTY_SIZE_DESC missing
missing_values_PROPERTY_SIZE_DESC = file['PROPERTY_SIZE_DESC'].isnull().sum() / total_rows * 100
print(missing_values_PROPERTY_SIZE_DESC)

#With over 80% missing in both cases, using these columns won't show valuable and accurate insights
#Dropping columns