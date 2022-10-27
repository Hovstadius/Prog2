'''
Student: David Hovstadius
Presented too: Nandini M S
Presentation date: 14/10-2022

'''

import math
import random
import matplotlib.pyplot as plt
import math
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111)

n = 1000
Ac = 0
Ak = 0
for i in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <= 1:
        plt.plot(x,y,'ro')
        Ac += 1
    else:
        plt.plot(x,y,'bo')
        Ak += 1
pie = 4*(Ac/(Ak+Ac))

print(Ac)
print(pie)
print(math.pi)

ax.set_aspect('equal', adjustable='box')
#plt.savefig(f"n{n}.png")
plt.show()

# n = 1000 : pi = 3.13
# n = 10000 : pi = 3.1324
# n = 100000 : pi = 3.1448
