import math
import numpy as np
import matplotlib.pyplot as plt

pi = math.pi
t = 0
u = []
k = 1
ans = 0
nx = 33
lx = 1.0
delx = lx / nx
x = 0
lx = 1.0
top = 30

while x < lx:
    ans = 0
    for m in range(0,top):
        ans = ans +  ((-1)**m/(2*m+1)**2)*(math.sin((2*m+1)*pi*x))*math.exp(-(2*m+1)**2*pi**2*k*t)
    ans2 = 8/(pi**2) * ans
    u.append(ans2)
    x = x + delx

print(u)
print(x)

yoko = np.arange(0,len(u),1)
plt.plot(yoko,u)
plt.show()
