# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import jieba
import jieba.analyse
import pymysql
import re


def dbHandle():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="1234",
        charset="utf8",
        db='secnews',
        port=3306)
    return conn


def is_figure(str):
    value = re.compile(r'^\d+$')
    if value.match(str):
        return True
    else:
        return False


def save_key_word(item):
    words = jieba.analyse.extract_tags(item['content'], topK=50, withWeight=True)

    conn = dbHandle()
    cursor = conn.cursor()
    sql = "insert ignore into t_security_news_words(title, `key`, val) values (%s,%s,%s)"
    try:
        for word in words:
            if is_figure(word[0]):
                continue
            cursor.execute(sql, (item['title'][0], word[0], int(word[1] * 1000)))
        cursor.connection.commit()
    except BaseException as e:
        print("存储错误", e, "<<<<<<原因在这里")
        conn.rollback()


def save_article(item):
    conn = dbHandle()
    cursor = conn.cursor()
    sql = "insert ignore into t_security_news_article(title, content, uri) values (%s,%s,%s)"
    try:
        cursor.execute(sql, (item['title'][0], item['content'], item['uri']))
        cursor.connection.commit()
    except BaseException as e:
        print("存储错误", e, "<<<<<<原因在这里")
        conn.rollback()


class TutorialPipeline(object):
    def process_item(self, item, spider):
        save_key_word(item)
        save_article(item)
        return item
