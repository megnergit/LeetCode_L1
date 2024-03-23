import pandas as pd

list_ex = [['jack', 19666], ['Piper', 74754], ['Mia', 62509], ['Ulysees', 54866]]
employees = pd.DataFrame(list_ex, columns=['name', 'salary'])


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] =  employees['salary'] * 2
    return employees


modifySalaryColumn(employees)