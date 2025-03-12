import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([0, 2, 4, 6])
ypoints = np.array([0, 120, 60, 200])

plt.plot(xpoints, ypoints)
plt.show()
plt.close('all')