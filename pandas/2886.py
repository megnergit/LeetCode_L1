import pandas as pd

list_ex=[
    [1, 'Ava', 6, 73.0],
    [2, 'Kate', 15, 87.0],
]

students=pd.DataFrame(list_ex, columns=['student_id', 'name', 'age', 'grade'])
students.info()
students['grade']=students['grade'].astype(int)
students.info()

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade']=students['grade'].astype(int)
    return students
    