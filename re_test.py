'''
@Author: AnakinJiang
@Email: jiangjinpeng319 AT gmail.com
@Descripttion: 
@Date: 2019-09-03 21:57:09
@LastEditors: AnakinJiang
@LastEditTime: 2019-09-04 10:26:07
'''
import re

# 匹配不少于两个阿拉伯数字开始的行
regular_v1 = re.findall("^[0-9][0-9]+","25regularexpression")
print (regular_v1)# 
regular_v2 = re.findall("^[0-9][0-9]+","34786match")
print (regular_v2)# 
regular_v3 = re.findall("^[0-9][0-9]+","a 34 not match")
print (regular_v3)# 
regular_v4 = re.findall("^[0-9][0-9]+","5too")
print (regular_v4)# 