import codecademylib3

# Import pandas with alias
import pandas as pd

# import numpy with alias
import numpy as np

# import date class from datetime module
from datetime import date

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

# Examine the first five rows of census dataframe
print(census.head())

# Output each data type of the variables of the census dataframe
print(census.dtypes)

# Print the unique values of the 'birth_year' column
print(census['birth_year'].unique())

# Replace the 'missing' value in the 'birth_year' variable with 1967
census['birth_year'] = census['birth_year'].replace('missing', 1967)

# Print the unique values of the 'birth_year' column
print(census['birth_year'].unique())

# Switch the data type of the variable 'birth_year' to an integer
census['birth_year'] = census['birth_year'].astype('int')

# Display the data types of the census dataframe
print(census.dtypes)

# Print the average birth year
print(census['birth_year'].mean())

# Convert the higher_tax variable to the category data type
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)

# print out unique values in the higher_tax column
print(census['higher_tax'].unique())

# Lebel encode the 'higher_tax' variable
census['higher_tax'] = census['higher_tax'].cat.codes

# Print out the median of the higher_tax variable
print(census['higher_tax'].median())

# Print out the first 5 rows in the census dataframe
print(census.head())

# Display the unique values of the variable 'marital_status'
print(census.marital_status.unique())

# Convert the marital_status variable to the category data type
census['marital_status'] = pd.Categorical(census['marital_status'], ['single', 'married', 'divorced', 'widowed'], ordered=True)

# Create a variable called marital_codes by Label Encoding the marital_status variable
census['marital_codes'] = census['marital_status'].cat.codes

# Use get_dummies to OHE the marital_status
census = pd.get_dummies(data=census, columns=['marital_status'])

# Print out the first 5 rows in the census dataframe
print(census.head())

# Create an 'age' variable to hold the ages of the respondents
census['age'] = date.today().year - census['birth_year']

# Set age interval
age_intervals = np.arange(min(census['age']) - 4, 100, 5)

# Create a variable called age_group, which groups respondents based on their birth year
census['age_group'] = pd.cut(census['age'], bins=age_intervals)

# Lebel encode the 'age_group' variable
census['age_group'] = census['age_group'].cat.codes

# Print the first five rows of census dataframe
print(census.head())