# import my_module
# name = 'ficke'
# my_module.read1()
# my_module.name ='ficke'
# my_module.read1()
# print(my_module.name)
import time
from importlib import reload

import my_module
from my_module import *
print(my_module.name)
time.sleep(10)
reload(my_module)
print(my_module.name)

