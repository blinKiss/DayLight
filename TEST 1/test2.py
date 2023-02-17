word = ['해바라기', '나팔꽃', '장미', '무궁화', '코스모스', '접시꽃', '선인장', '제비꽃', '국화', '에델바이스']
word2 = []
word3 = []
word4 = []
word5 = []
for i in word:
    if(len(i) == 2):
        word2.append(i)
    if(len(i) == 3):
        word3.append(i)
    if(len(i) == 4):
        word4.append(i)
    if(len(i) == 5):
        word5.append(i)
print('이름 길이로 분류한 꽃\n두 글자인 꽃 : {}\n세 글자인 꽃 : {}\n네 글자인 꽃 : {}\n다섯 글자인 꽃 : {}\n'
      .format(word2, word3, word4, word5))
        