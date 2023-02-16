import pandas as pd

s = pd.Series(
    {'A' : 1,
     'B' : (1,2,3,4,5),
     'C' : [6,7,8,9,10]
    }
)
print(s)
df = pd.DataFrame(
    {'Column A' : 1.0,
     'Column B' : (1,2,3,4,5),
     'Column C' : [6,7,8,9,10]
    }
)
print(df)