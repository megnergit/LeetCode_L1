import pandas as pd

dict_sales_person = {"id": [1, 2, 3, 4, 5], 
                         "name": ["John", "Alice", "Bob", "Dylan", "Charlie"], 
                         "salary": [100000, 200000, 30000, 400000, 500000],
                         "comission_rate": [6,5,12,25,10],
                         "hire_date": ["4/1/2006", "3/1/2008", "1/1/2010", "12/1/2000", "2/1/2013"]}

person= pd.DataFrame.from_dict(dict_sales_person)
person

dict_company = dict(com_id=[1, 2, 3, 4],
                    name=["RED", "BLUE", "GREEN", "YELLOW"],
                    city=["Mountain View", "Menlo Park", "Seattle", "Redmond"])
company = pd.DataFrame(dict_company)
company

dict_orders = dict(order_id=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   order_date=["1/1/2014",
                                "2/1/2014",
                                "3/1/2014",
                                "4/1/2014",
                                "5/1/2014",
                                "6/1/2014",
                                "7/1/2014",
                                "8/1/2014",
                                "9/1/2014",
                                "10/1/2014"],
                    sales_id=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],  
                    com_id=[1, 3, 1, 1, 3, 1, 1, 4, 1, 2],
                    amount=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

orders = pd.DataFrame(dict_orders)
orders

def sales_person(person: pd.DataFrame, 
                 company: pd.DataFrame, 
                 orders: pd.DataFrame) -> pd.DataFrame:

  if 'RED' not in company['name'].values :
    return person['name'].drop_duplicates().to_frame()

  target_com=company['com_id'].loc[company['name']=="RED"].values[0]
  x=orders.loc[orders['com_id'] ==target_com, 'sales_id'].unique()
  return person.loc[~person['sales_id'].isin(x), 'name'].to_frame()


print(sales_person(person, company, orders))

if 

target_com = company['com_id'].loc[company['name']=="RED", 'com_id']



  




company['name'].values