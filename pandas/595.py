import pandas as pd

dict = {
    'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'],
    'area': [1647500, 128748, 12381741, 1468, 11246700],
    'population': [31056997, 3581655, 32930091, 71201, 12127071],
    'continent': ['Asia', 'Europe', 'Africa', 'Europe', 'Africa'],
    'gdp': [21992800000, 12960000000, 160000000000, 1630000000, 66480000000]
}

world = pd.DataFrame(dict)
world

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.loc[(world['area'] >= 3_000_000) | (world['population'] >= 25_000_000),['name', 'area', 'population']]
                     

big_countries(world)


world.loc[(world['area'] >= 3_000_000) | (world['population'] >= 25_000_000),:]['name']
