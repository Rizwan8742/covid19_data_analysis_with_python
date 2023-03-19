import pandas as pd
import requests

#Step 1 Data Collection
url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'
response = requests.get(url)
data_list = pd.read_html(response.text)
target_df = data_list[12]

#Step 2 Data Cleaning

#Issue 1 Column Names
target_df.columns = ['col0','Country Name','Deaths/Million','Total Deaths','Total Cases']
#Issue 2 Extra Columns
target_df = target_df[['Country Name','Deaths/Million','Total Deaths','Total Cases']]
#Issue 3 Extra Rows
target_df = target_df.drop([0])
last_index = target_df.index[-1]
for i in range(229,last_index+1):
    target_df = target_df.drop([i])
 #Issue 4 Inconsistent Country Name  
target_df['Country Name'] = target_df['Country Name'].str.replace('\[.*\]','')

#Issue 5 Wrong Data types
target_df['Total Deaths'] = pd.to_numeric(target_df['Total Deaths'])
target_df['Total Cases'] = pd.to_numeric(target_df['Total Cases'])
target_df['Deaths/Million'] = pd.to_numeric(target_df['Deaths/Million'])

#step 3 Export The Data
target_df.to_csv(r'covid19_dataset.csv')
target_df.to_excel(r'covid19_dataset.xlsx')