from array import *
import matplotlib.pyplot as plt

N = int(input("Enter N: "))
dt = float(input("Enter dt: "))
x = float(input("Enter Initial x: "))
y = float(input("Enter Initial y: "))
vx = float(input("Enter Initial vx: "))
vy = float(input("Enter Initial vy: "))

time = array('f', [0.])
xsave = array('f', [x])
ysave = array('f', [y])
vxsave = array('f', [vx])
vysave = array('f', [vy])

for i in range(1,N):
    t = dt*i
    x += vx*dt
    y += vy*dt
    vx = vx
    vy += (-9.8)*dt
    time.append(t)
    xsave.append(x)
    ysave.append(y)
    vxsave.append(vx)
    vysave.append(vy)

plt.figure(1)
plt.subplot(411)
plt.plot(time, xsave)
plt.xlabel('Time')
plt.ylabel('Horizontal Position')
plt.subplot(412)
plt.plot(time, ysave)
plt.xlabel('Time')
plt.ylabel('Vertical Position')
plt.subplot(413)
plt.plot(time, vxsave)
plt.xlabel('Time')
plt.ylabel('Horizontal Velocity')
plt.subplot(414)
plt.plot(time, vysave)
plt.xlabel('Time')
plt.ylabel('Vertical Velocity')
plt.show()
