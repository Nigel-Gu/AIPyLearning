import torch as th
import random as rd
import numpy as np


x=th.rand(5,3)
print(x)
y=rd.randint(1,20)
print(y)
y=np.array(y)
x=x+y

print(x)