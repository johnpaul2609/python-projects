import pandas as pd
pizza_df = pd.read_csv('pizza_sales.csv')
print(pizza_df)
print(pizza_df.shape)
print(pizza_df.head().to_string())
print(pizza_df.columns)
print(pizza_df.dtypes)
o=pizza_df.groupby('pizza_category')['total_price'].sum()#() for grouping [] for inside calculation
print(o)
o=pizza_df.groupby('pizza_category')['total_price'].min()#() for grouping [] for inside calculation
print(o)
o=pizza_df.groupby('pizza_category')['total_price'].max()#() for grouping [] for inside calculation
print(o)
o=pizza_df.groupby('pizza_category')['total_price'].mean()#() for grouping [] for inside calculation
print(o)
o=pizza_df.groupby(['pizza_category','pizza_size'])['total_price'].sum()#() for grouping [] for inside calculation
print(o)
print(pizza_df.dtypes)
pizza_df['order_date']=pd.to_datetime(pizza_df['order_date'],format='%d-%m-%Y')
print(pizza_df)
pizza_df['order_year']=pd.to_datetime(pizza_df['order_date'],format='%d-%m-%Y')
print(pizza_df)
pizza_df['order_month']=pd.to_datetime(pizza_df['order_date'],format='%d-%m-%Y')
print(pizza_df)
pizza_df['order_day']=pd.to_datetime(pizza_df['order_date'],format='%d-%m-%Y')
print(pizza_df)
pizza_df['order_hour']=pd.to_datetime(pizza_df['order_time'],format='%d-%m-%Y')
print(pizza_df.head())
pizza_df['order_year']=pizza_df['order_date'].dt.year

pizza_df['orderdmonth']=pizza_df['order_date'].dt.month
# print(pizza_df)
pizza_df['orderdday']=pizza_df['order_date'].dt.day
# print(pizza_df)
pizza_df['orderdhour']=pizza_df['order_time'].dt.hour
# print(pizza_df)
# print(pizza_df.to_string())

print(pizza_df.columns)
o=pizza_df.groupby(['pizza_category','pizza_size'])['total_price'].sum()
print(o)

o=pizza_df.groupby('orderdhour')['total_price'].sum()
print(o)

pizza_category=pizza_df['']

