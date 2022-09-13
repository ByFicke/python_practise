import json
# dic = {'name1':'荷花1','sex1':'male1'}
# str_dic = json.dumps(dic,ensure_ascii=False)
# with open('json_file','a',encoding='utf-8') as f:
#     f.write(str_dic)


#
# with open('json_file','r',encoding='utf-8') as f:
#     content = f.read()
# ret = json.loads(content)
# print(ret)

# dic = {'name1':'荷花1','sex1':'male1'}
# with open('json_file','w',encoding='utf-8') as f:
#     json.dump(dic,f)

# dic = {'name1':'荷花1','sex1':'male1'}
# with open('json_file','w',encoding='utf-8') as f:
#     json.dump(dic,f,ensure_ascii=False)
#     json.dump(dic, f, ensure_ascii=False)
#     json.dump(dic, f, ensure_ascii=False)
#     json.dump(dic, f, ensure_ascii=False)

# with open('json_file','r',encoding='utf-8') as f:
#     dic = json.load(f)
#     print(dic)

# dic1 = {'name1':'荷花1','sex1':'male1'}
# dic2 = {'name2':'荷花2','sex2':'male2'}
# dic3 = {'name3':'荷花3','sex3':'male3'}
# def my_dumps(dic):
#     with open('json_file','a',encoding='utf-8') as f:
#         dic_str = json.dumps(dic)
#         f.write(dic_str+'\n')
# my_dumps(dic1)
# my_dumps(dic2)
# my_dumps(dic3)
#
# with open('json_file','r',encoding='utf-8') as f:
#     for line in f:
#         dic = json.loads(line.strip())
#         print(dic)

# dic1 = {'name1':'荷花1','sex1':'male1'}
# dic2 = {'name2':'荷花2','sex2':'male2'}
# dic3 = {'name3':'荷花3','sex3':'male3'}
# def my_dumps(dic):
#     with open('json_file','a',encoding='utf-8') as f:
#         syr = json.dumps(dic)
#         f.write(syr+'\n')
#
# my_dumps(dic1)
# my_dumps(dic2)
# my_dumps(dic3)
#
# with open('json_file','r',encoding='utf-8') as f:
#         for line in f:
#             dic = json.loads(line.strip())
#             print(dic)

import  pickle
class Course():
    def __init__(self,name,price):
        self.name = name
        self.price = price
# python = Course('python',29800)
# with open('pickle_file','wb') as f:
#     pickle.dump(python,f)

with open("pickle_file",'rb') as f:
    course = pickle.load(f)
print(course.name)


