import pandas as pd

list_1 = [[1, 'Mason', 8], 
          [2, 'Ava', 6], 
          [3, 'Taylor', 15],
          [4, 'Georgia', 17]]

list_2 = [[5, 'Leo', 7], 
          [6, 'Alex', 7]]

df1 = pd.DataFrame(list_1, columns=['student_id', 'name', 'age'])
df2 = pd.DataFrame(list_2, columns=['student_id', 'name', 'age'])

df1
df2




def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0, ignore_index=True)

    