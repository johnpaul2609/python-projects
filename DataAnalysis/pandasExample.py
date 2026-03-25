import pandas as pd


# st = [[1,'john',99,98,98],[2,'xyz',88,78,59]]
# stdf = pd.DataFrame(st)
# stdf1 = pd.DataFrame(st,columns=['id','name','m1','m2','m3'])
# print(st)
# print(stdf)
# print(stdf1)
# print(stdf1.shape)
# stdf1['total']=stdf1['m1']+stdf1['m2']+stdf1['m3']
# print(stdf1)
# print(stdf1.shape)
# stdf1['average']= stdf1['total']/2
# print(stdf1)
# print(stdf1.shape)

data = {
    "emp_id": [101, 102, 103, 104, 105, 106, 107],
    "name": ["John", "Alice", "Bob", "Diana", "Evan", "Sam", "Riya"],
    "department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance"],
    "salary": [60000, 50000, 70000, 65000, 52000, 72000, 68000],
    "experience": [3, 5, 2, 7, 4, 6, 8],
    "join_date": pd.to_datetime([
        "2020-01-10", "2018-03-15", "2021-07-23",
        "2016-11-01", "2019-05-20", "2017-08-30", "2015-02-14"
    ])
}

df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.head(2))  #default it run 5 datas
print(df.tail(2))
df['salaryrank']=df['salary'].rank(ascending=False)  #rank it skip the number when it repeat
print(df)
df['salarydenserank']=df['salary'].rank(ascending=False, method='dense') # it doesnot skip the number
print(df.to_string())
print(df.dtypes)
print(df.columns)
print(df.describe())
df.to_csv('data.csv')

