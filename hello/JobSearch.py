# -*- coding: UTF-8 -*-
import re

__author__ = 'gusw'

import urllib2
import BeautifulSoup

class TencentJobSearch:
    def search(self, url):
        content = urllib2.urlopen(url).read()
        soup = BeautifulSoup.BeautifulSoup(content)
        jobList = soup.findAll(href=re.compile("position_detail*"))
        jobUrls = []
        for href in jobList:
            jobUrls.append('http://hr.tencent.com/' + href['href'])
        return jobUrls
