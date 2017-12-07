# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import jieba
import jieba.analyse
import pymysql


def dbHandle():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="1234",
        charset="utf8",
        db='secnews',
        port=3306)
    return conn


class TutorialPipeline(object):
    def process_item(self, item, spider):

        words = jieba.analyse.extract_tags(item['content'], topK=50, withWeight=True)
        # words = Counter(jieba.cut(item['title'][0], cut_all=False))

        conn = dbHandle()
        cursor = conn.cursor()
        sql = "insert into t_security_news_words(title, `key`, val) values (%s,%s,%s)"
        try:
            for word in words:
                cursor.execute(sql, (item['title'][0], word[0], int(word[1]*1000)))
            cursor.connection.commit()
        except BaseException as e:
            print("存储错误", e, "<<<<<<原因在这里")
            conn.rollback()
        return item
