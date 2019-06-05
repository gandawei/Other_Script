import requests
import lxml
import sys,io
from lxml import etree
import random
import time
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #linux上运行时需要取消

class return_selector():
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'ASP.NET_SessionId=ze5hsc55j4wgfhf4wt4qsm55; ASP.NET_SessionId_NS_Sig=oenCV6md02sl4FC_',
            'Host': 'www.bajuintl.com',
            'Referer': 'https://www.baidu.com/link?url=V-pJBevCDwa13Dp8e0ieubsh_EiK1-7ODRb5wSMLSlVyQGbt16n7VHTCrCL2jVWc&wd=&eqid=e85d8dfb00098feb000000065cee541d',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5944.400 LBBROWSER/10.1.3378.400',
        }
    def selector(self,url):
        html = requests.get(url, headers=self.headers).content.decode('utf-8')
        selector = etree.HTML(html)
        return selector


if __name__ == '__main__':
    start_time = time.time()
    name="XXX" #作者人名
    times= random.randint(650,750) #总点击次数
    title_name=''
    clicks=0
    url = 'http://www.bajuintl.com/'
    html = return_selector()
    selector=html.selector(url)
    list=selector.xpath("//a[@target='_blank']/@href")
    url_second=[]
    for i in list[9:20]:
        url_1=url+str(i)
        url_second.append(url_1)
    for i in url_second:
        selector=html.selector(i)
        author = selector.xpath("//span[@id='lb_author']/text()")[0]
        click_times= selector.xpath("//span[@id='lb_count']/text()")[0]
        if author == name:
            if int(click_times)<times:
                for j in range(random.randint(25,35)): #该括号参数为每次运行的次数区间
                    s=html.selector(i)
                    c = s.xpath("//span[@id='lb_count']/text()")[0]
                    #time.sleep(2)
                s = html.selector(i)
                clicks = s.xpath("//span[@id='lb_count']/text()")[0]
                title_name = s.xpath("//span[@id='lb_title']/text()")[0]
                print('作者：{0}；文章名：{1}；点击次数：{2}'.format(author, title_name, clicks))
            else:
                title_name = selector.xpath("//span[@id='lb_title']/text()")[0]
                print('{},该文章次数已达到{},已无需再加速。'.format(title_name,click_times))
    i=datetime.datetime.now()
    print('记录时间为：%s月%s日%s时%s分' % (i.month, i.day, i.hour, i.minute))

    end_time = time.time()
    print('所花费时间为{}秒'.format(end_time-start_time))