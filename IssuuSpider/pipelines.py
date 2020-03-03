# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class IssuuspiderPipeline(object):
    def open_spider(self,spider):
        self.file = open('results.csv','w')
    def close_spider(self,spider):
        self.file.close()
    def process_item(self, item, spider):
        # data = str(item['like'][0])
        # print(data)
        data = str(item['follow']) + ',' + str(item['like']) + ',' + item['detail_url'] + ';\n'
        print('--------------data-------------------')
        print(data)
        print('--------------data-------------------')
        self.file.write(data)
        return data
