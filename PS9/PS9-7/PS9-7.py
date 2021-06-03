import numpy
import random

N = int(input("Enter N: "))
R = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for i in range(0, N):
    R = random.random()
    sum1 += R
    sum2 += R**2
    sum3 += R**3
    sum4 += R**4

print(str(sum1/N) + ', ' + str(sum2/N) + ', ' + str(sum3/N) + ', ' + str(sum4/N))
