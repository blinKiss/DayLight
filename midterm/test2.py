# 리스트 자료형
# word = ['해바라기', '나팔꽃', '장미', '무궁화', '코스모스', '접시꽃', '선인장', '제비꽃', '국화', '에델바이스']
# 이중에서 이름의 길이가 짝수인 꽃들만 추출해서 출력하시오

word = ['해바라기', '나팔꽃', '장미', '무궁화', '코스모스', '접시꽃', '선인장', '제비꽃', '국화', '에델바이스']
for i in word:
    if(len(i) % 2 == 0):
        print(i)
