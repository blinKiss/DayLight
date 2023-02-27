# 반복문으로 읽고 데이터프레임 합치기
# import pandas as pd
# import glob as glob

# files = glob.glob('./data/con*.csv')
# df_tot = pd.DataFrame()

# for file in files:
#     df_temp = pd.read_csv(file)
#     df_tot = pd.concat([df_tot, df_temp], ignore_index=True)
    
# print(df_tot)

# csv같은 파일이 웹상에 올라간 경우
# 로컬로 다운로드 받기
# urllib모듈에 
# urlretrieve(소스경로, 파일경로) 파일 다운로드함
# src http:// .csv
# 데이터를 읽어서 출력
import urllib.request
import pandas as pd
import numpy as np
csv_url = 'https://raw.githubusercontent.com/developer-sdk/kaggle-python-beginner/master/datas/kaggle-titanic/train.csv'
csv_save = './data/download/train.csv'
urllib.request.urlretrieve(csv_url, csv_save)

df = pd.read_csv('./data/download/train.csv')
print(df.info())

df['Sex'] = df['Sex'].astype('category')
print(df.info())