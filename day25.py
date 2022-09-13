import hashlib
# a = 'alex1234'
# md5_obj = hashlib.md5()
# # md5_obj.update(b'alex1234')
# md5_obj.update('alex1234'.encode('utf-8'))
# ret = md5_obj.hexdigest()
# print(ret,type(ret),len(ret))

# def get_md5(h,s):
#     md5_obj = hashlib.md5(h.encode('utf-8'))
#     md5_obj.update(s.encode('utf-8'))
#     ret = md5_obj.hexdigest()
#     return ret

# username = input('请输入用户名')
# passwd = input('请输入密码')
# with open('userinfo') as f:
#     for line in f:
#         usr,pwd = line.strip().split('|')
#         if username == usr and get_md5(passwd) == pwd:
#             print('登录成功')
#             break
#         else:
#             print('错误')

# 登录注册程序
# def get_md5(h,s):
#     md5_obj = hashlib.md5(h.encode('utf-8'))
#     md5_obj.update(s.encode('utf-8'))
#     ret = md5_obj.hexdigest()
#     return ret
#
# a = input('登录/注册')
# if a.strip() == '登录':
#     username = input('请输入用户名')
#     passwd = input('请输入密码')
#     with open('userinfo') as f:
#         for line in f:
#             usr, pwd = line.strip().split('|')
#             if username == usr and get_md5(username,passwd) == pwd:
#                 print('登录成功')
#                 break
#         else:
#             print('错误')
# else:
#     username = input('请输入用户名')
#     passwd = input('请输入密码')
#     with open('userinfo','a') as f:
#         passwd1 = get_md5(username,passwd)
#         tmp = '\n' + username +'|'+passwd1
#         f.write(tmp)

# 文件解码程序
# def get_md5(s):
#     md5_obj = hashlib.md5()
#     with open(s,encoding='utf-8') as f:
#         for line in f:
#             md5_obj.update(line.encode('utf-8'))
#     ret = md5_obj.hexdigest()
#     print(ret)
# get_md5('day22.py')#3389c882277fc53e5537ff928ca06029
# get_md5('day22副本.py')#3389c882277fc53e5537ff928ca06029

# 文件验证程序
# def get_md5(s,h):
#     md5_obj = hashlib.md5()
#     md5_obj1 = hashlib.md5()
#     with open(s,encoding='utf-8') as f:
#         for line in f:
#             md5_obj.update(line.encode('utf-8'))
#     ret = md5_obj.hexdigest()
#     print(ret)
#
#     with open(h,encoding='utf-8') as file:
#         for line1 in file:
#             md5_obj1.update(line1.encode('utf-8'))
#     ret1 = md5_obj1.hexdigest()
#     print(ret1)
#
#     if ret1 == ret:
#         print('通过')
#     else:
#         print("失败")
# get_md5('day23.py','day22副本.py')

# import os
# os.chdir(r'E:\python路飞\Python\课程文件夹\day25 hashlib模块、loggin模块等\day25 hashlib模块、loggin模块等\day25 hashlib模块、loggin模块等\video')
# def get_md5(file_path,butter = 1024):
#     md5_obj =hashlib.md5()
#     file_size = os.path.getsize(file_path)
#     with open(file_path,'rb') as f:
#         while file_size:
#             content = f.read(butter)
#             file_size -=len(content)
#             md5_obj.update(content)
#         print(md5_obj.hexdigest())
# get_md5(r'4.hashlib模块2.mp4')#6f16f17ecee7e08a52b0f9919a902fb3
# get_md5(r'2.今日内容.mp4')#88db2e611a22f059a571548e1c4143f2


# 大文件验证
# import os
# os.chdir(r'E:\python路飞\Python\课程文件夹\day25 hashlib模块、loggin模块等\day25 hashlib模块、loggin模块等\day25 hashlib模块、loggin模块等\video')
# def get_md5(file_path,file_path1,butter = 1024):
#     md5_obj =hashlib.md5()
#     md5_obj1 = hashlib.md5()
#     file_size = os.path.getsize(file_path)
#     file_size1 = os.path.getsize(file_path1)
#     with open(file_path,'rb') as f:
#         while file_size:
#             content = f.read(butter)
#             file_size -=len(content)
#             md5_obj.update(content)
#         print(md5_obj.hexdigest())
#     with open(file_path1,'rb') as f1:
#         while file_size1:
#             content1 =f1.read(butter)
#             file_size1 -=len(content1)
#             md5_obj1.update(content1)
#         print(md5_obj1.hexdigest())
#     if md5_obj.hexdigest() == md5_obj1.hexdigest():
#         print('文件一致')
#     else:
#         print("文件不一致")
# get_md5(r'4.hashlib模块2.mp4','2.今日内容.mp4')

# 日志
import logging
# 简单配置
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     filename = 'test.log')

# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
# format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s'

# 对象配置
logger =logging.getLogger()#创建对象
fh = logging.FileHandler('my_log.log')#创建文件操作符
sh = logging.StreamHandler()
fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s')
fmt1= logging.Formatter('%(asctime)s - %(name)s[line:%(lineno)d] - %(levelname)s -%(module)s:  %(message)s')
fh.setFormatter(fmt)
sh.setFormatter(fmt1)
logger.addHandler(fh)
logger.addHandler(sh)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')