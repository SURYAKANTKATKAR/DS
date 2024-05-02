import pandas as pd
import numpy as np 
df = pd.read_csv("covid_19_clean_complete_2022.csv")
df.head()
df.isna().any()
df.describe()                     
df.shape            
df.dtypes           
df['Date'] = pd.to_datetime(df['Date'])
df['Country/Region'] = df['Country/Region'].astype('string')
df.dtypes
x=pd.get_dummies(df['WHO Region'])
df.drop('Province/State', axis=1, inplace=True)
df=pd.concat([df,x],axis=1)
df
df = df.drop(['WHO Region','Country/Region'], axis=1)
df.head()
