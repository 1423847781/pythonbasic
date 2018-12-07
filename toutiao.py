#扩展
import requests
import re
import json
from coreSpider import Spider



#列表地址

def ListFn(pageNum,sys):
    #https://www.toutiao.com/search_content/?offset=20&format=json&keyword=搜索关键词&count=20&cur_tab=3&from=gallery
    urlStr = 'https://www.toutiao.com/search_content/?offset={}&format=json&keyword={}&count=20&cur_tab=3&from=gallery'
    return urlStr.format((pageNum-1)*10,sys.search)


def urlFn(tempUrl):
    return tempUrl


def pageNumFn():
    return 10


objDict = {
    'title': '',
    'imgList':''
}


def saveUrlFn(i):
    return './toutiao/%s.json' % i


listRegex = '''"article_url": "(.*?)"'''

contentRegex = '''<title>(?P<title>.*?)</title>.*?gallery: JSON.parse\("(?P<imgList>.*?)"\),'''

contentRegex2 = '''<title>(?P<title>.*?)</title>.*?"sub_images.*?\[(?P<imgList>.*)\],.*?"max_img_width'''


if __name__ == '__main__':
    app = Spider()
    # app.encoding = 'gb2312'
    # app.run(pageNum=pageNumFn(), listRegex=listRegex,
    #         contentRegex=contentRegex, contentDict=objDict, saveUrlFn=saveUrlFn)

    
    
    
    app.search = '美女'
    #列表页测试
    # result = app.listPage(1,listRegex,ListFn=ListFn,urlFn=urlFn)
    # print(result)
    #内容页测试
    # result = app.contentPage('http://toutiao.com/group/6602836640354271747/',contentRegex2,objDict)
    # print(result)
    
    app.run(pageNum=pageNumFn(), listRegex=listRegex,
                     contentRegex=contentRegex2, contentDict=objDict, saveUrlFn=saveUrlFn,ListFn=ListFn,urlFn=urlFn)
    
    
    
    
    
    
    # print(resStr)
    # print(isinstance(result['imgList'],str))
    # a = re.sub('\\', '', result['imgList'])
    # print(a)
    # a = json.loads(result['imgList'])
    # print(a)

