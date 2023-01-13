import time_to_sort as T
import print_time as P
import pandas as pd

tab = T.time_to_sort ()
print(tab)
P.print_time(tab)

col1 = "X"
data = pd.DataFrame({col1:tab})
data.to_excel('sample_data.xlsx', sheet_name='sheet1', index=False)
