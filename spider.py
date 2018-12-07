import requests
import re
import json


class Spider(object):
    # 构造函数
    def __init__(self):
        self.encoding='utf-8'
        
    # 运行 爬去相对应的内容
    def run(self,pageNum  =1,**config):
        num = 1
        listRegex = config['listRegex']
        contentRegex = config['contentRegex']
        contentDict = config['contentDict']
        saveUrlFn = config['saveUrlFn']
        
        for i in range(int(pageNum)):
            self.pageList = []
            listUrl = self.listPage(i+1,listRegex,ListFn=ListFn,urlFn=urlFn)
            for item in listUrl:
                itemDict =  self.contentPage(item['url'],contentRegex,objDict=contentDict)
                self.pageList.append(itemDict)
            
            with open(saveUrlFn(num),'w') as f:
                json.dump(self.pageList,f,ensure_ascii=False)
                num = num + 1
        print('爬取完毕')
        





        # 配置函数，需要产品页的规律和内容页的规律，放置字典
    def config(self,search):
        # 想要搜索的数据内容
        self.search = search
        pass

    

    # 定义列表页的爬取
    #regex = '''<td height="26">.*?<a href="(.*?)"'''
    def listPage(self,pageNum,regex,ListFn= lambda x:x,urlFn=lambda x:x):
        res = requests.get(ListFn(pageNum))
        res.encoding = self.encoding
        result = res.text
        print(regex)
        pattern = re.compile(regex,re.S)
        resultList = re.findall(pattern,result)
        
        endList = []

        for item in resultList:
            endList.append({'url':urlFn(item)})
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

# 定义内容页的爬取
    def contentPage(self,url,regex,objDict):
        res = requests.get(url)
        res.encoding = self.encoding
        content = res.text
        print(content)
        print(regex)
        pattern = re.compile(regex,re.S)
        result = re.search(pattern,content)


        for key,value in objDict.items():
            objDict[key] = result.group(key)
        return objDict




#扩展

def ListFn(pageNum):
    return 'http://www.dytt8.net/html/gndy/oumei/list_7_'+str(pageNum)+'.html'

def urlFn(tempUrl):
    return 'http://www.dytt8.net'+tempUrl


def pageNumFn():
    num = 1
    res = requests.get('http://www.dytt8.net/html/gndy/oumei/list_7_'+str(num)+'.html')
    res.encoding = 'gb2312'
    result = res.text
    # print(result)


    yema = re.compile('''共(\d*?)页''',re.S)
    pageNum = re.search(yema,result)
    pageNum =pageNum.groups()[0]
    return pageNum

objDict = {
            'title':'',
            'time':'',
            'imgUrl':'',
            'download':''
        }


def saveUrlFn(i):
    return './json/%s.json'%i


listRegex = '''<td height="26">.*?<a href="(.*?)"'''

contentRegex =  '<div class="title_all.*?#07519a>(?P<title>.*?)\s*</font>.*?发布时间：\s*(?P<time>.*?)\s*<tr>.*?<img.*?src="(?P<imgUrl>.*?)".*?<td style="WORD-WRAP: break-word".*?href="(?P<download>.*?)"'


if __name__=='__main__':
    app = Spider()
    app.encoding = 'gb2312'
    app.run(pageNum=pageNumFn(),listRegex = listRegex,contentRegex=contentRegex,contentDict=objDict,saveUrlFn=saveUrlFn)
