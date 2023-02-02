import re

text = ('111<head>안녕하세요</head>22')
body = re.search('<.*>', text)

body = body.group()
print(body)

