#!/Library/Frameworks/Python.framework/Versions/Current/bin/python2.7
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from numpy import *
x = loadtxt('x.txt')
y = loadtxt('y.txt')
z = loadtxt('z.txt')

print x,y,z
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x[1][:100],y[1][:100],z[1][:100])

plt.show()