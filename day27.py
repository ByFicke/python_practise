import re
# ret = re.findall('\d+','SAUDGHUIASHDG12346sdad56419')
# print(ret)
#
# ret1 = re.search('\d+','SAUDGHUIASHDG12346sdad56419')
# print(  ret1.group())

# ret = re.search('\d[*/][\d]','2*3/4*5')
# print(ret.group())
# \d(\.\d)?[*/][\d]

ret = re.search('\d(\.\d)?[*/][\d]','1.5*5')#不能用findall,findall会优先显示（）组合中的内容
print(ret.group())

ret = re.findall('\d(?:\.\d)?[*/][\d]','1.5*5')#不能用findall,findall会优先显示（）组合中的内容,可在组合开始前加？：取消优先显示
print(ret)
