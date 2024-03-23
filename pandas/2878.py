from typing import List
import pandas as pd

list_example = [[1,2],[2,3],[3,4]]
df_example = pd.DataFrame(list_example, columns=['id', 'value'])
df_example
dir(df_example)
df_example.shape

def getDataframeSize(players: pd.DataFrame) -> List[int]:
  return list(players.shape)


    
    