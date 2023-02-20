import pandas as pd

df = pd.read_excel('./data/stock price.xlsx')
# 판다스 엑셀 읽는 엔진 변경 pip install openpyxl

print(df)