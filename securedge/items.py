# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SecuredgeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     # The source URL
    url_from = scrapy.Field()
    # The destination URL
    url_to = scrapy.Field()
    # nofollow = scrapy.Field()
    pass
