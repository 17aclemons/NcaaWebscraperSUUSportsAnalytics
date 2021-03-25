# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NcaaPipeline:
    def process_item(self, item, spider):
        if(type(item) is dict):
            temp = 'stuff'
            if(temp in item):
                item = item['stuff']

        return item
