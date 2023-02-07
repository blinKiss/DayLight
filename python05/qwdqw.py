import re
import urllib
import urllib.request
ya = 'https://kbs/신상출시/asd/편스토랑.rgw'
yali = list(ya)
yastr = ''
hangul = re.findall('[가-힣]', ya)

for i in range(0, len(yali)):
    for j in range(0, len(hangul)): 
        if(yali[i] == hangul[j]):
            yali[i] = urllib.parse.quote(yali[i])
    yastr += yali[i]
print(yastr)