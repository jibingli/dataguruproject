# -*- coding: utf-8 -*-

import re

print(re.findall('e', 'elex make love'))
print(re.search('e', 'alex make love').group())
print(re.match('e', 'alex make love'))

print(re.split('[ab]', 'abcd'))
print('===>', re.sub('a', 'A', 'alex make love', 1))
print('===>', re.sub('a', 'A', 'alex make love', 2))

obj = re.compile('\d{2}')
print(obj.search('abc123eeee').group())

a = ['wuchao', 'jinxin', 'xiaohu', 'sanpang', 'ligang', ['wuchao', 'jinxin']]
a.append('xuepeng')
a.insert(1, 'xuepeng')
a[1] = 'haidilao'
a[1:3] = ['a', 'b']

a.remove(a[0])
b = a.pop(1)
a.remove(['wuchao', 'jinxin'])

t = ['to', 'be', 'or', 'not', 'to', 'be'].count('to')
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
# index # 根据内容找位置
a = ['wuchao', 'jinxin', 'xiaohu', 'ligang', 'sanpang', 'ligang', ['wuchao', 'jinxin']]
first_lg_index = a.index("ligang")
little_list = a[first_lg_index + 1:]
second_lg_index = little_list.index("ligang")
second_lg_index_in_big_list = first_lg_index + second_lg_index + 1
# reverse
a = ['wuchao', 'jinxin', 'xiaohu', 'ligang', 'sanpang', 'ligang']
a.reverse()
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
a = ['wuchao', 'jinxin', 'Xiaohu', 'Ligang', 'sanpang', 'ligang']
a.sort()

dic = {1: 'alex', 'age': 35, 'hobby': {'girl_name': '铁锤', 'age': 45}, 'is_handsome': True}
dic = {'age': 'alex', 'age': 35, 'hobby': {'girl_name': '铁锤', 'age': 45}, 'is_handsome': True}  # 字典两大特点:无序，键唯一
# 字典的创建
a = list()
dic = {'name': 'alex'}
dic1 = {}
dic2 = dict((('name', 'alex'),))
dic3 = dict([['name', 'alex'], ])
dic1 = {'name': 'alex'}
dic1[
    'age'] = 18  # 键存在，不改动，返回字典中相应的键对应的值 ret=dic1.setdefault('age',34) #键不存在，在字典中中增加新的键值对，并返回相应的值 ret2=dic1.setdefault('hobby','girl')
# 查 通过键去查找
# dic3={'age': 18, 'name': 'alex', 'hobby': 'girl'} print(dic3['name'])
print(list(dic3.keys()))
print(list(dic3.values()))
print(list(dic3.items()))

li = [1, 2, 34, 4]
li[2] = 5
dic3 = {'age': 18, 'name': 'alex', 'hobby': 'girl'}
dic3['age'] = 55
dic4 = {'age': 18, 'name': 'alex', 'hobby': 'girl'}
dic5 = {'1': '111', '2': '222'}
dic5 = {'1': '111', 'name': '222'}
dic4.update(dic5)
dic5 = {'name': 'alex', 'age': 18, 'class': 1}
dic5.clear()  # 清空字典
del dic5  # 删除整个字典

import queue
import threading
import time

q = queue.Queue()


def product(arg):
    while True:
        q.put(str(arg) + '资源')


def consumer(arg):
    while True:
        print(arg, q.get())
        time.sleep(2)
        for i in range(7):
            t = threading.Thread(target=product, args=(i,))
            t.start()
        for j in range(24):
            t = threading.Thread(target=consumer, args=(j,))
            t.start()


# 读取csv文件方法1
import csv

csvfile = open('csvWrite.csv', newline='')  # 打开一个文件
csvReader = csv.reader(csvfile)  # 返回的可迭代类型
print(type(csvReader))
for content in csvReader:
    print(content)
    csvfile.close()  # 关闭文件
