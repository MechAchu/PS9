from array import *
import matplotlib.pyplot as plt

N = int(input("Enter N: "))
dt = float(input("Enter dt: "))
x = float(input("Enter x: "))
y = float(0)
vx = float(0)
vy1 = float(input("Enter vy1: "))
vy2 = float(input("Enter vy2: "))
vy3 = float(input("Enter vy3: "))
Fx = float(0)
Fy = float(0)
ax = float(0)
ay = float(0)
t = 0

y1 = y
y2 = y
y3 = y

x1 = x
x2 = x
x3 = x

vx1 = vx
vx2 = vx
vx3 = vx

Fx1 = Fx
Fx2 = Fx
Fx3 = Fx

Fy1 = Fy
Fy2 = Fy
Fy3 = Fy

ax1 = ax
ax2 = ax
ax3 = ax

ay1 = ay
ay2 = ay
ay3 = ay

G = 6.67 * (10 ** -11)
Ms = 2 * (10 ** 30)
Me = 6 * (10 ** 24)
R = 1.5 * (10 ** 11)
V = 3 * (10 ** 4)
F = (G*Ms*Me)/(R ** 2)

timesave = array('f', [0.])
x1save = array('f', [x1])
x2save = array('f', [x2])
x3save = array('f', [x3])
y1save = array('f', [y1])
y2save = array('f', [y2])
y3save = array('f', [y3])


for i in range(1, N):
    x1 += vx1*dt
    x2 += vx2*dt
    x3 += vx3*dt
    y1 += vy1*dt
    y2 += vy2*dt
    y3 += vy3*dt
    Fx1 = (-F*x1)/R
    Fx2 = (-F*x2)/R
    Fx3 = (-F*x3)/R
    Fy1 = (-F*y1)/R
    Fy2 = (-F*y2)/R
    Fy3 = (-F*y3)/R
    ax1 = Fx1/Me
    ax2 = Fx2/Me
    ax3 = Fx3/Me
    ay1 = Fy1/Me
    ay2 = Fy2/Me
    ay3 = Fy3/Me
    vx1 += ax1*dt
    vx2 += ax2*dt
    vx3 += ax3*dt
    vy1 += ay1*dt
    vy2 += ay2*dt
    vy3 += ay3*dt
    t = dt*i
    timesave.append(t)
    x1save.append(x1)
    x2save.append(x2)
    x3save.append(x3)
    y1save.append(y1)
    y2save.append(y2)
    y3save.append(y3)

plt.figure(1)
plt.subplot(111)
plt.plot(x1save, y1save, label="Velocity = 15000")
plt.plot(x2save, y2save, label="Velocity = 30000")
plt.plot(x3save, y3save, label="Velocity = 60000")
plt.legend(loc="lower right")
plt.xlabel('Horizontal Position')
plt.ylabel('Vertical Position')
plt.show()
