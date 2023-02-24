import pandas as pd

df_bb= pd.read_csv('./data/billboard.csv')

df_bb_long = df_bb.melt(id_vars=['year', 'artist', 'track', 'time', 'date.entered'])
# print(df_bb_long)
# print(df_bb_long.columns)
df_song = df_bb_long[['year', 'artist', 'track', 'time']]
# print(df_song.shape[0])
# df_duplicate = df_bb_long[df_bb_long['track']=='Loser']
# print(df_duplicate.shape[0])

df_song_remove = df_song.drop_duplicates() # .duplicated = T, F를 반환
print(df_song_remove)

