import pandas as pd

dict = dict(sales_id=[1, 2, 3, 4, 5],
            name=["John", "Alice", "Bob", "Dylan", "Charlie"],
            salary=[100000, 200000, 30000, 400000, 500000],
            comission_rate=[6,5,12,25,10],
            hire_date=["4/1/2006",
                
sales_person = pd.DataFrame(dict)

dict = dict(company_id=[1, 2, 3, 4],
            name=["Google", "Facebook", "Amazon", "Microsoft"],
            city=["Mountain View", "Menlo Park", "Seattle", "Redmond"])

company = pd.DataFrame(dict)

dict = dict(order_id=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            order_date=['1/1/2014', '2/1/2014', '3/1/2014', '4/1/2014', 
                        '5/1/2014', '6/1/2014', '7/1/2014', '8/1/2014', '9/1/2014', '10/1/2014'],
            sales_id=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
                        


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
  
    