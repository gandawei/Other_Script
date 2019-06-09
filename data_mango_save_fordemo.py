from pymongo import MongoClient
import datetime


class mango_save:

    def __init__(self):
        self.client = MongoClient()
        self.database = self.client.sino_web_demo
        self.collection = self.database.url_record01

    def insert_data(self,name,tag,url,page,code):
        self.name = str(name)
        self.tag=tag
        self.url=str(url)
        self.page=page
        self.code=code
        self.time=datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        result=self.collection.find_one({'url':self.url,'name':self.name})
        if result is None:
            data={'name':self.name,'tag':self.tag,'url':self.url,'page':self.page,'code':self.code,'time':self.time}
            self.collection.insert(data)
            print(data)
            print('Mango database Insert success')
        else:
            print("Data is repeat,so failed")


    def find_url(self,condition,result):
        list=self.collection.find(condition,result)
        print('数据库url查询更新完毕')
        return list
    def update_data(self,condition,set):
        self.collection.update_one(condition,set)
        print('数据库code更新完毕')


