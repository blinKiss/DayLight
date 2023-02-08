import urllib.request

URL = 'https://www.google.com/search?q='

keyword_list = ['python', 'java', 'bigdata', 'vscode']
# print(len(keyword_list))
newURL = ''
for i in keyword_list:
    newURL = URL + i
    print(newURL)

# res = urllib.request.urlopen(newURL)
req = urllib.request.Request(newURL, headers = {'User-Agent' :'Mozilla/5.0'})
res = urllib.request.urlopen(req)

byte_data = res.read()
text_data = byte_data.decode()
print(text_data)

