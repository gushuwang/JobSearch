# -*- coding: UTF-8 -*-

from Job import *
from JobSearch import *

#neteaseJobParser = NeteaseJobParser()
#job2 = neteaseJobParser.getJob('http://hr.163.com/getPositionById.do?id=2208')

tencentJobSearch = TencentJobSearch()
tencentJobList = tencentJobSearch.search('http://hr.tencent.com/position.php?keywords=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&lid=2156&tid=87')

jobs = [];
tencentJobParser = TencentJobParser()
for jobUrl in tencentJobList:
    job = tencentJobParser.getJob(jobUrl)
    jobs.append(job)
#job3 = tencentJobParser.getJob('http://hr.tencent.com/position_detail.php?id=15150&keywords=%E6%B5%8B%E8%AF%95&tid=0&lid=2156')
print jobs