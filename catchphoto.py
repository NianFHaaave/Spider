# coding:utf-8
import urllib.request
import re
import os
import importlib


path1=os.getcwd()

def pathname(x):    
    newpath1=os.path.join(path1,'tiebapictures')
    if not os.path.isdir(newpath1):
        os.mkdir(newpath1)
    t=os.path.join(newpath1,'%s.jpg' % x)
    return t

def gethtml(url):
    page = urllib.request.urlopen(url)
    htmlcode = page.read()
    return htmlcode

def getimage(htmlcode):
    reg = r'<img class="BDE_Image".*? src="(.*?\.jpg)" '
    regimg = re.compile(reg)
    htmlcode=htmlcode.decode('utf8')#python3
    imglist = regimg.findall(htmlcode)
    x = 1
    for img in imglist:
        print ("It's downloading %s" %x + "th's picture")
        urllib.request.urlretrieve(img, pathname(x))
        x += 1

print ('gainfromtieba！')
a=input('p/')
url = 'https://tieba.baidu.com/p/'+a
print ('----------loading---------')
htmlcode = gethtml(url)
print ('----------downloading---------')
getimage(htmlcode)
print ('-----------succeeded-----------')
input('Press Enter to exit')
