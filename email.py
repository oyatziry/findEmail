#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import re
import urllib2

def findemail(url):
    page=urllib2.urlopen(url).read()
    page=str(page)
    #print page
    emailRegex = r'\w+\s?(@|AT)\s?(\w+(\s*(\.|DOT)*)\s*)+'
    email = re.search(emailRegex, page)
    if email:
        return email.group()
    
#findemail("http://www.math.ucla.edu/~hangjie/contact")      
