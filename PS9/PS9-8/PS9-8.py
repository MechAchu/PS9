from array import *
import matplotlib.pyplot as plt

Nt = int(input("Enter Nt: "))
dt = float(input("Enter dt: "))
Nx = int(input("Enter Nx: "))
dx = float(input("Enter dx: "))
D = float(input("Enter D: "))

Ddtodx2 = (D*dt)/(dx**2)
rho = array('f', [0.0])
x = 0
xaxis = array('f', [x])
yaxis = array('f', [0.0])

for ix in range(1, Nx):
    rho.append(0.0)

rho.insert(int(Nx/2), int(1))

newrho = array('f', [0.0])
for ix in range(1, Nx):
    newrho.append(0.0)

for it in range(1, Nt):
    t = dt*it
    for ix in range(1, Nx):
        newrho[ix] = rho[ix] + Ddtodx2*(rho[ix-1] - 2 * rho[ix] + rho[ix+1])
    for ix in range(1, Nx):
        rho[ix] = newrho[ix]

for ix in range(0, Nx):
    x = dx*ix

    xaxis.append(x)
    yaxis.append(rho[ix])

plt.figure(1)
plt.plot(xaxis, yaxis)
plt.show()
