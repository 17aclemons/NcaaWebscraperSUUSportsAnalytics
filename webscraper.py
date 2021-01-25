# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:29:51 2021

@author: User
"""

from bs4 import BeautifulSoup
import requests

url = "https://stats.ncaa.org/team/inst_team_list?academic_year=2020&conf_id=-1&division=1&sport_code=WVB"

temp = requests.get(url)

#do I have permission to scrape this?