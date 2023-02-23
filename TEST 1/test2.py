word = ['해바라기', '나팔꽃', '장미', '무궁화', '코스모스', '접시꽃', '선인장', '제비꽃', '국화', '에델바이스']
word_dict = {len(i): [] for i in word}
# print(word_dict)
for j in word:
    word_dict[len(j)].append(j)

print('이름 길이로 분류한 꽃\n두 글자인 꽃 : {}\n세 글자인 꽃 : {}\n네 글자인 꽃 : {}\n다섯 글자인 꽃 : {}\n'
.format(word_dict[2], word_dict[3], word_dict[4], word_dict[5]))