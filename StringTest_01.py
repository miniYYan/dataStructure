#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-27 00:27:30
# @Author  : minizhan (574511236@qq.com)
# @Link    : https://github.com/miniYYan
'''
    替换空格
'''

import os
import re

def spaceReplace(a):
    tmp = re.sub(r' ','%20',a)
    return tmp

def spaceReplace_01(a):
    length = len(a)
    b = ''
    for i in range(length -1):
        if a[i] == " ":
#             b+="%20"
            a+="%20"
        else:
            b+=a[i]
        ++i
    return b
a = 'a a dsf df'
t_result = spaceReplace(a)
t_result_01 = spaceReplace_01(a)
# b=a.replace(' ','%20')
print t_result_01