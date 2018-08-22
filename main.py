import numpy as np
import math
import random
import pyJHTDB
import matplotlib.pyplot as plt

def loadData(x, time):
    # load shared library
    lTDB = pyJHTDB.libJHTDB()
    #initialize webservices
    lTDB.initialize()
    
    for t in np.arange(time.size):
        temp = lTDB.getData(time[t], x, data_set = 'channel', sinterp = 4, getFunction = 'getVelocity')
        if t == 0:
            u = temp[:, :, 0]
        else:
            u = np.dstack((u, temp[:, :, 0]))

    lTDB.finalize()
    return u

time = np.array([0, 1.56, 2])
t1 = np.linspace(0, 2*3.14, 64)
t2 = np.linspace(-1, 0, 64)
x = np.zeros((t1.shape[0], t2.shape[0], 3), np.float32)
x[:, :, 0] = t1[np.newaxis, :]
x[:, :, 1] = t2[:, np.newaxis]
x[:, :, 2] = .0

u = loadData(x, time)
np.savez('data', x, u, time)
fig = plt.figure(figsize = (10, 5))
a = fig.add_subplot(121)
a.imshow(u[:, :, 2], extent = [t1[0], t1[-1] - t1[0], t2[0], t2[-1] - t2[0]], interpolation = 'none', aspect = 'equal')
plt.show()
