import pandas as pd

list_x = [['Umbrella', 417, 224, 379, 611], 
#          ['SleepingBag', 800, 936, 93, 875]
          ['WirelessEarbubs', 752, 138, 39, 988], 
          ['Skateboard', 647, 996, 697, 746],
          ['Jewelry', 555, 170, 814, 169],
          ['LeatherWallet', 963, 537, 57, 55]
]

report = pd.DataFrame(list_x, columns=['product', 
                                       'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])
report
report.melt(id_vars='product')
            
report.melt(id_vars='product', var_name='quarter', value_name='sales')

def meltTable(report: pd.DataFrame) -> pd.DataFrame:

    return report.melt(id_vars='product', var_name=['quarter', 'sales'])


#     report.set_index('product', inplace=True)
# report = report.stack(level=-1)
# report
# report.reset_index().rename(columns={"level_1":'quarter', 0:'sales' }).sort_values(by=['quarter'], kind='mergesort', ignore_index=True)

