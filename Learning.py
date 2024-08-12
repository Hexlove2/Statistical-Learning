import numpy as np
x = np.random.normal(size = 50)
print(x)
rng = np.random.default_rng(103)
print(rng.normal(scale = 6, size = 50))

import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot
y = rng.normal(size = 50)
fig, ax = subplot(figsize = (8, 8))
ax.plot(x, y)
plt.show()