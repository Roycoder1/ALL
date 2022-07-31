import numpy as np
import pandas as pd
from requests import delete

def createNumpy ():
    arr= np.arange(6,100,4)
    print(arr)
createNumpy()

a = np.array([1,2,3,np.nan,5,6,7,np.nan])
b=a[~np.isnan(a)]
print(b)
c = np.random.randint(1,100,30).reshape(5,6)
print (c)

series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
print(series)
series1 = pd.Series(['01 Jan 2020', '10-19-2020', '20150303', '2013/04/04', '2012-05-05', '2013-06-06T12:20'])
print(series1)