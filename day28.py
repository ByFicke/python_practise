import os
import re
#re模块match方法，从头匹配，只匹配开头
# ret = re.match('\d+','ysgdhuashg123')
# print(ret)#none
# ret1 = re.match('\d+','123ysgdhuashg123')
# print(ret1)#<re.Match object; span=(0, 3), match='123'>

#切割split
# s1 = 'alex|egon|boss_jin'
# s2 = s1.split('|')
# print(s2)
# s1 = 'alex21egon45boss_jin'
# ret = re.split('\d+',s1)#按正则要求分割
# print(ret)#['alex', 'egon', 'boss_jin']
# s2 = 'alex21egon45boss_jin'
# ret1 = re.split('(\d+)',s2)#按正则要求分割,加了（）分组同时保留分组内容
# print(ret1)#['alex', '21', 'egon', '45', 'boss_jin']

#sub替换
# s1 = 'alex|egon|boss_jin'
# print(s1.replace('|', '='))
# s2 = 'alex12egon345boss_jin'
# print(re.sub('\d+', '|', s2))
# print(re.sub('\d+', '|', s2,1))
# ret = re.subn('\d+','|',s2)#subn在sub基础上在返回替换次数
# print(ret)

#finditer 节省空间，返回可迭代对象
# s2 = 'alex12egon345boss_jin'
# ret = re.finditer('\d+',s2)
# print(ret)
# for i in ret:
#     print(i)

#compile 编译正则规则
# s2 = 'alex12egon345boss_jin'
# com = re.compile('\d+')
# print(com.search(s2).group())
# print(com.findall(s2))
# ret = com.finditer(s2)
# for i in ret:
#     print(i.group())

# pattern = r'<(?P<tag>.*?)>.*?</(?P=tag)>'#引用tag组名或者r'<(.*?)>.*?</\1>'引用第一组名
# ret = re.search(pattern,'<h1>函数</h1>')
# print(ret)
# if ret:
#     print(ret.group())

#异常处理
l= ['登录','注册']
try:
    num = int(input('>>>'))
    print(l[num - 1])
except (ValueError,NameError,IndexError):
    print('输入错误')
# except Exception as e:  #万能异常as显示异常问题
#     print(e)

