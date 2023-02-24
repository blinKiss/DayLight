import pandas as pd

df = pd.read_excel('./data/codefilex.xlsx')

print('전국 은행 지점 수 :', df.shape[0])
df_slice = df[['은행코드', '점포명', '주소', '전화번호']]
# print(df_slice)
df_woori = df_slice[df_slice['점포명'].str.contains('우리')]
# 총 점포 수
print('우리은행 점포 수 :', df_woori.shape[0])
# 주소를 기준으로 지역별로 갯수 서울 인천 경기 부산 광주				
# df_seoul = df_woori[df_woori['주소'].str.contains('서울')]
# print('우리 은행 서울 지점 수 :', df_seoul.shape[0])
# df_incheon = df_woori[df_woori['주소'].str.contains('인천')]
# print('우리 은행 인천 지점 수 :', df_incheon.shape[0])
region = ['서울', '인천', '경기', '부산', '광주']
for r in region:
    df_region = df_woori[df_woori['주소'].str.contains(r)]
    print('우리 은행 {}지점 수 : {}'.format(r, df_region.shape[0]))

