#!/Library/Frameworks/Python.framework/Versions/Current/bin/python2.7
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

a = np.loadtxt('/data/pngit/marion/test.txt')
if 0:
	from mayavi import mlab
	s = mlab.mesh(a[1],a[2],a[3])
	mlab.show()

if 1:
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(a[1],a[2],a[3])

    plt.show()