from array import *
import matplotlib.pyplot as plt

N = int(input("Enter N: "))
dt = float(input("Enter dt: "))
k = float(input("Enter k: "))
m = float(input("Enter m: "))
b = float(input("Enter b: "))
x1 = float(input("Enter First Initial x: "))
x2 = float(input("Enter Second Initial x: "))
x3 = float(input("Enter Third Initial x: "))
v = float(input("Enter Initial v: "))

v1 = v
v2 = v
v3 = v

time = array('f', [0.])
x1save = array('f', [x1])
x2save = array('f', [x2])
x3save = array('f', [x3])
v1save = array('f', [v1])
v2save = array('f', [v2])
v3save = array('f', [v3])

for i in range(1,N):
    t = dt*i
    x1 += v1*dt
    x2 += v2*dt
    x3 += v3*dt
    v1 += (((-k*x1)/m) - (b*(x1**3)))*dt
    v2 += (((-k*x2)/m) - (b*(x2**3)))*dt
    v3 += (((-k*x3)/m) - (b*(x3**3)))*dt
    time.append(t)
    x1save.append(x1)
    x2save.append(x2)
    x3save.append(x3)
    v1save.append(v1)
    v2save.append(v2)
    v3save.append(v3)

plt.figure(1)
plt.subplot(211)
plt.plot(time, x1save)
plt.plot(time, x2save)
plt.plot(time, x3save)
plt.xlabel('Time')
plt.ylabel('Position')
plt.subplot(212)
plt.plot(time, v1save)
plt.plot(time, v2save)
plt.plot(time, v3save)
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.show()

'''
As the initial x value increases the period of the system
will decrease for an anharmonic spring.
'''
