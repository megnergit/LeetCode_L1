import pandas as pd

dict_x=dict(name=['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'], 
            species=['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
            age=[98,50,6,45,100,26],
            weight=[464, 41, 328, 463, 50, 349])

animals=pd.DataFrame.from_dict(dict_x)
animals.loc[animals['weight'] > 100, : ].sort_values(by=['weight'], ascending=False, ignore_index=True)['name'].to_frame()




def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.loc[animals['weight'] > 100, : ].sort_values(by=['weight'], ascending=False, ignore_index=True)['name'].to_frame()
