# import time
# print(time.time())
# fmt = time.strftime('%H:%M:%S')
# print(fmt)
# fmt1 = time.strftime('%Y-%m-%d')
# print(fmt1,fmt)
# fmt2 = time.strftime('%c')
# print(fmt2)
#
# truct_time = time.localtime()
# print(time.localtime())
#
# str_time = '2018-2-2'
# str_time1 = time.strptime(str_time,'%Y-%m-%d')
# print(str_time1)
# str_time2 = time.mktime(str_time1)
# print(str_time2)
#
# timestamp = 3500000000
# fftime = time.localtime(timestamp)
# fftime1 = time.strftime('%Y-%m-%d %H:%M:%S',fftime)
# print(fftime1)

# import random
# # print(random.random())
# # print(random.uniform(2,3))
# # print(random.randint(1,2))
# # print(random.randrange(1,20,1))
#
# lst = [1,2,3,4,('a','b'),'cc','dd']
# ret = random.choice(lst)#随机抽
# print(ret)
# ret1 = random.sample(lst,3)#随机抽多个
# print(ret1)
# random.shuffle(lst)#乱序
# print(lst)


import os
# import time
# ret = os.stat('E:\pythonProject')
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(ret.st_atime)))
path = 'E:\pythonProject\day23.py'
# ret = os.path.dirname(path)
# print(ret)
# ret1 = os.path.basename(path)
# print(ret1)

# ret = os.path.isabs(path)
# print(ret)

# ret = os.path.isdir(path)
# ret1 = os.path.isfile(path)
# print(ret,ret1)

# ret = os.path.getsize(pat h)
# print(ret)


# print(os.getcwd())

# import sys
# print(sys.path)
# values = [11, 22, 33,44,55,66,77,88,99,90]
#
# my_dict = {}
#
# for value in  values:
#     if value>66:
#         if 'k1' in my_dict.keys():
#             my_dict['k1'].append(value)
#         else:
#             my_dict['k1'] = [value]
#     else:
#         if 'k2' in my_dict.keys():
#             my_dict['k2'].append(value)
#         else:
#             my_dict['k2'] = [value]
# print(my_dict)

#原生字典解决方法

#原生字典解决方法