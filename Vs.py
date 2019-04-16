# coding:utf-8
import urllib.request
import re
import os
import importlib
import ssl


path1=os.getcwd()

def pathname(x):    
    newpath1=os.path.join(path1,'Vicioussyndicate')
    if not os.path.isdir(newpath1):
        os.mkdir(newpath1)
    t=os.path.join(newpath1,'%s.png' % x)
    return t

def gethtml(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
    req=urllib.request.Request(url,headers=headers) 
    htmlcod=urllib.request.urlopen(req)
    htmlcode=htmlcod.read()
    htmlcod.close()
    return htmlcode

def getimage(htmlcode):
    reg = r'<img class="aligncenter size-full wp-image-.*?\" src="(.*?\.png)" alt="" width=".*?\" height=".*?\" /></a> </div>'
    regimg = re.compile(reg)
    htmlcode=htmlcode.decode('utf8')
    imglist = regimg.findall(htmlcode)
    x = 1
    for img in imglist:
        print ("正在加载第 %s" %x + "张图片")
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(img, pathname(x))
        x += 1

print ('vs炉石周报获取！')
input()
url = 'http://data-reaper-report.vicioussyndicate.com/'
print ('----------正在获取最新的标准vs周报---------')
htmlcode = gethtml(url)
print ('----------正在下载图片---------')
getimage(htmlcode)
print ('-----------下载成功-----------')
input('Press Enter to exit')
