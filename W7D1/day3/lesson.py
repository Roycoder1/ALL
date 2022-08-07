# ex1 :
from turtle import color
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# pt = np.random.randint(0,75,100)
# print(pt)
# colors = np.random.rand()
# pt.reshape(50,2)
# print(pt.reshape(50,2))
# plt.scatter(pt[0],pt[2],c=colors, alpha=0.5)
# plt.xlabel('Random number line1')
# plt.ylabel('Random number line2')
# plt.title('first graph')
# plt.show()

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
data.describe()
# print(data.describe())
# pt = np.random.randint(0,75,100)
# # print(pt)
# pt.reshape(50,2)
# # print(pt.reshape(50,2))
# plt.scatter('sepal_length','sepal_width')
# plt.xlabel('Random number line1')
# plt.ylabel('Random number line2')
# plt.title('first graph')
# plt.show()

# plt.scatter(data['sepal_length'],data['sepal_width'])
# plt.xlabel('sepal_length')
# plt.ylabel('sepal_width')
# plt.show()



# plt.hist(data['sepal_length'],data['sepal_width'])
# plt.xlabel('sepal_length')
# plt.ylabel('sepal_width')
# plt.show()

# setosa_data = data[data.species == 'setosa']
# versicolor_data = data[data.species == 'versicolor']
# virginica_data = data[data.species == 'virginica']

# fig, ax=plt.subplots(1,3,figsize=(13, 5))


# ax[0].hist(setosa_data.petal_length, color='g', label = 'setosa')
# ax[1].hist(versicolor_data.petal_length, color='r', label = 'versicolor')
# ax[2].hist(virginica_data.petal_length, color='b', label = 'virginica')

# ax[0].legend()
# ax[1].legend()
# ax[2].legend()
# ax[0].set_ylabel('Frequency')
# ax[1].set_ylabel('Frequency')
# ax[2].set_ylabel('Frequency')
# ax[0].set_xlabel('petal length (cm)')
# ax[1].set_xlabel('petal length (cm)')
# ax[2].set_xlabel('petal length (cm)')

# plt.show()

titanic_df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
titanic_df.head()
# print (titanic_df.head())
# print(titanic_df.info())
# print(titanic_df.describe())
# age = titanic_df[titanic_df.Age<40]
# age2 = titanic_df[titanic_df.Age>40]
# print(age)
# fig,ax = plt.subplots(1,2,figsize=(13, 5))
# ax[0].hist(age.Age , color ='r', label= 'Young people')
# ax[1].hist(age2.Age, color ='g', label = 'Old people')
# ax[0].legend()
# ax[1].legend()
# ax[0].set_xlabel('Age')
# ax[1].set_xlabel('Age')
# ax[0].set_ylabel ('People')
# ax[1].set_ylabel ('People')
# plt.show()\
print(titanic_df.head())
sel = titanic_df[titanic_df.Fare<275]
print(sel)
fig,ax = plt.subplots(1,figsize=(13, 5))
ax.hist(sel.Fare , color='g',label= 'Fare')
ax.legend()
ax.set_xlabel('Fare')
ax.set_ylabel('People')
plt.show()



