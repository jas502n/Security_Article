# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SeebugItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 文章标题 Article_Title
    Article_Title = scrapy.Field()

    # 文件链接 Article_Link
    Article_Link = scrapy.Field()

    # 文章时间 Article_Time
    Article_Time = scrapy.Field()

    # 文章标签 Article_Tag
    Article_Tag = scrapy.Field()

    # 文章简介 Article_Introduction
    # Article_Introduction = scrapy.Field()

    # 文章作者
    Article_Author = scrapy.Field()

    # 原文链接 Article_
    Article_Origin_Link = scrapy.Field()

    # Article_Summary
    Article_Summary = scrapy.Field()
    pass
