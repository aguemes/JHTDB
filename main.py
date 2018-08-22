import numpy as np
import math
import random
import pyJHTDB
import matplotlib.pyplot as plt

# load shared library
lTDB = pyJHTDB.libJHTDB()
#initialize webservices
lTDB.initialize()

t1 = np.linspace(0, 2*3.14, 64)
t2 = np.linspace(0, 1, 64)
x = np.zeros((t1.shape[0], t2.shape[0], 3), np.float32)
x[:, :, 0] = t1[np.newaxis, :]
x[:, :, 1] = t2[:, np.newaxis]
x[:, :, 2] = .0

T = pyJHTDB.dbinfo.channel['time'][-1]
time = np.random.random()*T
u = lTDB.getData(time, x, data_set = 'channel', sinterp = 4, getFunction='getVelocity')
np.savez('data', x, u, time)
e = np.sum(u**2, axis = 2)
fig = plt.figure(figsize = (10, 5))
a = fig.add_subplot(121)
a.imshow(u[:,:,0], extent = [t1[0], t1[-1] - t1[0], t2[0], t2[-1] - t2[0]], interpolation = 'none', aspect = 'equal')
plt.show()
lTDB.finalize()
