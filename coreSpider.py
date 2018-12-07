import requests
import re
import json


class Spider(object):
    def __init__(self):
        self.encoding = 'utf-8'

    def run(self, pageNum=1, **config):
        num = 1
        listRegex = config['listRegex']
        contentRegex = config['contentRegex']
        contentDict = config['contentDict']
        saveUrlFn = config['saveUrlFn']
        ListFn = config['ListFn']
        urlFn = config['urlFn']

        for i in range(int(pageNum)):
            self.pageList = []
            listUrl = self.listPage(i+1, listRegex, ListFn=ListFn, urlFn=urlFn)
            for item in listUrl:
                # item['url']
                if not re.search('toutiao',item['url']):
                    continue
                itemDict = self.contentPage(item['url'], contentRegex, objDict=contentDict)
                self.pageList.append(itemDict)

            with open(saveUrlFn(num), 'w') as f:
                json.dump(self.pageList, f, ensure_ascii=False)
                num = num + 1
        print('爬取完毕')

    def config(self, search):
        self.search = search
        pass

    #regex = '''<td height="26">.*?<a href="(.*?)"'''
    def listPage(self, pageNum, regex, ListFn=lambda x: x, urlFn=lambda x: x):
        res = requests.get(ListFn(pageNum,self))
        res.encoding = self.encoding
        result = res.text
        # print(regex)
        pattern = re.compile(regex, re.S)
        resultList = re.findall(pattern, result)

        endList = []

        for item in resultList:
            endList.append({'url': urlFn(item)})
        # yield {'url':''}
        return endList

    # #objDict = {
    #         'title':a[0],
    #         'time':a[1],
    #         'imgUrl':a[2],
    #         'download':a[3]
    #     }

    #encoding = 'gb2312'
    #regex = '<div class="title_all.*?#07519a>(.*?)\s*</font>.*?发布时间：\s*(.*?)\s*<tr>.*?<img.*?src="(.*?)".*?<td style="WORD-WRAP: break-word".*?href="(.*?)"'

    def contentPage(self, url, regex, objDict):
        #设置一下请求的标识
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
        }
        res = requests.get(url,headers=headers)
        res.encoding = self.encoding
        content = res.text
        # print(content)
        # print(regex)
        pattern = re.compile(regex, re.S)
        result = re.search(pattern, content)
        print(res.url)
        for key, value in objDict.items():
            objDict[key] = result.group(key)
        
        # print(objDict)
        return objDict
