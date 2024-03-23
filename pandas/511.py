import pandas as pd

dict_game = dict(player_id=[1,1,2,3,3], device_id=[2,2,3,1,4], 
                 event_date=["2016-03-01", "2016-05-02", "2016-06-25", "2016-03-02", "2016-07-03"],
                 game_played=[5,6,1,0,5])

activity=pd.DataFrame.from_dict(dict_game)

activity.info()

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
  activity['event_date']=pd.to_datetime(activity['event_date'])
  activity.sort_values('event_date', inplace=True)
  activity.drop_duplicates(subset=['player_id'], keep='first', inplace=True)
  activity.sort_values('player_id', inplace=True)
  activity.rename(columns={"event_date": "first_login"}, inplace=True)
#  print(activity)
  return activity.loc[:,["player_id", 'first_login']]

game_analysis(activity)
    