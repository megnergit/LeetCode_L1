import pandas as pd

dict_ex = dict(id=[1,2,3,4,5], 
               first=['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'], 
               last=['King', 'Wright', 'Hall', 'Thompson', 'Moore'], 
               age=[6, 7, 16, 18, 19])

students=pd.DataFrame.from_dict(dict_ex)


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={"id":'student_id', 
                            'first':'first_name', 
                            'last':'last_name', 
                            'age':'age_in_years'})


    