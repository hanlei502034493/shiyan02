# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo

class HahaPipeline(object):
    conn=pymongo.MongoClient('localhost',27017)
    db=conn.hanlei
    table=db.leilei
    def process_item(self, item, spider):
        self.table.insert_one(dict(item))
        return item

class MysqlPipeline(object):
    conn=pymysql.connect(host="localhost",db="goods",charset="utf8",port=3306,user="root",password="")
    cursor=conn.cursor()
    def process_item(self, item, spider):
        data=dict(item)
        try:
            self.cursor.execute('insert into good values("%s","%s","%s","%s")'%(data['name'],data['title'],data['link'],data['riqi']))
            self.conn.commit()
            print("入库成功")
        except Exception as e:
            print("入库失败")
            print(e)
            self.conn.rollback()
        return item