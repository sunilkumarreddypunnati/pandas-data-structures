import pandas as pd
print("dataframe data structure:")
a={"Name":["sunil","kumar","reddy"],
   "Age":[23,25,22],
   "City":["Hyderabad","Chennai","Bengaluru"]
   }
data_1=pd.DataFrame(a)
print(data_1,'\n')
print("data frame with customised index:")
data_2=pd.DataFrame(a,index=['a','b','c'])
print(data_2)