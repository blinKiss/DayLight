text = "    <title>의류쇼핑몰의 메인에 오신 것을 환영합니다</title>    "
# 4개씩 좌우에 공백이 있음
# strip 좌우 공백제거
print('공백' + text.strip() + '제거')
# 오른쪽 공백만 제거
print('공백 있음' + text.rstrip() + '공백 제거')
# 왼쪽 공백만 제거
print('공백 제거' + text.lstrip() + '공백 있음')