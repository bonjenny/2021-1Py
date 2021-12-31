# -*- coding: utf-8 -*-
"""
Created on Fri May 14 19:33:53 2021

@author: bonje
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, ls=":", label="sin")
plt.plot(x, y2, ls="--", label="cos")
# linestyle: solid, dashed, dotted, dashdot

plt.title('Graph of sin cos')
plt.legend(loc=3)
plt.grid()
plt.show()
