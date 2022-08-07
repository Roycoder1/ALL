from itertools import groupby
import numpy as np
import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
# print(df.head())
# # voir les index de 50 a 60
# print(df.iloc[50:60])
# res = df.loc [(df['species'] =='versicolor') & (df['petal_width'] ==1.4)]
# # print(res)
# # we can also use .filter 
# # df.filter('species'== ['versicolor']) 
# # groupby
# res1=df.groupby(by = ['species']).sum()
# res3= df.groupby(by = ['species', 'petal_length'])
# res4=df.groupby(by = ['species']).apply(np.mean)
# print(res4)
# # print(res3)
# # print(res1)
# # Sorting
# res2= df.sort_values(['petal_width'], ascending =False)
# # print (res2)
# Exercise:
# ex1= df.iloc[50]
# print(ex1)
# # ex2= df.iloc[50:60][['species', 'petal_length','petal_width']]
# # print(ex2)
# # ex3= df.groupby(by = ['species']).sum(['sepal_length'])
# # print(ex3)
# # ex4 = df[['species','sepal_length']].groupby('species').agg([np.mean,np.median,np.sum])
# # print(ex4)

# # exercise pdf

# #     Step 1. Import the necessary libraries
# #      Step 2. Import the dataset from this      
# # https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv 
# #      Step 3. Assign it to a variable called chipo.
# #      Step 4. See the first 10 entries
# #      Step 5. What is the number of observations in the dataset?

# chipo = pd.read_table("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv")
# b= chipo.describe()
# print(b)
# chipo.info()
# # print(chipo.info())
# ji= chipo['item_price'].iloc[:10]
# # print (ji)
# dollar_strip = lambda s:s.strip('$')
# hu= chipo['item_price'].apply(dollar_strip).apply(np.float64)
# # print(hu)
# # def dollar_strip(s):
# #     return s.strip('$')

# # dollar_strip()
# # arr32 = np.random.randint(1,10,size = (5,5),dtype= np.float64)
# v= chipo.info()
# # print(v)
# a= chipo.index.values.tolist()
# print(a)
# c= chipo.sort_values(['quantity'], ascending= True)
# items.sort_values([‘quantity’], ascending = False)
# print(c)
# np.mean(chipo['quantity']['price'])
# filtering and sorting
#    Step 1. Import the necessary libraries
#      Step 2. Import the dataset from this 
# https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv
#      Step 3. Assign it to a variable called chipo.
chipot = pd.read_table("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv")
chipot.info()
# print(chipot.head())
#      Step 4. How many products cost more than $10.00?
dollar_strip = lambda s:s.strip('$')
chipot['item_price'] = chipot['item_price'].apply(dollar_strip).apply(np.float64)

g = chipot.loc[chipot['item_price'] > 10.0].sum()
# print(g)
#      Step 5. What is the price of each item? 
groupchipot= chipot[['item_name','item_price']].groupby('item_price')
print (groupchipot)

#      print a data frame with only two columns item_name and item_price
data = chipot[['item_name','item_price']]
print (data)
#      Step 6. Sort by the name of the item
sorted = chipot.sort_values(['item_name'], ascending= True)
print(sorted)
#      Step 7. What was the quantity of the most expensive item ordered?
r= chipot.sort_values(['item_price'],ascending=False)
print(r)
#      Step 8. How many times were a Veggie Salad Bowl ordered?
p= np.count_nonzero(chipot.item_name == "Veggie Salad Bowl" )
print(p)
#      Step 9. How many times people orderd more than one Canned Soda?
canned = np.count_nonzero((chipot.item_name == "Canned Soda")&( chipot.quantity >1))
print(canned)

# Ex3 : 
#  Step 1. Import the necessary libraries
#  Step 2. Import the dataset from this 
# https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user
#  Step 3. Assign it to a variable called users.
#  Step 4. Discover what is the mean age per occupation
#  Step 5. Discover the Male ratio per occupation and sort it from the most to the least
#  Step 6. For each occupation, calculate the minimum and maximum ages
#  Step 7. For each combination of occupation and gender, calculate the mean age
#  Step 8. For each occupation present the percentage of women and men

nf = pd.read_table("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user",sep="|")
print(nf.head())
mean1 = nf.groupby('occupation').age.mean()
print(mean1)
nf['is_male'] = nf.gender.apply(lambda x: True if x == 'M' else False)
nf_true = nf.groupby('occupation').is_male.sum() / nf.groupby('occupation').gender.count().sort_values(ascending = False)
print(nf_true)



# 4. Merge
 
#  Step 1. Import the necessary libraries
#  Step 2. Create the 3 DataFrames based on the followin raw data
# raw_data_1 = {
#  'subject_id': ['1', '2', '3', '4', '5'],
#  'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
#  'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
# raw_data_2 = {
#  'subject_id': ['4', '5', '6', '7', '8'],
#  'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
#  'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
# raw_data_3 = {
#  'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
#  'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

raw_data_1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

raw_data_2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

raw_data_3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

data1 = pd.DataFrame(raw_data_1, columns = ['subject_id','first_name','last_name'])
print (data1)
data2 = pd.DataFrame(raw_data_2,columns = ['subject_id','first_name','last_name'])
print(data2)
data3 = pd.DataFrame(raw_data_3, columns = ['subject_id','test_id'])
print(data3)
#  Step 3. Assign each to a variable called data1, data2, data3
#  Step 4. Join the two dataframes along rows and assign all_data
joined = pd.concat([data1,data2])
print(joined)

#  Step 5. Join the two dataframes along columns and assing to all_data_col
all_data_col = pd.DataFrame([raw_data_1,raw_data_2],columns=['subject_id','first_name','last_name'])
print(all_data_col)
#  Step 6. Print data3
print(data3)
#  Step 7. Merge all_data and data3 along the subject_id value
merge1 = pd.merge(joined,data3 ,on = 'subject_id')
print(merge1)
#  Step 8. Merge only the data that has the same 'subject_id' on both data1 and data2
merge2 = pd.merge(data1,data2 , on = 'subject_id')
#  Step 9. Merge all values in data1 and data2, with matching records from both sides where 
merge3 = pd.merge(data1,data2, on='subject_id',how= 'outer')
print(merge3)
# available.


# 5. Deleting
# This exercise may seem a little bit strange, but keep doing it
 
#  Step 1. Import the necessary libraries
#  Step 2. Import the dataset from this
# https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
#  Step 3. Assign it to a variable called iris
#  Step 4. Create columns for the dataset
#  1. sepal_length (in cm)
#  2. sepal_width (in cm)
#  3. petal_length (in cm)
#  4. petal_width (in cm)
#  5. class
#  Step 5. Is there any missing value in the dataframe?Yes there is missing values
#  Step 6. Lets set the values of the rows 10 to 29 of the column 'petal_length' to NaN
#  Step 7. Good, now lets substitute the NaN values to 1.0
#  Step 8. Now let's delete the column class
#  Step 9. Set the first 3 rows as NaN
#  Step 10. Delete the rows that have NaN
#  Step 11. Reset the index so it begins with 0 again
# Create your own q

iris= pd.read_table("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(iris.head())
column_names = ['sepal_length','sepal_width','petal_length','petal_width','class']
go = pd.DataFrame(iris, columns=column_names)
print (go)
setvalue = iris['petal_length'][10:30] = np.nan
print(setvalue)
