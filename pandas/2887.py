import pandas as pd


dict_ex = dict(name=["Wristwatch", 'WirelessEarbuds', 'Golfclubs', 'Printer'], 
               quantity=[None, None, 779, 849], 
               price=[135, 821, 9319, 3051])

products=pd.DataFrame.from_dict(dict_ex)
products.info()

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace=True)
    products['quantity'] = products['quantity'].astype(int)
    return products     

    