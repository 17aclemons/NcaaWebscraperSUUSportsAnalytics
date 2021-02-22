# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:29:51 2021

@author: User
"""

import scrapy


class NcaaSpider(scrapy.Spider):
    name = "ncaa"

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
            yield scrapy.Request(url, callback=self.parse_scheduleAndStats)

    def parse_scheduleAndStats(self, response):
        teamName = response.css(
            'html>body[id=body]>div[id=contentarea]>fieldset>legend>a::text').get()
        season = response.css(
            'html>body[id=body]>div[id=contentarea]>fieldset>div>form[id=change_sport_form]>select[id=year_list]>option[selected=selected]::text').get()
        sport = response.css(
            'html>body[id=body]>div[id=contentarea]>fieldset>div>form[id=change_sport_form]>select[id=sport_list]>option[selected=selected]::text').get()
        schedule = response.css(
            'html>body[id=body]>div[id=contentarea]>table>tr>td>fieldset>table>tbody>tr')
        # coach =
        for s in range(0, len(schedule), 2):
            yield {
                'teamName': teamName,
                'season': season,
                'sport': sport,
                'headCoach': coach,
                'date': schedule[s].xpath('td//text()').get(),
                'opponent': schedule[s].xpath('td/a//text()').get(),
                'result': schedule[s].css('td>a[class=skipMask]::text').get(),
                'attendance': schedule[s].css('td[align=right]::text').get()
            }

        teamStats = response.xpath(
            '//html/body/div[2]/table/tr/td[2]/table[1]/tr')

        for row in teamStats:
            yield {
                'stat': row.xpath('td[1]/a/text()').get(),
                'rank': row.xpath('td[2]/text()').get(),
                'value': row.xpath('td[3]/text()').get()
            }
        # I think this is where I need to jump to get the team stats link and pull those stats
        # Separate Player and Team Stats
        # Bonus points
            # pull the coaches name
# bonus points if you can pull that team statistics table
