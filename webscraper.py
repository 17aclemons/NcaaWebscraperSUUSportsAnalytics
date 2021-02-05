# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:29:51 2021

@author: User
"""

import scrapy

class PostSpider(scrapy.Spider):
    name = "test"
    urls = ["https://stats.ncaa.org/team/inst_team_list?academic_year=2020&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2019&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2018&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2017&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2016&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2015&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2014&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2013&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2012&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2011&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2010&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2009&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2008&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2007&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2006&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2005&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2004&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2003&conf_id=-1&division=1&sport_code=WVB",
          "https://stats.ncaa.org/team/inst_team_list?academic_year=2002&conf_id=-1&division=1&sport_code=WVB"]
        
        
    start_url = urls[0]
    
    

#gets the team number stuff from response       
#response.css('a[href*=//team]::attr(href)').getall()    
        
        
        
#team tags are in a table body, td tag and a tag
#pull tags to get url for each team that is d1 for that year
#pull schedule results for that team
#get player statistics

#bonus points if you can pull that team statistics table
