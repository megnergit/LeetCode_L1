import pandas as pd


list_ex = [[1,2], [2,3], [3,4], [4,5]]
df_ex = pd.DataFrame(list_ex, columns=['id','value' ])
df_ex
df_ex.loc[:2,:]

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
  return employees.loc[:2,:]

    