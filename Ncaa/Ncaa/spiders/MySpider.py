# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:29:51 2021

@author: User
"""

import scrapy
import json


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

    """ def start_requests(self):
        # WBB - Women's Basketball
        # WSB - Women's Softball
        # WSO - Women's Soccer
        # WTE - Women's Tennis
        # WLA - Women's Lacrosse
        # WIH - Women's Ice Hockey
        # WWP - Women's Water Polo
        # WSV - Women's Beach Volleyball
        # WVB - Women's Volleyball

        # only change these two variables if needed
        year = ["2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012",
                "2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003", "2002"]
        # add or remove sports codes as needed
        sportCode = ["WBB", "WSB", "WSO", "WTE",
                    "WLA", "WIH", "WWP", "WSV", "WVB"]
        urls = []

        for sport in sportCode:
            for y in year:
                temp = "https://stats.ncaa.org/team/inst_team_list?academic_year=" + y
                temp = temp + "&conf_id=-1&division=1&sport_code=" + sport
                urls.append(temp)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) """

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
        coach = response.xpath(
            '/html/body/div[2]/fieldset[1]/div[2]/div[2]/fieldset/a/text()').get()
        coach = response.xpath(
            '/html/body/div[2]/fieldset[1]/div[2]/div[2]/fieldset/a/text()').get()
        for s in range(0, len(schedule), 2):
            yield {
                'teamName': teamName,
                'season': season,
                'sport': sport,
                'headCoach': coach,
                'date': schedule[s].xpath('td//text()').get(),
                'opponent': schedule[s].xpath('td/a//text()').get(),
                'result': schedule[s].css('td>a[class=skipMask]::text').get(),
                'attendance': schedule[s].css('td[align=right]::text').get().strip("\n").strip()
            }

        teamStats = response.xpath(
            '//html/body/div[2]/table/tr/td[2]/table[1]/tr')

        for row in teamStats:
            try:
                yield{
                    'stat': row.xpath('td[1]/a/text()').get(),
                    'rank': row.xpath('td[2]/text()').get(),
                    'value': row.xpath('td[3]/text()').get().strip("\n").strip()
                }
            except AttributeError:
                yield{

                }

        # get the URL for the Team Stats
        stats = response.xpath('/html/body/div[2]/a[2]/@href').get()

        # make a new url for Scrapy
        url = "https://stats.ncaa.org" + stats

        yield scrapy.Request(url, callback=self.parseStats)

    # https://stats.ncaa.org/team/817/stats/14942 Team stats link

    def parseStats(self, response):
        data = {}
        # get the year
        data['year'] = response.css(
            'html>body[id=body]>div[id=contentarea]>fieldset>div>form>select[id=year_list]>option[selected=selected]::text').get()
        # get the team
        data['team'] = response.xpath(
            '/html/body/div[2]/fieldset[1]/legend/a[1]//text()').get()
        # coach
        data['coach'] = response.xpath(
            '/html/body/div[2]/fieldset[1]/div[2]/div[2]/fieldset/a//text()').get()

        # table
        table = response.xpath('//*[@id="stat_grid"]')
        # get column names
        th = table.xpath('thead/tr/th/text()').getall()
        #tr = table.xpath('tbody/tr//td//text()')
        #tf = table.xpath('tfoot/tr//td//text()')

        #for tr in table.xpath('tbody/tr'):
        