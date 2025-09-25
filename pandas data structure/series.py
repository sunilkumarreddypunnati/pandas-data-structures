import pandas as pd
print("Series data structure:")
a=(1,2,3,4,5)
b=pd.Series(a)
print(b,'\n')
print("series data structure with customised index:")
c=pd.Series(a,index=['a','b','c','d','e'])
print(c)