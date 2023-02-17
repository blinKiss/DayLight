import pandas as pd

Aclass = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
st_score = pd.Series(Aclass)
print('총 학생 수 : {}\n합계 : {}\n평균 : {}'.format(st_score.size, st_score.sum(),st_score.mean()))