text = "    <title>의류쇼핑몰의 메인에 오신 것을 환영합니다</title>    "
text2 = text.strip()
text3 = text2.replace('title', 'div')
print(text3)
text4 = text3.replace('<div>', '').replace('</div>', '')
print(text4)

# 정규식을 이용한 방법
import re
text5 = "ㅁㅁ<title>의류쇼핑몰의 메인에 오신 것을 환영합니다</title>ㅁㅁ"
modify = re.sub('<.*?>','', text5)

print(modify)

# modify = re.compile('\<.+?\>')

