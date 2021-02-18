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
            yield scrapy.Request(url, callback=self.parse_schedule)

    def parse_schedule(self, response):
        teamName = response.css(
            'html>body[id=body]>div[id=contentarea]>fieldset>legend>a::text').get()

        schedule = response.css(
            'html>body[id=body]>div[id=contentarea]>table>tr>td>fieldset>table>tbody>tr')
        results = {
            'date': [],
            'opponent': [],
            'result': [],
            'attendance': [],
        }

        for s in range(0, len(schedule), 2):
            results['date'].append(schedule[s].xpath('td//text()').get())
            results['opponent'].append(schedule[s].xpath('td/a//text()').get())

        results['result'].append(schedule.css(
            'td>a[class=skipMask]::text')).getall()
        results['attendance'].append(
            schedule.css('td[align=right]::text').getall())

        return results

# bonus points if you can pull that team statistics table
