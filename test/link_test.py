from linklist import *
import time

list = range(999999)

link = Linklist()
link.inti__list(list)

start_time = time.time()
# for item in list:
#     print(item)
list.add(8866)
print("时间是：",time.time()-start_time)