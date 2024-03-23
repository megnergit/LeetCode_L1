import pandas as pd


dict_orders=dict(order_number=[1,2,3,4], 
                 customer_number=[1,2,3,3])

orders=pd.DataFrame.from_dict(dict_orders)

dict_null=
df_null=
df_null



def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
  if len(orders)==0: 
    return pd.DataFrame.from_dict(dict(customer_number=[])) 
  return orders.groupby("customer_number").sum().sort_values('order_number', ascending=False).reset_index().loc[[0],'customer_number'].to_frame()


print(largest_orders(orders))




