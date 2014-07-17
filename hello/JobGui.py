# -*- coding: UTF-8 -*-
__author__ = 'gusw'

import Tkinter
from Job import *
from JobSearch import *

class App:
    def __init__(self, master):
        frame = Tkinter.Frame(master)
        frame.pack()
        self.label = Tkinter.Label(frame,text=u'腾讯测试工程师招聘信息')
        self.label.pack()

        tencentJobSearch = TencentJobSearch()
        tencentJobList = tencentJobSearch.search('http://hr.tencent.com/position.php?keywords=%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&lid=2156&tid=87')

        jobs = []
        tencentJobParser = TencentJobParser()
        for jobUrl in tencentJobList:
            job = tencentJobParser.getJob(jobUrl)
            jobs.append(job)

        self.infoFrame = Tkinter.Frame(frame)
        for i in range(len(jobs)):
            name = Tkinter.Label(self.infoFrame, text=jobs[i].name)
            name.grid(row=i,column=0)
            jdStr = ''
            yaoqiuStr = ''
            for j in range(len(jobs[i].jd.contents)):
                jdStr += jobs[i].jd.contents[j].contents[0]
                yaoqiuStr += jobs[i].yaoqiu.contents[j].contents[0]
            jd = Tkinter.Text(self.infoFrame, height=7, width=60)
            jd.insert(1.0, jdStr)
            jd.grid(row=i, column=1)
            yaoqiu = Tkinter.Text(self.infoFrame, height=7, width=60)
            yaoqiu.insert(1.0, yaoqiuStr)
            yaoqiu.grid(row=i, column=2)

        self.infoFrame.pack()

top = Tkinter.Tk()
#top.geometry('600x400')

app = App(top)
top.mainloop()
