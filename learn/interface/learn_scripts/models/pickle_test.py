import matplotlib.pyplot as plt
import numpy as np
import pickle

ax = plt.subplot(111)
x = np.linspace(0, 10)
y = np.exp(x)
plt.plot(x, y)
with open('myplot.pkl','wb') as fid:
    pickle.dump(ax, fid)