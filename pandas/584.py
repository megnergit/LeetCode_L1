import pandas as pd

dict_customer=dict(id=[1,2,3,4,5,6],
                   name=["Will","Jane","Alex","Bill","Zack","Mark"],
                   referee_id=['nan','nan',2,'nan',1,2])

customer = pd.DataFrame.from_dict(dict_customer)
customer

print(dict_customer)

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
  customer['referee_id'] = customer['referee_id'].astype(str)
  return customer.loc[~(customer['referee_id']=='2'), :]['name'].to_frame()

print(find_customer_referee(customer))

    