from array import *
import matplotlib.pyplot as plt

Nt = int(input("Enter Nt: "))

rows, cols = (301, 201)

V = [[0 for i in range(cols)] for j in range(rows)]
newV = [[0 for i in range(cols)] for j in range(rows)]

xaxis = array('f', [0.0])
yaxis = array('f', [0.0])

dx = 0.1
dy = 0.1

for iy in range(0, 21):
    for ix in range(0, 31):
        V[ix][iy] = 0.0;

iy = 20
for ix in range(0, 31):
    V[ix][iy] = 8.0

for it in range(0, Nt):
    for iy in range(1, 20):
        for ix in range(1, 30):
            newV[ix][iy] = 0.25*(V[ix+1][iy] + V[ix-1][iy] + V[ix][iy+1] + V[ix][iy-1])
    for iy in range(1, 20):
        for ix in range(1, 30):
            V[ix][iy] = newV[ix][iy]
    for iy in range(0, 21):
        y = 1
        for ix in range(0, 31):
            x = dx*ix
            xaxis.append(x)
            yaxis.append(V[ix][iy])

plt.figure(1)
plt.plot(xaxis, yaxis)
plt.show()
