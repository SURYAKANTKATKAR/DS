import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sales = pd.read_csv('supermarket_sales.csv')
sales.head()
sales.tail()
sales.shape
sales.isnull().sum()
sales.count()
sales.sum()
sales['Total'].sum()
sales[['Total','gross income']].sum()
sales.mean(numeric_only="True")
sales['Rating'].mean()
sales.std(numeric_only="True")
sales['Rating'].std()
print('The Mode of : ',sales['Payment'].mode)
sales['Payment'].mode()  
sales['Quantity'].min()           
sales['Quantity'].max()
sales['Total'].cumsum().head()     
sales['Total'].head()
median = sales['Quantity'].median()
median
print('median quantity: ' + str(median))
var = sales['Quantity'].var()
var
print('var of quantity: ' + str(var))
groupby_sum = sales.groupby(['City']).sum()
groupby_sum
groupby_count = sales.groupby(['City']).count()
groupby_count
groupby_sum1 = sales.groupby(['Payment']).sum()
groupby_sum1
groupby_count1 = sales.groupby(['Payment']).count()
groupby_count1
print('sum of values, grouped by the payment: ' + str(groupby_sum1))
print('count of values, grouped by the payment: ' + str(groupby_count1))
sales.describe() 
sales.describe(include='object')
sales.describe(include='all')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('Iris.csv')
iris.head()
iris.tail()
iris.shape
print(iris.columns)
iris.isnull().sum()
iris.describe()
iris['Species'].value_counts()
iris.plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm')
plt.show()
iris.mean(numeric_only="True")
iris.Species.mode()
import seaborn as sns
sns.set_style("whitegrid")
sns.FacetGrid(iris, hue="Species", height=7).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend()
plt.show()
setosa_data = iris[iris['Species'] == 'Iris-setosa']
versicolor_data = iris[iris['Species'] == 'Iris-versicolor']
setosa_data
versicolor_data
setosa_stats = {
    'percentile': np.percentile(setosa_data['SepalLengthCm'], 50),
    'mean': np.mean(setosa_data['SepalLengthCm']),
    'std_dev': np.std(setosa_data['SepalLengthCm'])
}
versicolor_stats = {
    'percentile': np.percentile(versicolor_data['SepalLengthCm'], 50),
    'mean': np.mean(versicolor_data['SepalLengthCm']),
    'std_dev': np.std(versicolor_data['SepalLengthCm'])
}
print('Statistics for Iris Setosa:')
print(setosa_stats)
print('')

print('Statistics for Iris Versicolor:')
print(versicolor_stats)
