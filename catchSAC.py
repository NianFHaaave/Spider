# coding:utf-8
import urllib.request
import requests
import re
import os
import importlib
import chardet
import sys
import operator
import datetime
from w3lib.html import remove_tags
from bs4 import BeautifulSoup
from lxml import etree
from time import sleep
from threading import Thread
import http.cookiejar
import io
import matplotlib.pyplot as plt
import numpy as np
import winreg
import time

path1=os.getcwd()
Te1 = ''
Te2 = ''
Te3 = ''
PT1 = 0.288
PT2 = 0.568
PS = 0.32
P1 = 0
P2 = 0
P3 = 0



def gethtml1(date):
    formdata = {
        }
    data = urllib.parse.urlencode(formdata).encode('utf-8')
    headers = {
        '',
        }
    url = ''
    rlog = urllib.request.Request(url, headers = headers, data = data)
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    rlogse = opener.open(rlog)
    a = []
    b = []
    for i in cookie:
        a.append(i.name)
        b.append(i.value)
    url = ''
    c = ''
    for i in range(len(a)):
        c = c + a[i] + '=' + b[i]+'; '
    cookie = c + 'Lang=en'
    headers = {
           }
    req=urllib.request.Request(url,headers=headers)
    page = urllib.request.urlopen(req)
    htmlcode = page.read().decode('utf-8')
    page.close()
    return htmlcode

def gethtml2(date):
    formdata = {
        }
    data = urllib.parse.urlencode(formdata).encode('utf-8')
    headers = {
        '',
        }
    url = ''
    rlog = urllib.request.Request(url, headers = headers, data = data)
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    rlogse = opener.open(rlog)
    a = []
    b = []
    for i in cookie:
        a.append(i.name)
        b.append(i.value)
    c = ''
    for i in range(len(a)):
        c = c + a[i] + '=' + b[i]+'; '
    date1 = datetime.datetime.strptime(date,'%Y-%m-%d')
    date2 = date1 + datetime.timedelta(days = 1)
    date1 = date1.strftime('%Y-%m-%d')
    date2 = date2.strftime('%Y-%m-%d')
    url = ''
    cookie = ''
    headers = {
        }
    req=urllib.request.Request(url,headers=headers)
    page = urllib.request.urlopen(req)
    htmlcode = page.read().decode('utf-8')
    page.close()
    return htmlcode

def gethtml3(date):
    formdata = {
        'account': '',
        'pwd': '',
        'code': ''
        }
    data = urllib.parse.urlencode(formdata).encode('utf-8')
    headers = {
        '',
        }
    url = ''
    rlog = urllib.request.Request(url, headers = headers, data = data)
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    rlogse = opener.open(rlog)
    a = []
    b = []
    for i in cookie:
        a.append(i.name)
        b.append(i.value)
    c = ''
    for i in range(len(a)):
        c = c + a[i] + '=' + b[i]+'; '
    url = ''
    cookie = ''
    headers = {
        }
    date = datetime.datetime.strptime(date,'%Y-%m-%d')
    date = date.strftime('%m/%d/%Y')
    formdata = {
        'str':''
        }
    data = urllib.parse.urlencode(formdata).encode('utf-8')
    r=urllib.request.Request(url,headers=headers)
    req=urllib.request.Request(url,data=data,headers=headers)
    page = urllib.request.urlopen(req)
    htmlcode = page.read().decode('utf-8')
    page.close()
    return htmlcode

def deal1(txt):
    reg = r'{"dt":.*?\}'
    regneed = re.compile(reg)
    list1 = regneed.findall(txt)
    a0=[]
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    a5=[]
    reg1 = re.compile(r':(.*?),')
    ind1 = 0
    t1=[]
    for i in list1:
        list2 = reg1.findall(i)
        ind2 = 0
        for j in list2:
            j=j.strip(':').strip(',').strip('"')
            if ind2 == 0:
                a0.append(j)
            elif ind2 == 1:
                a1.append(float(j))
            elif ind2 == 2:
                a2.append(float(j))
            elif ind2 == 3:
                a3.append(float(j))
            elif ind2 == 4:
                a4.append(float(j))
            else:
                a5.append(float(j))
            ind2 = ind2 + 1
        t1.append(a3[ind1]-a4[ind1])
        ind1 = ind1 + 1
    global P1,PT1,PT2,PS
    temp = 0
    if ind1>95:
        for i in range(95):
            if t1[i]>0:
                temp = temp +(PT1+PS)*t1[i]
            else:
                temp = temp +(PT1)*t1[i]
            temp = round(temp,3)
        for i in range(96,ind1):
            if t1[i]>0:
                temp = temp +(PT2+PS)*t1[i]
            else:
                temp = temp +(PT2)*t1[i]
            temp = round(temp,3)
    else:
        for i in range(ind1):
            if t1[i]>0:
                temp = temp +(PT1+PS)*t1[i]
            else:
                temp = temp +(PT1)*t1[i]
            temp = round(temp,3)
    P1 = temp
    x = np.arange(ind1)
    y1 = np.array(a1)
    y2 = np.array(a2)
    y3 = np.array(a3)
    y4 = np.array(a4)
    y5 = np.array(a5)
    plt.subplot(2,2,1)
    plt.title("Portal.global-mde")
    plt.axis([0, 288, -300, 2000])
    plt.plot(x,y1,'r',label = 'PV Generation')
    plt.plot(x,y2,'g',label = 'Load Consumption')
    plt.plot(x,y3,'#8B008B',label = 'Grid Feed-in')
    plt.plot(x,y4,'#00FF7F',label = 'Grid Supply')
    #plt.plot(x,y5,'#FF69B4')
    plt.legend()
    
def deal2(txt):
    reg = r'{"dt":.*?\}'
    regneed = re.compile(reg)
    list1 = regneed.findall(txt)
    a0=[]
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    a5=[]
    reg1 = re.compile(r':(.*?),')
    ind1 = 0
    for i in list1:
        list2 = reg1.findall(i)
        ind2 = 0
        for j in list2:
            j=j.strip(':').strip(',').strip('"')
            if ind2 == 0:
                a0.append(j)
            elif ind2 == 1:
                try:
                    j = float(j)
                except:
                    j = float(0)
                a1.append(j)
            elif ind2 == 2:
                try:
                    j = float(j)
                except:
                    j = float(0)
                a2.append(j)
            elif ind2 == 3:
                try:
                    j = float(j)
                except:
                    j = float(0)
                a3.append(j)
            elif ind2 == 4:
                try:
                    j = float(j)
                except:
                    j = float(0)
                a4.append(j)
            else:
                pass
            ind2 = ind2 + 1
        ind1 = ind1 + 1
    global P2,PT1,PT2,PS
    temp = 0
    if ind1>95:
        for i in range(95):
            if a3[i]>0:
                temp = temp +(PT1+PS)*a3[i]
            else:
                temp = temp +(PT1)*a3[i]
            temp = round(temp,3)
        for i in range(96,ind1):
            if a3[i]>0:
                temp = temp +(PT2+PS)*a3[i]
            else:
                temp = temp +(PT2)*a3[i]
            temp = round(temp,3)
    else:
        for i in range(ind1):
            if a3[i]>0:
                temp = temp +(PT1+PS)*a3[i]
            else:
                temp = temp +(PT1)*a3[i]
            temp = round(temp,3)
    P2 = temp
    x = np.arange(ind1)
    y1 = np.array(a1)
    y2 = np.array(a2)
    y3 = np.array(a3)
    plt.subplot(2,2,2)
    plt.title("Solax-portal")
    plt.axis([0, 288, -300, 2300])
    plt.plot(x,y1,'r',label = 'Out')
    plt.plot(x,y2,'g',label = 'In')
    plt.plot(x,y3,'b',label = 'Grid Feed-in')
    plt.legend()

def deal3(txt):
    a0=[]
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    a5=[]
    listload = re.findall('''"load":\s(.*?)]''',txt,re.S)
    reg1 = r'''"x":\s"(.*?)"'''
    regn1 = re.compile(reg1)
    list1 = regn1.findall(str(listload))
    ind = 0
    for i in list1:
        a0.append(i)
        ind = ind + 1
    reg2 = r'"y":\s(\S*\d+.\d+)'
    regn2 = re.compile(reg2)
    list2 = regn2.findall(str(listload))
    for i in list2:
        a1.append(float(i))#load

    listmeter = re.findall('''"meter":\s(.*?)]''',txt,re.S)
    reg3 = r'"y":\s(\S*\d+.?\d+?)'
    regn3 = re.compile(reg3)
    list3 = regn3.findall(str(listmeter))
    for i in list3:
        a2.append(float(i))#meter

    listpv = re.findall('''"pv":\s(.*?)]''',txt,re.S)
    reg4 = r'"y":\s(\S*\d+.\d+)'
    regn4 = re.compile(reg4)
    list4 = regn4.findall(str(listpv))
    for i in list4:
        a3.append(float(i))#pv

    listbattery = re.findall('''"battery":\s(.*?)]''',txt,re.S)
    reg5 = r'"y":\s(\S*\d+.\d+)'
    regn5 = re.compile(reg5)
    list5 = regn5.findall(str(listbattery))
    for i in list5:
        a4.append(float(i))#battery

    listsoc = re.findall('''"soc":\s(.*?)]''',txt,re.S)
    reg6 = r'"y":\s(\S*\d+)'
    regn6 = re.compile(reg6)
    list6 = regn6.findall(str(listsoc))
    for i in list6:
        a5.append(float(i))#soc
        
    global P3,PT1,PT2,PS
    temp = 0
    if ind>95:
        for i in range(95):
            if a2[i]>0:
                temp = temp +(PT1+PS)*a2[i]
            else:
                temp = temp +(PT1)*a2[i]
            temp = round(temp,3)
        for i in range(96,ind):
            if a2[i]>0:
                temp = temp +(PT2+PS)*a2[i]
            else:
                temp = temp +(PT2)*a2[i]
            temp = round(temp,3)
    else:
        for i in range(ind):
            if a2[i]>0:
                temp = temp +(PT1+PS)*a2[i]
            else:
                temp = temp +(PT1)*a2[i]
            temp = round(temp,3)
    P3 = temp
    
    x = np.arange(ind)
    y1 = np.array(a1)
    y2 = np.array(a2)
    y3 = np.array(a3)
    y4 = np.array(a4)
    y5 = np.array(a5)
    plt.subplot(2,2,3)
    plt.title("Semsportal")
    plt.axis([0, 288, -300, 2000])
    timelist=range(1,25)
    plt.plot(x,y1,'r',label = 'Load')
    plt.plot(x,y2,'g',label = 'Meter')
    plt.plot(x,y3,'b',label = 'PV')
    plt.plot(x,y4,'#FF00FF',label= 'Battery')
    plt.plot(x,y5,'#8B008B',label = 'Soc')
    plt.legend()
    
def comb(date):
    global Te1
    try:
        temp = gethtml1(date)
    except:
        print('NetError——Portal.global-mde')
        deal1(Te1)
    else:
        deal1(temp)
        Te1 = temp
    global Te2
    try:
        temp = gethtml2(date)
    except:
        print('NetError——Solax-portal')
        deal2(Te2)
    else:
        deal2(temp)
        Te2 = temp
    global Te3
    try:
        temp = gethtml3(date)
    except:
        
        print('NetError——Semsportal')
        deal3(Te3)
    else:
        deal3(temp)
        Te3 = temp
    income = [P1,P2,P3]
    #print(income)
    namelist = ['GMDE','Solax','Sems']
    plt.subplot(2,2,4)
    plt.bar(range(3),income,color='rgb',tick_label = namelist,width = 0.5)

startdate = lock()
plt.figure("JinKo")
plt.subplots_adjust(left=0.08, bottom=0.08, right=0.92, top=0.92, wspace=0.33, hspace=0.40)
plt.ion()
while 1:
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    date1 = str(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
    #date = '2019-1-25'
    print("Reload data at "+date1)
    comb(date)
    plt.show()
    plt.pause(150)
    plt.clf()
