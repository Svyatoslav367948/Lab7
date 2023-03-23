import numpy as np
import time
import random

count = 1000000
low = -100
high = 100

npmass1 = np.random.randint(low, high, count)
npmass2 = np.random.randint(low,high, count)
# print(npmass1,npmass2)

listmass1=[]
listmass2=[]
for i in range(count):
    listmass1.append(random.randint(low, high))
for i in range(count):
    listmass2.append(random.randint(low, high))
print(listmass2, listmass1)

# measuring time first
t_startnp = time.perf_counter()
first = np.multiply(npmass1, npmass2)
all_timenp = time.perf_counter() - t_startnp
print(all_timenp)


# measuring time second
t_startlist = time.perf_counter()
lists=[]
for i in range(count):
    lists.append(listmass1[i]*listmass2[i])
all_timelist = time.perf_counter() - t_startlist
print(all_timelist)