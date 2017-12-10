# sec_news_scrapy

# 简介
本程序基于Scrapy实现爬虫，可以自动爬取“[E安全](https://www.easyaq.com/)”网站上的安全资讯页面内容，然后基于[jieba](https://github.com/fxsjy/jieba)做中文分词，并提取关键字。将结果信息保存到MySQL数据库中，最后通过eChart根据文章中关键词出现的频率用词云[echarts-wordcloud](https://github.com/ecomfe/echarts-wordcloud)展示出来。
详细介绍请阅读这篇文章：[《Scrapy+eChart自动爬取生成网络安全词云》](http://dearcharles.cn/2017/12/10/Scrapy-eChart%E8%87%AA%E5%8A%A8%E7%88%AC%E5%8F%96%E7%94%9F%E6%88%90%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E8%AF%8D%E4%BA%91/)

# 过程
1. 用Scrapy先去安全咨询网站上爬取文章的标题和内容
2. 对文章的内容进行切词
3. 使用TF-IDF算法提取关键词
4. 将关键词保存到数据库
5. 最后可以用可视化将近期出现的比较频繁的关键词做个展示

# 如何执行
## 安装Scrapy
安装过程这里不详述
## 准备数据库
先准备好一个MySQL数据库，然后将数据库信息写入pipelines.py。在数据库中建表，脚本在工程目录下secnewsdb.sql文件中，一共两个表，分别保存文章和关键词。

## 运行爬虫
打开cmd，进入工程根目录，执行
```
scrapy crawl security
```
结果会保存到数据库中
## 分析结果生成eChart数据对象
执行工程目录下的gen_wordcloud.py，会自动查询MySQL中的数据并将结果写入文件
## 词云可视化展示
词云文件在工程目录下的echart目录中，最简单的展示方式是用python自带的web容器。
打开cmd，进入echart目录，执行
```
python -m http.server 8000
```
然后打开浏览器访问http://localhost:8000/optionKeywords.html
![词云可视化效果](http://upload-images.jianshu.io/upload_images/8818451-23844b9653c4ef3b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)