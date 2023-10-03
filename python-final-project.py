# -*- coding: utf-8 -*-

# -- Project --

# # Final Project - Analyzing Sales Data
# 
# **Date**: 24 August 2023
# 
# **Author**: Pan Thunkarn
# 
# **Course**: `Pandas Foundation`


# import data
import pandas as pd
df = pd.read_csv("sample-store.csv")

# preview top 5 rows
df.head()

# shape of dataframe
df.shape

# see data frame information using .info()
df.info()

# We can use `pd.to_datetime()` function to convert columns 'Order Date' and 'Ship Date' to datetime.


# example of pd.to_datetime() function
pd.to_datetime(df['Order Date'].head(), format='%m/%d/%Y')

# TODO - convert order date and ship date to datetime in the original dataframe
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')

df.head()

# TODO - count nan in postal code column
df['Postal Code'].isna().sum()

# TODO - filter rows with missing values
df[df['Postal Code'].isna()]

# TODO - Explore this dataset on your owns, ask your own questions
## How many segments and count each segments
df['Segment'].value_counts()

## Which segment has more profit?
### Consumer
df.groupby('Segment')['Profit'].mean()

# ## Data Analysis Part
# 
# Answer 10 below questions to get credit from this course. Write `pandas` code to find answers.


# TODO 01 - how many columns, rows in this dataset
num_of_rows = df.shape[0]
num_of_cols = df.shape[1]

print(f'there are {num_of_rows} rows and {num_of_cols} columns')

# TODO 02 - is there any missing values?, if there is, which colunm? how many nan values?
missing_values = df.isnull()

for column in missing_values.columns:
  if missing_values[column].any():
    print(f"Column {column} has {missing_values[column].sum()} missing values")

# TODO 02.1 - missing rows?
missing_rows = df.isnull().any(axis=1)

# Print the rows with missing values
for row in missing_rows.index:
  if missing_rows[row]:
    print(f"Row {row} has missing values")

# TODO 03 - your friend ask for `California` data, filter it and export csv for him
df_california = df.query('State == "California"')
df_california.to_csv("df_california.csv")

# TODO 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
## create new column (order_date_year)
df['order_date_year'] = df['Order Date'].dt.year

df_2017 = df.query('order_date_year == 2017')
df_2017_tc = df_2017.query('State == "California" | State == "Texas"')
df_2017_tc.to_csv("df_2017_tc.csv")

# TODO 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017
df_2017['Sales'].agg(['sum', 'mean', 'std']).reset_index()

print(f"The total sales in 2017 is {round(df_2017['Sales'].sum(), 2)} USD with average sales {round(df_2017['Sales'].mean(), 2)} USD and standard diviation is {round(df_2017['Sales'].std(),2)}")

# TODO 06 - which Segment has the highest profit in 2018
df_2018 = df.query('order_date_year == 2018')

df_2018.groupby('Segment')['Profit'].sum().idxmax()

# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
df07 = df[(df['Order Date'] >= "2019-04-15") & (df['Order Date'] <= "2019-12-31")]

df07.groupby('State')['Sales'].sum().sort_values().head(5).reset_index()

# TODO 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 
df2019 = df.query('order_date_year == 2019')
df2019_total_sales = df2019['Sales'].sum()
df2019_wc = df2019.groupby('Region')['Sales'].sum()[['West', 'Central']].sum()

print(f"propotional sales of Central and West is {round((df2019_wc/df2019_total_sales)*100 , 2)}%")

# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
df1920 = df.query('order_date_year == 2019 | order_date_year == 2020')
df1920_total_sales = df1920['Sales'].sum()
df1920_sales_topten = df1920.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10).sum()

print(f"top ten products sales is {round((df1920_sales_topten/df1920_total_sales)*100 , 2)}% from total sales")

# TODO 09.1 correction using quantity instead of sales.
df1920_sales_topten_quant = df1920.groupby('Product Name')[['Quantity', 'Sales']].sum().sort_values('Quantity', ascending=False)\
    .head(10).sum()['Sales']

print(f"top ten products sales by number of orders (quantity) is {round((df1920_sales_topten_quant/df1920_total_sales)*100 , 2)}% from total sales")

# TODO 10 - plot at least 2 plots, any plot you think interesting :)
#10.1 graph show total sales in each segment on year 2018
df1920.groupby('Segment')['Sales'].sum().plot(x='Segment', y='Sales', kind='bar', color = ['salmon', 'orange', 'brown'])

# TODO Bonus - use np.where() to create new column in dataframe to help you answer your own questions
import numpy as np

## order that Sales more than 100.00
df['sales_more_than_100'] = np.where(df['Sales'] >= 100, True, False)
df
