import pandas as pd
import glob as glob

sample_data = {
    'id' : [1000,1001,1002,1003],
    'job' : ['manager', 'developer', 'manager', 'designer'],
    'salary' : [5000, 3000, 6000, 10000],
    'phn1_phn2' : ['11113333-22225555', '33336666-44449999', '43211234-12344321', '12124562-21212353']
}

df = pd.DataFrame(sample_data)
# print(df)
# print(df['job'].str.capitalize())

# print(df['job'].str.replace('manager', 'marketer'))
# 내 답
# psplit = df['phn1_phn2'].str.split('-')
# df['phone1'] = psplit.str.get(0)
# df['phone2'] = psplit.str.get(1)
df['phone1'], df['phone2'] = df['phn1_phn2'].str.split('-').str

for i in range(len(df['phone1'])):
    # df['phone1'][i] = df['phone1'][i][:4] + '-' + df['phone1'][i][4:]
    # df['phone2'][i] = df['phone2'][i][:4] + '-' + df['phone2'][i][4:]
    df.loc[i, 'phone1'] = df.loc[i, 'phone1'][:4] + '-' + df.loc[i, 'phone1'][4:]
    df.loc[i, 'phone2'] = df.loc[i, 'phone2'][:4] + '-' + df.loc[i, 'phone2'][4:]

df = df.drop('phn1_phn2', axis=1)
print(df)  

# 선생님 답
# df2 = df['phn1_phn2'].str.split('-', expand=True)
# print(pd.concat([df,df2[0]], axis=1))
# split_1 = df['phn1_phn2'].str.split('-').str.get(0)
# df['phn1'] = split_1
# print(df)