import pandas as pd

# converting dictionary to dataframe
df1 = pd.DataFrame({ 'Product ID': [1, 2, 3, 4], 'Product Name':['t-shirt','t-shirt','skirt','skirt'],'Color':['blue','green','red','black']
  # add Product Name and Color here
})
print(df1)
print(df1.info)

# converting list of list to dataframe, having a list of columns 
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3,	'San Francisco',	90], 
  [4,	'Sacramento',	115]
  # Fill in rows 3 and 4
],
  columns=['Store ID', 'Location','Number of Employees'
    #add column names here
  ])
print(df2.Location)
print(df2)
