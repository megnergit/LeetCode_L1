import pandas as pd

dict_ex = dict(student_id=[32,217,779,849], 
               name=['Piper', None, 'Gerogia', 'Willow'],
               age=[5, 19, 20, 14]
)

students=pd.DataFrame.from_dict(dict_ex)




def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'], axis=0)