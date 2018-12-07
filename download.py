import re
import requests
import json


with open('./toutiao/2.json','r') as f:
    text = f.read()
    # print(text)
    txt = text.replace('\\',"")
    # print(json.loads(txt))


# print(txt)

#http://p3.pstatp.com/origin/pgc-image/1534120014452f64478eb10
result = re.search('"imgList": "(.*?)\}\]$', txt, re.S)

abc = result.groups()[0]

retext = re.findall('"url":"(.*?)","width"',abc,re.S)

resList = []
for item in retext:
    temp = re.search('"height".*?"url":"(.*)', item)
    if temp:
        resList.append(temp.groups()[0])
    else:
        resList.append(item)




resList = set(resList)
print(resList)




num = 1
for item in resList:
    res = requests.get(item)
    content = res.content
    with open('./images/{}.jpg'.format(num),'wb') as f:
        f.write(content)
        num = num + 1
