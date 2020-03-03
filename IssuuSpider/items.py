# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IssuuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    follow = scrapy.Field()
    like = scrapy.Field()
    detail_url = scrapy.Field()