import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def cal_heat(v):
    return v ** 2

def cool_down(heat):
    heat = heat - COOL_SPEED / 50
    if heat < 0:
        heat = 0
    return heat

def cal_dmg(v):
    if 10 <= v <= 25:
        return 50
    else:
        # linear assumed, expected value returned
        prob_500 = 1 / (45 - 25) * (v - 25)
        return prob_500 * 500 + (1 - prob_500) * 50

HEAT_LIMIT = 1600
COOL_SPEED = 500

v_list = np.arange(10, 46)                       # m/s
f_list = np.linspace(0.1, 5, num=49)             # /s

dmg_array = np.zeros((len(v_list), len(f_list)))
for v_index, v in enumerate(v_list):
    for f_index, f in enumerate(f_list):
        dmg = 0
        heat = 0
        counter = 0
        for t in np.linspace(0, 100, num=50*100, endpoint=False):   # 50Hz
            if t > counter * 1.0 / f:
                if heat + cal_heat(v) < HEAT_LIMIT:
                    dmg += cal_dmg(v)
                    heat += cal_heat(v)
                counter += 1
            heat = cool_down(heat)

        dmg_array[v_index][f_index] = dmg / 100

fig = plt.figure()
ax = fig.gca(projection='3d')
v_list, f_list = np.meshgrid(f_list, v_list)
surf = ax.plot_surface(v_list, f_list, dmg_array, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.show()
