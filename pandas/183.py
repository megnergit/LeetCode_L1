import pandas as pd

dict_customers=dict(id=[1,2,3,4], name=["Joe","Henry","Sam","Max"] )
dict_orders=dict(id=[1,2], customerId=[3,1])

df_customers=pd.DataFrame.from_dict(dict_customers)
df_orders=pd.DataFrame.from_dict(dict_orders)


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
  x = df_customers.loc[~df_customers["id"].isin(df_orders["customerId"])]["name"].reset_index(drop=True)
  return(x)

print(find_customers(df_customers, df_orders))


