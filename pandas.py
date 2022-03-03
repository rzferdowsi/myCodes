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

# Select Rows with Logic
#df[df.MyColumnName == desired_column_value]
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
january = df[df.month == 'January']
print(january)
print(type(january))

# df[(df.age < 30) | (df.name == 'Martha Jones')]
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
march_april = df[(df.month == "March") | (df.month == 'April')]
print(march_april)

# df[df.name.isin(['Martha Jones','Rose Tyler','Amy Pond'])]

f = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west'])
january_february_march = df[df.month.isin(['January', 'February','March'])]
print(january_february_march)

# Setting indices
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

df2 = df.loc[[1, 3, 5]]
print(df2)
df2.reset_index(inplace=True)

print(df2)

import pandas as pd
orders = pd.read_csv('shoefly.csv')
print(orders.head(10))
print(orders.info())
emails = orders.email
print(emails)
frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]
print(frances_palmer)
comfy_shoes = orders[orders.shoe_type.isin(['clogs','boots','ballet flats'])]
print(comfy_shoes)

#Modifying data
#df["new_col"]=[1,2,3] (a list) or df["new_col"]=0 (a constant value)
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Sold in Bulk?'] = ['Yes','Yes', 'No','No']
print(df)

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Is taxed?'] = 'Yes'
print(df)

import codecademylib3
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Is taxed?'] = 'Yes'
df['Margin'] = df.Price - df['Cost to Manufacture']
print(df)

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Add columns here
df['Lowercase Name'] = df.Name.apply(str.lower)
print(df)
# one line functions
mylambda = lambda k: k[0]+k[-1]
print(mylambda('This is a string'))

import codecademylib3
mylambda = lambda age: "Welcome to BattleCity!" if age >= 13 else  "You must be over 13"
print(mylambda(13))

df = pd.read_csv('employees.csv')

# Add columns here
get_last_name = lambda x: x.split(' ')[-1]
print(df)
df['last_name'] = df.name.apply(get_last_name)
print(df)

df = pd.read_csv('employees.csv')
print(df)
total_earned = lambda row: ((row.hours_worked - 40)*1.5 + 40) * row.hourly_wage if row.hours_worked > 40 else (row.hours_worked * row.hourly_wage)
# df['total_earned'] = df.apply(mylambda)

df['total_earned'] = df.apply(total_earned, axis = 1)
print(df)

df = pd.read_csv('imdb.csv')
# print(df.columns)
# Rename columns here
print(df)
df.columns= ["ID","Title","Category","Year Released","Rating"]
print(df)
df = pd.read_csv('imdb.csv')

# Rename columns here
df.rename(columns={'name':'movie_title'},inplace = True)
print(df)

import codecademylib3
import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders.head(5))

orders['shoe_source'] = orders.shoe_material.apply(lambda x: 'animal' if x =='leather'else 'vegan')
orders['salutation'] = orders.apply(lambda row: 'Dear Mr. ' + row['last_name'] if row['gender'] == 'male' else 'Dear Ms. ' + row['last_name'],axis=1)
print(orders.head(5))

"""Petal Power Inventory
You’re the lead data analyst for a chain of gardening stores called Petal Power. Help them analyze their inventory!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video."""

import pandas as pd
inventory = pd.read_csv('inventory.csv')
staten_island =(inventory.head(10))
print(staten_island)
print(inventory.info())
product_request = staten_island.product_description 
print(product_request)
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
print(seed_request)
s_ch = lambda x: True if x > 0 else False
inventory['in_stock'] = inventory.quantity.apply(s_ch)
print(inventory.head())
inventory['total_value'] = inventory.price * inventory.quantity 
print(inventory.head())
combine_lambda = lambda row: '{} - {}'.format(row.product_type,row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda,axis=1)
print(inventory.head())
