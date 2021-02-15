# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:29:51 2021

@author: User
"""

import scrapy


class NcaaSpider(scrapy.Spider):
    name = "draft"

    start_urls = ["https://stats.ncaa.org/team/inst_team_list?academic_year=2020&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2019&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2018&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2017&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2016&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2015&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2014&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2013&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2012&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2011&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2010&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2009&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2008&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2007&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2006&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2005&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2004&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2003&conf_id=-1&division=1&sport_code=WVB",
                  # "https://stats.ncaa.org/team/inst_team_list?academic_year=2002&conf_id=-1&division=1&sport_code=WVB"
                  ]

    def parse(self, response):
        team = response.css('tr>td>a::attr(href)').getall()
        new_url = "https://stats.ncaa.org"
        for i in team:
            url = new_url + i
            yield scrapy.Request(url, callback = self.parse_team)

    def parse_team(self, response):
        #figure out how to get all rows in the table
        for schedule in response.css('html>body[id=body]>div[id=contentarea]>table>tr>td>fieldset>table>tbody>tr').getall()#need to iterate by 2
        yield {
         'date', schedule.css('td::text').get(),
         #'opponent', schedule.css()
         }

        #get schedule results
#response.css('html>body[id=body]>div[id=contentarea]>table>tbody>tr>td')

#stack overflow example code
# def parse(self, response):
#         products = response.xpath("//*[contains(@class, 'ph-summary-entry-ctn')]/a/@href").extract()
#         for p in products:
#             url = urljoin(response.url, p)
#             yield scrapy.Request(url, callback=self.parse_product)
# def parse_product(self, response):
#         for info in response.css('div.ph-product-container'):
#             yield {
#                 'product_name': info.css('h2.ph-product-name::text').extract_first(),
#                 'product_image': info.css('div.ph-product-img-ctn a').xpath('@href').extract(),
#                 'sku': info.css('span.ph-pid').xpath('@prod-sku').extract_first(),
#                 'short_description': info.css('div.ph-product-summary::text').extract_first(),
#                 'price': info.css('h2.ph-product-price > span.price::text').extract_first(),
#                 'long_description': info.css('div#product_tab_1').extract_first(),
#                 'specs': info.css('div#product_tab_2').extract_first(),
#             }
# bonus points if you can pull that team statistics table
