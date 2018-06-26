# -*- coding: utf-8 -*-
# @Date    : 2018-06-26 23:29:53
# @Author  : minizhan (574511236@qq.com)
# @Link    : https://github.com/miniYYan

'''

题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的

顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

'''
#python数组列表(List)
# 序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。

# Python有6个序列的内置类型，但最常见的是列表和元组。

# 序列都可以进行的操作包括索引，切片，加，乘，检查成员。
# 
# 此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
# 
# 列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 
# 列表的数据项不需要具有相同的类型

#有序二位数组查找
import os

def Find(listArray , rows, columns, number):
    row = 0
    column = columns -1
    if list == None or rows < 0 or columns < 0:
        return False
    while row < rows and column >= 0:
        a = listArray[row][column]
        if a == number:
            return True
        elif a > number:
            column = column -1
        else:
            row = row +1
     
    return False

# a = [[1,2,3],[4,5,6],[7,8,9]]
a = []
# print a[2][2]

# t_Result = Find(a, 3, 3, 0)
t_Result = Find(a, 0, 0, 0)
print t_Result