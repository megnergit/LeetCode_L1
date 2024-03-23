import pandas as pd

dict_couses = {
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'class': ['math', 'math', 'math', 'math', 'math', 'english', 'english', 'english', 'english'],     
}

courses = pd.DataFrame(dict_couses)
courses

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
#  return (courses.groupby('class').count() >=5).index.to_frame().reset_index(drop=True)['class'].to_frame()
#  return (courses.groupby('class').count() >=5).index.to_frame()['class']
  x = courses.groupby('class').count() >=5
  return x.loc[x['student'] == True].index.to_frame().reset_index(drop=True)['class'].to_frame()



find_classes(courses) 

#     courses['class'].isin
          




    