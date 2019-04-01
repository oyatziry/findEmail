#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import re
import urllib2

#Problem 1
def mytype(v):
    if re.findall(r'[\d+](?=[,])', v):
        print('list')
    elif re.match(r'^[\d]+$', v):
        print('integer')
    elif re.match(r'[\d+][\.][\d+]', v):
        print('float')
    else:
       print('string')
        
#mytype('hello')
#mytype('07039')
#mytype('5.08')
#mytype('[1,2,3]')
        
   
     
#Problem 2
def findpdfs(L):
    list_L = L.split(',')
    pdf_list = []
    for i in list_L:
        pdf = re.search(r'(.+)\.pdf', i)
        if pdf:
            pdf_list.append(i)
    return pdf_list        
    
#findpdfs('"IMG2309.jpg", "lecture1.pdf", "homework.py", "lecture2.pdf"')  


#Problem 3
def findemail(url):
    page=urllib2.urlopen(url).read()
    page=str(page)
    #print page
    emailRegex = r'\w+\s?(@|AT)\s?(\w+(\s*(\.|DOT)*)\s*)+'
    email = re.search(emailRegex, page)
    if email:
        return email.group()
    
#findemail("http://www.math.ucla.edu/~hangjie/contact")      
