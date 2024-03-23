import pandas as pd

list_ex = [[101, 'Ulysses', 13],
        [53, 'William', 10],
        [128, 'Henry', 6],
        [3, 'Henry', 11]]

students=pd.DataFrame(list_ex, columns=['student_id', 'name', 'age'])
students
students.loc[students['student_id']==101, :]

def selectData(students: pd.DataFrame) -> pd.DataFrame:
  return students.loc[students['student_id']==101, :]

    