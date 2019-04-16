# coding:utf-8
import urllib.request
import requests


def gethtml1(l):
    url = l
    #headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
    payload={'key1':'value1','key2':['value2','value3']}
    req=requests.get(url,params=payload)
    print(req)
    print(req.text)
    print(req.url)
    req=requests.put(url,data={'key':'value'})
    print(req)
    print(req.text)


url = 'http://httpbin.org/get'
gethtml1(url)
