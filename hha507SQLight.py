import pandas as pd
import sqlite3

#Create a connection to SQLite database
conn = sqlite3.connect('obesity.db')

#read in data 
data = pd.read_csv('https://data.cdc.gov/api/views/3nzu-udr9/rows.csv?accessType=DOWNLOAD',sep=',')
print(data.head())

#Save the DataFrame to the SQLite database
data.to_sql('health',conn, if_exists='replace', index=False)

#Test a query
query = 'SELECT * FROM health'
result_df = pd.read_sql(query, conn)
print(result_df)

#querys for assignment 

#Gets all info where the year = 2015-2018
query1 = 'Select * From health WHERE year = "2015-2018"'
result_df1 = pd.read_sql(query1, conn)
print(result_df1)

#Gets a count of rows that have year = 2015-2018
query2 = 'Select year From health WHERE year = "2015-2018"'
result_df2 = pd.read_sql(query2, conn)
print(result_df2.count())

#Calculates Overall Average percentage of male population that is considered normal weight from 1988-2018 for age adjusted population
query3 = 'Select Estimate From health WHERE (STUB_LABEL_NUM = 2.1 AND UNIT = "Percent of population, age-adjusted" AND PANEL_NUM = 1)'
result_df3 = pd.read_sql(query3, conn)
print(result_df3.mean())

#Returns all data where Stub_label = Male: Not Hispanic or Latino: White only
query4 = 'Select * From health WHERE STUB_LABEL = "Male: Not Hispanic or Latino: White only"'
result_df4 = pd.read_sql(query4, conn)
print(result_df4.head())