import numpy as np
import pandas as pd

# dict
data = {
    'name' : ['Kim', 'Park', 'Choi', 'Lee'],
    'id' : ['abc', 'asd', 'zxc', 'qwe'],
    'math' : ['A', 'B', 'C', 'D'],
    'm_score' : [100, 88, 73, 65]
}

# dataframe
df = pd.DataFrame(data)
print(df, '\n')
# print(df.melt(id_vars='A', value_vars='B'))
print(df.melt(id_vars='name', value_vars='math', var_name='subject', value_name='grade'))
print(df.melt(id_vars=['name', 'id'], value_vars=['math', 'm_score'], var_name='subject', value_name='grade').sort_values(by='name'))



