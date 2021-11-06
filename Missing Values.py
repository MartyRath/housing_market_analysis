#Missing Values
#Checking if there are missing values
missing_values = file.isnull().sum()
#print(missing_values[0:])

#what percent of these missing values against total rows minus column row
total_rows = file.shape[0] - 1

# % POSTAL_CODE missing values
#missing_values_POSTAL_CODE = file['POSTAL_CODE'].isnull().sum() / total_rows * 100
#print(missing_values_POSTAL_CODE)

# % PROPERTY_SIZE_DESC missing values
#missing_values_PROPERTY_SIZE_DESC = file['PROPERTY_SIZE_DESC'].isnull().sum() / total_rows * 100
#print(missing_values_PROPERTY_SIZE_DESC)

#With over 80% missing in both cases, using these columns won't show valuable and accurate insights
#Dropping columns POSTAL_CODE and PROPERTY_SIZE_DESC due to missing values
file.drop(['POSTAL_CODE', 'PROPERTY_SIZE_DESC'],axis=1,inplace=True)
#print(file.head())

#If I wanted to replace missing values, I could have executed the following two lines:
#file['POSTAL_CODE'] = file['POSTAL_CODE'].fillna('Unknown')
#file['PROPERTY_SIZE_DESC'] = file['PROPERTY_SIZE_DESC'].fillna('Unknown')