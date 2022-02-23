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
  [3,	'San Francisco', 90], 
  [4,	'Sacramento',	115]
  # Fill in rows 3 and 4
],
  columns=['Store ID', 'Location','Number of Employees'
    #add column names here
  ])
print(df2.Location)
print(df2)

#Loading and Saving CSVs
import codecademylib3
import pandas as pd
df= pd.read_csv('sample.csv')
print(df)

#writing to a csv file
df.to_csv('new-csv-file.csv')

# Inspect a DataFrame

import codecademylib3
import pandas as pd
#load the CSV below:
df = pd.read_csv('imdb.csv')
print(df.head())
print("\n----------------------------\n")
print(df.info())

# Select Columns

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
clinic_north = df.clinic_north 
print(clinic_north,type(clinic_north ) )

#  Selecting Multiple Columns

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
clinic_north_south = df[['clinic_north','clinic_south']]

print(clinic_north_south,"\n",type(clinic_north_south))

# Select Rows
import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])
march = df.iloc[1:4:2]
print(march, type(march))

#  Selecting Multiple Rows

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
april_may_june = df.iloc[3:6]
print(april_may_june)
