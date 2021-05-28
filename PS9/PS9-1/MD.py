from array import *
import matplotlib.pyplot as plt

N = int(input("Enter N: "))
dt = float(input("Enter dt: "))
k = float(input("Enter k: "))
m = float(input("Enter m: "))
x = float(input("Enter Initial x: "))
v = float(input("Enter Initial v: "))

time = array('f', [0.])
xsave = array('f', [x])
vsave = array('f', [v])

for i in range(1,N):
    t = dt*i
    x += v*dt
    v += (-k*x*dt)/m
    time.append(t)
    xsave.append(x)
    vsave.append(v)

for i in range(1,N):
    t = dt*i
    x += v*dt
    v += (-k*x*dt)/m
    print(time[i], xsave[i])

plt.figure(1)
plt.subplot(211)
plt.plot(time, xsave)
plt.xlabel('Time')
plt.ylabel('Position')
plt.subplot(212)
plt.plot(time, vsave)
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.show()

'''
The initials only matter if it's zero or a different number.
We get the same graph for any positive position or velocity.
The graph itself changes with negative initial values but the period remains
the same.
'''
