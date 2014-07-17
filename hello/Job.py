# -*- coding: UTF-8 -*-
__author__ = 'gusw'

import urllib2
import BeautifulSoup

class Job:
    name = '软件测试工程师'
    url = ''
    city = '北京'
    time = ''
    jd = ''
    yaoqiu = ''

class NeteaseJobParser:
    def getJob(self, url):
        job = Job()
        job.url = url
        content = urllib2.urlopen(job.url).read()
        soup = BeautifulSoup.BeautifulSoup(content)
        target = soup.findAll('div', {'class': 'c4 clearfix'})
        job.jd = target
        return job

class TencentJobParser:
    def getJob(self, url):
        job = Job()
        job.url = url
        newurl = job.url.encode("gb2312")
        content = urllib2.urlopen(newurl).read()
        soup = BeautifulSoup.BeautifulSoup(content)
        target = soup.findAll('ul', {'class': 'squareli'})
        job.jd = target[0]
        job.yaoqiu = target[1]
        return job
