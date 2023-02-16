# movie.csv파일을 읽어온다
'''
Film,Genre,RottenTomatoesRatings,AudienceRatings,Budget(million),Yearofrelease
(500) Days of Summer,Comedy,87,81,8,2009
'''
import pandas as pd

df = pd.read_csv('./data/movie-ratings.csv')
# 100번째 모든 컬럼값 출력
print('100번째 모든 컬럼 값 :','\n', df.loc[100], '\n')
# 200번째 장르만 출력
print('200번째 장르만 출력 :', df.loc[100, 'Genre'], '\n')
# 맨 마지막에 행 데이터 추가
df.loc[len(df)] = ['Back to the Future', 'Action', '80', '70', '40', 2000]
print('가장 마지막 행 데이터 추가 :', df.loc[len(df)-1], '\n')
# 300번째 영화제목 출력 후 행 삭제
print('300번째 영화제목 출력 :', df.loc[300, 'Film'], '\n')
df.drop(index = [300], axis = 0, inplace=True)
# 400번째 rating값에 -5하여 수정
print('400번째 행 :', df.loc[400], '\n')
# df.loc[400, ('RottenTomatoesRatings', 'AudienceRatings')] = 61, 73
upd_rott = df.loc[400, 'RottenTomatoesRatings'] - 5
upd_audi = df.loc[400, 'AudienceRatings'] - 5
df.loc[400, ('RottenTomatoesRatings', 'AudienceRatings')] = upd_rott, upd_audi
print('400번째 행 레이팅 값 수정', df.loc[400])


# print(df)


# print(df.loc[0:1])
# print(df.loc[:3, 'LAST_NAME']) # 행과 열이름 동시에 만족하는 값
