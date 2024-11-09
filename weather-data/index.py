import pandas as pd
data = pd.read_csv(r"C:yourfilepath\weather-data\weather-datasets.csv")
print(data.head()) # first N rows in the data 
print(data.shape) # total no. of rows and no. of columns of the dataframe
print(data.index) # index of the dataframe
print(data.columns) # name of each column
print(data.dtypes) # data type of each column
print(data['Weather'].unique()) # all the unique values
print(data.nunique()) # total no. of unique values in each column
print(data.count()) # total no. of non-null values in each column.
print(data['Weather'].value_counts()) # all the unique values with their count
