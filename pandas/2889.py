import pandas as pd

list_1 = [['Jacksonville', 'January', 13], 
          ['Jacksonville', 'Feburary', 23],
          ['Jacksonville', 'March', 38],
          ['Jacksonville', 'April', 5],
          ['Jacksonville', 'May', 34],

          ['Elpaso', 'January', 20],
          ['Elpaso', 'Feburary', 6],
          ['Elpaso', 'March', 26],
          ['Elpaso', 'April', 2],
          ['Elpaso', 'May', 43]]

weather=pd.DataFrame(list_1, columns=['city', 'month', 'temperature'])
weather.pivot(index='month', columns='city', values='temperature')

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')

