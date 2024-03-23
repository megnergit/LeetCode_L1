import pandas as pd

dict_ex=dict(name=['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'], 
             salary=[4548, 28150, 1103, 6593, 74576, 24433]
)

employees = pd.DataFrame.from_dict(dict_ex)
employees

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
  employees['bonus'] = employees['salary'] * 2
  return employees

createBonusColumn(employees)