import pandas as pd

# 2차원 배열로 정의
# prod_id       prod_name       prod_price      sale_price
# com-10000     삼성노트북       ₩1,000,000      추가
# car-10000     엔진오일         ₩50,000         추가   
# com-20000     키보드           ₩100,000        추가
# sport-10000   등산화           ₩80,000         추가

df = pd.DataFrame({
    'prod_id' : ['com-10000', 'car-10000', 'com-20000', 'sport-10000'],
    'prod_name' : ['삼성노트북', '엔진오일', '키보드', '등산화'],
    # 'prod_price' : ['₩1,000,000', '₩50,000', '₩100,000', '₩80,000']
    'prod_price' : [1000000, 50000, 100000, 80000]
})

# df['sale_price'] = ['₩1,100,000', '₩60,000', '₩120,000', '₩90,000']
df['sale_price'] = ['₩' + str(format(round((i*1.2)), ',')) for i in df['prod_price']]
df['prod_price'] = ['₩' + str(format(i, ',')) for i in df['prod_price']]



print(df)