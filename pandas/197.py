import pandas as pd

dict_weather=dict(id=[1,2,3,4],
                  recordDate=["2015-01-01","2015-01-05","2015-01-04","2015-01-03"],
                  temperature=[10,-25,20,30])
weather=pd.DataFrame.from_dict(dict_weather)
weather['recordDate']=pd.to_datetime(weather['recordDate'])
weather.info()

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
  if len(weather)==0: 
    return pd.DataFrame.from_dict(dict(id=[], dtype={"id": int}))
#   weather.sort_values(by=["recordDate"], inplace=True)
  weather['recordDate']=pd.to_datetime(weather['recordDate'])
  continuous_dates = pd.date_range(weather['recordDate'].min(),
  weather['recordDate'].max()
  ).to_series().to_frame()

  continuous_dates.rename(columns={0:"dates"}, inplace=True)
  print(continuous_dates)
  print(continuous_dates.info())

  weather = pd.merge(continuous_dates, weather, how="left", left_on="dates", right_on="recordDate")

  w = weather['temperature'].shift(1)
  return weather.loc[(weather['temperature'] - w > 0)]["id"].to_frame()
    
rising_temperature(weather)  
len(weather)
print(weather)