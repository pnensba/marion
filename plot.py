#!/Library/Frameworks/Python.framework/Versions/Current/bin/python2.7
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

a = np.loadtxt('test.txt')
fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.plot(a[1],a[2],a[3])
ax.plot(a[0],a[1],a[2])
plt.show()